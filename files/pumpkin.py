__version__ = "0.4.6"

import config
import economy
import state


def in_pumpkin_zone(x, y, world_size):
	start, end = economy.pumpkin_bounds(world_size)
	return x >= start and x <= end and y >= start and y <= end


def force_reseed_now():
	if state.loop_count <= 0:
		return False
	return state.loop_count % config.PUMPKIN_FORCE_RESEED_EVERY == 0


def _ensure_soil():
	if get_ground_type() != Grounds.Soil:
		till()


def _apply_water_if_needed():
	if not config.ENABLE_WATERING:
		return
	if num_unlocked(Unlocks.Watering) <= 0:
		return
	if num_items(Items.Water) <= 0:
		return
	if get_water() < config.WATER_TARGET_PUMPKIN:
		use_item(Items.Water)


def handle_pumpkin_tile(world_size):
	x = state.current_x
	y = state.current_y
	if not in_pumpkin_zone(x, y, world_size):
		return False

	_ensure_soil()
	_apply_water_if_needed()

	entity = get_entity_type()
	if entity == Entities.Pumpkin:
		if can_harvest():
			harvest()
			if economy.can_plant(Entities.Pumpkin):
				plant(Entities.Pumpkin)
		elif force_reseed_now() and economy.can_plant(Entities.Pumpkin):
			# Periodic reseed helps clear dead pumpkins that never become harvestable.
			plant(Entities.Pumpkin)
		return True

	if entity != None and can_harvest():
		harvest()

	if economy.can_plant(Entities.Pumpkin):
		plant(Entities.Pumpkin)
	return True
