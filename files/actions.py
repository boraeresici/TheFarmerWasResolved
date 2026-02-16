__version__ = "0.5.4"

import config
import economy
import pumpkin
import state


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
	if not config.ENABLE_FERTILIZER:
		return
	if num_unlocked(Unlocks.Fertilizer) <= 0:
		return
	if num_items(Items.Fertilizer) < config.MIN_FERTILIZER_STOCK:
		return
	if not can_harvest():
		use_item(Items.Fertilizer)


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
	pumpkin_mode = economy.pumpkin_enabled(world_size)
	if pumpkin_mode and pumpkin.handle_pumpkin_tile(world_size):
		return
	_manage_base_tile(world_size)
