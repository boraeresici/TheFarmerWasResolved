__version__ = "0.1.1"

import config
import state


_snapshot_loop = -1
_target_unlock = None
_focus_item = None
_focus_missing = 0


def _unlock_plan():
	return [Unlocks.Dinosaurs, Unlocks.Mazes, Unlocks.Megafarm]


def _unlock_name(unlock_type):
	if unlock_type == Unlocks.Dinosaurs:
		return "Dinosaurs"
	if unlock_type == Unlocks.Mazes:
		return "Mazes"
	if unlock_type == Unlocks.Megafarm:
		return "Megafarm"
	return "Unknown"


def _item_name(item_type):
	if item_type == Items.Cactus:
		return "Cactus"
	if item_type == Items.Weird_Substance:
		return "Weird_Substance"
	if item_type == Items.Gold:
		return "Gold"
	if item_type == Items.Wood:
		return "Wood"
	if item_type == Items.Hay:
		return "Hay"
	if item_type == Items.Carrot:
		return "Carrot"
	return "Unknown"


def _cost_available():
	if not config.ENABLE_LOCKED_MODULE:
		return False
	if not config.LOCKED_REQUIRE_COSTS_UNLOCK:
		return True
	return num_unlocked(Unlocks.Costs) > 0


def _find_target_unlock():
	for unlock_type in _unlock_plan():
		if num_unlocked(unlock_type) <= 0:
			return unlock_type
	return None


def _missing_from_cost(cost):
	missing = {}
	if cost == None:
		return missing
	for item_type in cost:
		need = cost[item_type]
		have = num_items(item_type)
		if have < need:
			missing[item_type] = need - have
	return missing


def _largest_missing_item(missing):
	best_item = None
	best_amount = 0
	for item_type in missing:
		amount = missing[item_type]
		if amount > best_amount:
			best_item = item_type
			best_amount = amount
	return best_item, best_amount


def _pick_focus_item(target_unlock, missing):
	item_type, amount = _largest_missing_item(missing)
	if item_type == None:
		return None, 0

	# Prefer cactus push on early locked route.
	if target_unlock == Unlocks.Dinosaurs and item_type == Items.Cactus:
		return Items.Cactus, amount
	if target_unlock == Unlocks.Mazes and item_type == Items.Cactus:
		return Items.Cactus, amount

	# Megafarm usually needs gold-side progress.
	if target_unlock == Unlocks.Megafarm and item_type == Items.Gold:
		return Items.Gold, amount

	return item_type, amount


def _sync_state():
	if _target_unlock == None:
		state.locked_target_name = "none"
	else:
		state.locked_target_name = _unlock_name(_target_unlock)

	if _focus_item == None:
		state.locked_focus_item_name = "none"
	else:
		state.locked_focus_item_name = _item_name(_focus_item)

	state.locked_missing_amount = _focus_missing


def _refresh():
	global _snapshot_loop
	global _target_unlock
	global _focus_item
	global _focus_missing

	if _snapshot_loop == state.loop_count:
		return
	_snapshot_loop = state.loop_count

	_target_unlock = _find_target_unlock()
	_focus_item = None
	_focus_missing = 0

	if _target_unlock == None:
		_sync_state()
		return
	if not _cost_available():
		_sync_state()
		return

	cost = get_cost(_target_unlock)
	missing = _missing_from_cost(cost)
	_focus_item, _focus_missing = _pick_focus_item(_target_unlock, missing)
	_sync_state()


def _current_cost():
	if _target_unlock == None:
		return None
	if not _cost_available():
		return None
	return get_cost(_target_unlock)


def target_unlock_name():
	_refresh()
	return state.locked_target_name


def focus_item_name():
	_refresh()
	return state.locked_focus_item_name


def focus_missing_amount():
	_refresh()
	return state.locked_missing_amount


def required_amount(item_type):
	_refresh()
	cost = _current_cost()
	if cost == None:
		return 0
	if item_type in cost:
		return cost[item_type]
	return 0


def missing_amount(item_type):
	required = required_amount(item_type)
	if required <= 0:
		return 0
	have = num_items(item_type)
	if have >= required:
		return 0
	return required - have


def should_force_cactus_for_goal():
	return missing_amount(Items.Cactus) > 0


def should_push_bush_for_goal():
	_refresh()
	return _focus_item == Items.Weird_Substance


def mode_bonus(mode):
	_refresh()
	if not config.ENABLE_LOCKED_MODULE:
		return 0
	if _focus_item == None:
		return 0

	if _focus_item == Items.Cactus and mode == "cactus":
		return config.LOCKED_PRIORITY_BONUS
	if _focus_item == Items.Weird_Substance and mode == "maze_focus":
		return config.LOCKED_PRIORITY_BONUS
	if _focus_item == Items.Gold:
		if mode == "maze_focus":
			return config.LOCKED_GOLD_PRIORITY_BONUS
		if mode == "cactus":
			return config.LOCKED_PRIORITY_BONUS // 2
	if _focus_item == Items.Wood and (mode == "tree_boost" or mode == "tree_fallback"):
		return config.LOCKED_PRIORITY_BONUS
	if _focus_item == Items.Hay and mode == "hay_recovery":
		return config.LOCKED_PRIORITY_BONUS
	if _focus_item == Items.Carrot and mode == "carrot_recovery":
		return config.LOCKED_PRIORITY_BONUS
	return 0
