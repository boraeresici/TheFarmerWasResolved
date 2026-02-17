__version__ = "0.7.28"

import config
import locked
import state


def _refresh_resource_snapshot():
	if state.snapshot_loop == state.loop_count:
		return
	state.snapshot_loop = state.loop_count
	state.snapshot_wood = num_items(Items.Wood)
	state.snapshot_hay = num_items(Items.Hay)
	state.snapshot_carrot = num_items(Items.Carrot)
	state.snapshot_power = num_items(Items.Power)
	state.snapshot_cactus = num_items(Items.Cactus)
	state.snapshot_weird_substance = num_items(Items.Weird_Substance)


def item_count(item_type):
	_refresh_resource_snapshot()
	if item_type == Items.Wood:
		return state.snapshot_wood
	if item_type == Items.Hay:
		return state.snapshot_hay
	if item_type == Items.Carrot:
		return state.snapshot_carrot
	if item_type == Items.Power:
		return state.snapshot_power
	if item_type == Items.Cactus:
		return state.snapshot_cactus
	if item_type == Items.Weird_Substance:
		return state.snapshot_weird_substance
	return num_items(item_type)


def unlock_level(unlock_type):
	return num_unlocked(unlock_type)


def has_unlock(unlock_type):
	return num_unlocked(unlock_type) > 0


def unlock_count(unlock_type):
	return num_unlocked(unlock_type)


def can_pay(cost):
	if cost == None:
		return True
	for item in cost:
		if num_items(item) < cost[item]:
			return False
	return True


def can_plant(entity_type):
	# Before Costs unlock, get_cost() may be unavailable.
	if not has_unlock(Unlocks.Costs):
		return True
	return can_pay(get_cost(entity_type))


def target_hay_buffer():
	if has_unlock(Unlocks.Watering):
		return config.MIN_HAY_BUFFER_LATE
	return config.MIN_HAY_BUFFER


def target_carrot_buffer():
	if has_unlock(Unlocks.Pumpkins):
		return config.MIN_CARROT_BUFFER_WITH_PUMPKIN
	return config.MIN_CARROT_BUFFER


def target_pumpkin_carrot_buffer():
	return config.PUMPKIN_CARROT_BUFFER


def update_recovery_mode(current_value, target_value, exit_margin, was_recovery):
	if was_recovery:
		if current_value >= target_value + exit_margin:
			return False
		return True
	if current_value < target_value:
		return True
	return False


def update_mode_hysteresis(current_value, enable_threshold, disable_threshold, was_active):
	if was_active:
		if current_value >= disable_threshold:
			return False
		return True
	if current_value < enable_threshold:
		return True
	return False


def hay_recovery_active(hay):
	state.hay_recovery_mode = update_recovery_mode(
		hay,
		target_hay_buffer(),
		config.HAY_RECOVERY_EXIT_MARGIN,
		state.hay_recovery_mode,
	)
	return state.hay_recovery_mode


def carrot_recovery_active(carrots):
	if not has_unlock(Unlocks.Carrots):
		state.carrot_recovery_mode = False
		return False
	state.carrot_recovery_mode = update_recovery_mode(
		carrots,
		target_carrot_buffer(),
		config.CARROT_RECOVERY_EXIT_MARGIN,
		state.carrot_recovery_mode,
	)
	return state.carrot_recovery_mode


def target_cactus_buffer():
	locked_target = locked.required_amount(Items.Cactus)
	if locked_target > 0:
		return locked_target
	if has_unlock(Unlocks.Dinosaurs):
		return config.DINOSAUR_CACTUS_BUFFER
	return config.MIN_CACTUS_BUFFER


def target_maze_prep_weird_substance():
	return config.MAZE_PREP_WEIRD_SUBSTANCE_TARGET


def target_weird_substance_buffer():
	return config.MIN_WEIRD_SUBSTANCE_BUFFER


def maze_prep_active():
	if not config.ENABLE_MAZE_PREP_MODE:
		return False
	if has_unlock(Unlocks.Mazes):
		return False
	if not has_unlock(Unlocks.Fertilizer):
		return False
	return item_count(Items.Weird_Substance) < target_maze_prep_weird_substance()


def should_spend_fertilizer():
	if maze_prep_active():
		return config.MAZE_PREP_USE_FERTILIZER
	if has_unlock(Unlocks.Mazes) and config.ENABLE_FERTILIZER_AFTER_MAZE:
		if item_count(Items.Weird_Substance) < target_weird_substance_buffer():
			return True
	return config.ENABLE_FERTILIZER


def should_focus_bush_for_maze():
	if not has_unlock(Unlocks.Mazes):
		return False
	if item_count(Items.Weird_Substance) >= target_weird_substance_buffer():
		return False
	return True


def has_utilities_unlock():
	return has_unlock(Unlocks.Utilities)


def in_time_window(cycle_seconds, active_seconds):
	t = game_time_seconds()
	if t < 0:
		return True
	if cycle_seconds <= 0:
		return True
	return (t % cycle_seconds) < active_seconds


def should_use_sunflowers(wood, hay, carrots):
	if in_early_game_phase() and config.EARLY_DISABLE_SUNFLOWERS:
		state.sunflower_mode_active = False
		return False
	if not config.ENABLE_SUNFLOWER_MODE:
		state.sunflower_mode_active = False
		return False
	if not has_unlock(Unlocks.Sunflowers):
		state.sunflower_mode_active = False
		return False
	power = item_count(Items.Power)
	state.sunflower_mode_active = update_mode_hysteresis(
		power,
		config.MIN_POWER_BUFFER,
		config.MIN_POWER_BUFFER + config.SUNFLOWER_DISABLE_MARGIN,
		state.sunflower_mode_active,
	)
	if not state.sunflower_mode_active:
		return False
	if wood < config.WOOD_FOR_WATER_BOOST + config.SUNFLOWER_WOOD_HEADROOM:
		return False
	if hay < target_hay_buffer():
		return False
	if has_unlock(Unlocks.Carrots) and carrots < target_carrot_buffer():
		return False
	if state.timing_unlocked:
		if not in_time_window(config.SUNFLOWER_TIME_CYCLE, config.SUNFLOWER_ACTIVE_SECONDS):
			return False
	return True


def should_use_polyculture(wood, carrots):
	if not config.ENABLE_POLYCULTURE_MODE:
		return False
	if not has_unlock(Unlocks.Polyculture):
		return False
	if wood < config.WOOD_FOR_WATER_BOOST + config.POLYCULTURE_WOOD_HEADROOM:
		return False
	if not has_unlock(Unlocks.Carrots):
		return False
	if carrots < target_carrot_buffer() + config.POLYCULTURE_CARROT_HEADROOM:
		return False
	return True


def should_use_cactus(wood, hay, carrots):
	if maze_prep_active() and config.MAZE_PREP_DISABLE_CACTUS and not locked.should_force_cactus_for_goal():
		state.cactus_mode_active = False
		return False
	if not config.ENABLE_CACTUS_MODE:
		state.cactus_mode_active = False
		return False
	if not has_unlock(Unlocks.Cactus):
		state.cactus_mode_active = False
		return False
	cactus_count = item_count(Items.Cactus)
	cactus_target = target_cactus_buffer()
	state.cactus_mode_active = update_mode_hysteresis(
		cactus_count,
		cactus_target,
		cactus_target + config.CACTUS_DISABLE_MARGIN,
		state.cactus_mode_active,
	)
	if not state.cactus_mode_active:
		return False
	if wood < config.WOOD_FOR_WATER_BOOST + config.CACTUS_WOOD_HEADROOM:
		return False
	if hay < target_hay_buffer():
		return False
	if has_unlock(Unlocks.Carrots):
		if carrots < target_carrot_buffer() + config.CACTUS_CARROT_HEADROOM:
			return False
	if state.timing_unlocked:
		if not in_time_window(config.CACTUS_TIME_CYCLE, config.CACTUS_ACTIVE_SECONDS):
			return False
	return True


def random_poly_weights():
	# Dictionaries unlocked: keep random mix in a single weights table.
	tree = config.RANDOM_POLY_TREE_CHANCE
	carrot = config.RANDOM_POLY_CARROT_CHANCE
	bush = config.RANDOM_POLY_BUSH_CHANCE
	grass = 1 - (tree + carrot + bush)
	if grass < 0:
		grass = 0
	return {
		Entities.Tree: tree,
		Entities.Carrot: carrot,
		Entities.Bush: bush,
		Entities.Grass: grass,
	}


def polyculture_mix_crop(x, y):
	if config.ENABLE_RANDOM_POLYCULTURE and has_utilities_unlock():
		r = random()
		weights = random_poly_weights()
		cumulative = 0
		selected = Entities.Grass
		for entity in [Entities.Tree, Entities.Carrot, Entities.Bush, Entities.Grass]:
			cumulative = cumulative + weights[entity]
			if r < cumulative:
				selected = entity
				break
		if selected == Entities.Tree:
			if has_unlock(Unlocks.Trees) and tree_tile_allowed(x, y):
				return Entities.Tree
			return Entities.Bush
		return selected

	# Lists unlocked: keep base rotation maintainable via a list table.
	rotation = [Entities.Tree, Entities.Carrot, Entities.Bush, Entities.Grass]
	preferred = rotation[(x + y) % len(rotation)]
	if preferred == Entities.Tree:
		if has_unlock(Unlocks.Trees) and tree_tile_allowed(x, y):
			return Entities.Tree
		return Entities.Bush
	return preferred


def tree_tile_allowed(x, y):
	# Checkerboard-like spacing lowers tree adjacency penalties.
	return (x + y) % 2 == 0


def game_time_seconds():
	if state.timing_unlocked:
		return state.game_time
	return -1


def in_early_game_phase():
	if not config.ENABLE_TIME_PHASES:
		return False
	t = game_time_seconds()
	if t < 0:
		return False
	return t < config.EARLY_GAME_SECONDS


def should_use_tree_boost(wood):
	if not has_unlock(Unlocks.Trees):
		return False

	headroom = config.TREE_WOOD_HEADROOM
	if in_early_game_phase():
		headroom = headroom + config.EARLY_TREE_EXTRA_HEADROOM

	if wood < config.WOOD_FOR_WATER_BOOST + headroom:
		return True
	return False


def _pick_best_mode(candidates):
	if len(candidates) <= 0:
		return "bush_fallback", config.SCORE_BUSH_FALLBACK

	best_mode = candidates[0][0]
	best_score = candidates[0][1]
	for mode, score in candidates:
		if score > best_score:
			best_mode = mode
			best_score = score
		elif score == best_score and mode == state.current_mode:
			best_mode = mode
			best_score = score
	return best_mode, best_score


def _score_for_mode(candidates, target_mode):
	for mode, score in candidates:
		if mode == target_mode:
			return score
	return None


def _add_scored_candidate(candidates, mode, base_score):
	candidates.append((mode, base_score + locked.mode_bonus(mode)))


def _select_strategy_mode(wood, hay, carrots):
	if wood < config.WOOD_FOR_WATER_BOOST:
		return "wood_floor", 1000

	candidates = []
	if hay_recovery_active(hay):
		_add_scored_candidate(candidates, "hay_recovery", config.SCORE_HAY_RECOVERY)
	if carrot_recovery_active(carrots):
		_add_scored_candidate(candidates, "carrot_recovery", config.SCORE_CARROT_RECOVERY)
	if should_focus_bush_for_maze():
		_add_scored_candidate(candidates, "maze_focus", config.SCORE_MAZE_FOCUS)
	if locked.should_push_bush_for_goal():
		_add_scored_candidate(candidates, "maze_focus", config.SCORE_MAZE_FOCUS)
	if should_use_tree_boost(wood):
		_add_scored_candidate(candidates, "tree_boost", config.SCORE_TREE_BOOST)
	if should_use_sunflowers(wood, hay, carrots):
		_add_scored_candidate(candidates, "sunflower", config.SCORE_SUNFLOWER)
	if should_use_cactus(wood, hay, carrots):
		_add_scored_candidate(candidates, "cactus", config.SCORE_CACTUS)
	if should_use_polyculture(wood, carrots):
		_add_scored_candidate(candidates, "polyculture", config.SCORE_POLYCULTURE)
	if has_unlock(Unlocks.Trees):
		_add_scored_candidate(candidates, "tree_fallback", config.SCORE_TREE_FALLBACK)

	best_mode, best_score = _pick_best_mode(candidates)

	# Keep current mode for a few loops to reduce rapid mode switching.
	if config.ENABLE_MODE_LOCK and state.current_mode != "init":
		if state.last_mode_change_loop >= 0:
			held_loops = state.loop_count - state.last_mode_change_loop
			if held_loops < config.MODE_MIN_HOLD_LOOPS:
				current_score = _score_for_mode(candidates, state.current_mode)
				if current_score != None:
					return state.current_mode, current_score

	return best_mode, best_score


def _mode_to_entity(mode, x, y):
	if mode == "wood_floor":
		return Entities.Bush
	if mode == "hay_recovery":
		return Entities.Grass
	if mode == "carrot_recovery":
		return Entities.Carrot
	if mode == "maze_focus":
		return Entities.Bush
	if mode == "tree_boost" or mode == "tree_fallback":
		if tree_tile_allowed(x, y):
			return Entities.Tree
		return Entities.Bush
	if mode == "sunflower":
		return Entities.Sunflower
	if mode == "cactus":
		return Entities.Cactus
	if mode == "polyculture":
		return polyculture_mix_crop(x, y)
	return Entities.Bush


def decide_base_crop(world_size=None, x=None, y=None):
	# Backward compatibility: older actions.py may call with no arguments.
	if x == None:
		x = 0
	if y == None:
		y = 0

	wood = item_count(Items.Wood)
	hay = item_count(Items.Hay)
	carrots = item_count(Items.Carrot)

	if config.ENABLE_PRIORITY_SCHEDULER:
		mode, score = _select_strategy_mode(wood, hay, carrots)
		if mode != state.current_mode:
			state.last_mode_change_loop = state.loop_count
		state.current_mode = mode
		state.current_mode_score = score
		return _mode_to_entity(mode, x, y)

	if wood < config.WOOD_FOR_WATER_BOOST:
		return Entities.Bush
	if hay_recovery_active(hay):
		return Entities.Grass
	if carrot_recovery_active(carrots):
		return Entities.Carrot
	if should_focus_bush_for_maze():
		return Entities.Bush
	if should_use_tree_boost(wood):
		if tree_tile_allowed(x, y):
			return Entities.Tree
		return Entities.Bush
	if should_use_sunflowers(wood, hay, carrots):
		return Entities.Sunflower
	if should_use_cactus(wood, hay, carrots):
		return Entities.Cactus
	if should_use_polyculture(wood, carrots):
		return polyculture_mix_crop(x, y)
	if has_unlock(Unlocks.Trees):
		if tree_tile_allowed(x, y):
			return Entities.Tree
		return Entities.Bush
	return Entities.Bush


def pumpkin_enabled(world_size):
	_refresh_resource_snapshot()
	if maze_prep_active() and config.MAZE_PREP_DISABLE_PUMPKINS:
		state.pumpkin_mode_active = False
		return False
	if in_early_game_phase() and config.EARLY_DISABLE_PUMPKINS:
		state.pumpkin_mode_active = False
		return False
	if not has_unlock(Unlocks.Pumpkins):
		state.pumpkin_mode_active = False
		return False
	if item_count(Items.Wood) < config.WOOD_FOR_WATER_BOOST:
		state.pumpkin_mode_active = False
		return False

	carrots = item_count(Items.Carrot)
	enter_threshold = target_pumpkin_carrot_buffer() + config.PUMPKIN_ENABLE_MARGIN
	exit_threshold = target_pumpkin_carrot_buffer()
	if state.pumpkin_mode_active:
		if carrots < exit_threshold:
			state.pumpkin_mode_active = False
	else:
		if carrots >= enter_threshold:
			state.pumpkin_mode_active = True

	if not state.pumpkin_mode_active:
		return False

	if state.timing_unlocked:
		if not in_time_window(config.PUMPKIN_TIME_CYCLE, config.PUMPKIN_ACTIVE_SECONDS):
			return False
	return True


def should_run_pumpkin_program(world_size):
	# Backward-compatible alias for older actions.py versions.
	return pumpkin_enabled(world_size)


def pumpkin_square_size(world_size):
	size = config.PUMPKIN_MIN_SIZE
	if world_size < size:
		size = world_size
	if size < 1:
		size = 1
	if size > config.PUMPKIN_MAX_SIZE:
		size = config.PUMPKIN_MAX_SIZE
	return size


def pumpkin_bounds(world_size):
	square = pumpkin_square_size(world_size)
	start = (world_size - square) // 2
	end = start + square - 1
	return start, end
