__version__ = "0.5.10"

import config
import economy
import locked
import pumpkin
import state


def _maybe_rotate_hat():
	if not config.ENABLE_HAT_ROTATION:
		return
	if config.HAT_REQUIRE_UNLOCK and num_unlocked(Unlocks.Hats) <= 0:
		return
	# Avoid repeated hat changes during the same loop.
	if state.last_hat_change_loop == state.loop_count:
		return

	due = False
	if config.HAT_CHANGE_ON_FIRST_LOOP and state.loop_count == 1:
		due = True
	elif config.HAT_CHANGE_EVERY_LOOPS > 0 and state.loop_count % config.HAT_CHANGE_EVERY_LOOPS == 0:
		due = True
	if not due:
		return

	hats = [Hats.Gray_Hat, Hats.Purple_Hat, Hats.Green_Hat, Hats.Brown_Hat]
	index = 0

	if config.USE_RANDOM_HATS and num_unlocked(Unlocks.Utilities) > 0:
		r = random()
		if r < 0.25:
			index = 0
		elif r < 0.50:
			index = 1
		elif r < 0.75:
			index = 2
		else:
			index = 3
	else:
		index = (state.loop_count // config.HAT_CHANGE_EVERY_LOOPS) % len(hats)

	# Reduce chance of "no visible change" from selecting the same hat.
	if index == state.last_hat_index:
		index = (index + 1) % len(hats)

	change_hat(hats[index])
	state.last_hat_index = index
	state.last_hat_change_loop = state.loop_count


def _ensure_ground_for(entity_type):
	if entity_type == Entities.Carrot or entity_type == Entities.Pumpkin or entity_type == Entities.Sunflower or entity_type == Entities.Cactus:
		if get_ground_type() != Grounds.Soil:
			till()
		return

	# Grass/Bush/Tree can live on grassland. Keep soil usage focused.
	if get_ground_type() == Grounds.Soil and entity_type == Entities.Grass:
		till()


def _apply_generic_watering(in_pumpkin_mode):
	if not config.ENABLE_WATERING:
		return
	if num_unlocked(Unlocks.Watering) <= 0:
		return
	if num_items(Items.Water) <= 0:
		return

	target = config.WATER_TARGET
	if in_pumpkin_mode:
		target = config.WATER_TARGET_PUMPKIN

	if get_water() < target:
		use_item(Items.Water)


def _apply_fertilizer_if_enabled():
	if not economy.should_spend_fertilizer():
		return
	if num_unlocked(Unlocks.Fertilizer) <= 0:
		return
	if num_items(Items.Fertilizer) <= 0:
		return
	if not economy.maze_prep_active() and num_items(Items.Fertilizer) < config.MIN_FERTILIZER_STOCK:
		return
	if not can_harvest():
		use_item(Items.Fertilizer)


def _maybe_print_status():
	if not config.ENABLE_STATUS_OUTPUT:
		return
	if state.current_x != 0 or state.current_y != 0:
		return
	if config.STATUS_OUTPUT_EVERY_LOOPS <= 0:
		return
	if state.loop_count % config.STATUS_OUTPUT_EVERY_LOOPS != 0:
		return

	target = locked.target_unlock_name()
	focus = locked.focus_item_name()
	missing = locked.focus_missing_amount()
	if num_unlocked(Unlocks.Timing) > 0:
		quick_print(
			"[status]",
			"loop=", state.loop_count,
			"mode=", state.current_mode,
			"score=", state.current_mode_score,
			"target=", target,
			"focus=", focus,
			"missing=", missing,
		)
		return
	print(
		"[status]",
		"loop=", state.loop_count,
		"mode=", state.current_mode,
		"score=", state.current_mode_score,
		"target=", target,
		"focus=", focus,
		"missing=", missing,
	)


def _manage_base_tile(world_size):
	x = state.current_x
	y = state.current_y
	target = economy.decide_base_crop(world_size, x, y)

	if target == Entities.Grass:
		if can_harvest():
			harvest()
		_ensure_ground_for(Entities.Grass)
		_apply_generic_watering(False)
		return

	_ensure_ground_for(target)

	entity = get_entity_type()
	if entity == target:
		if can_harvest():
			harvest()
			if economy.can_plant(target):
				plant(target)
		_apply_generic_watering(False)
		_apply_fertilizer_if_enabled()
		return

	if entity != None and can_harvest():
		harvest()

	if economy.can_plant(target):
		plant(target)

	_apply_generic_watering(False)
	_apply_fertilizer_if_enabled()


def handle_tile(world_size):
	# Required function signature: grid calls handle_tile(world_size).
	_maybe_rotate_hat()
	_maybe_print_status()
	pumpkin_mode = economy.pumpkin_enabled(world_size)
	if pumpkin_mode and pumpkin.handle_pumpkin_tile(world_size):
		return
	_manage_base_tile(world_size)
