__version__ = "0.7.15"

import config
import state


def item_count(item_type):
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


def target_cactus_buffer():
	return config.MIN_CACTUS_BUFFER


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
		return False
	if not config.ENABLE_SUNFLOWER_MODE:
		return False
	if not has_unlock(Unlocks.Sunflowers):
		return False
	if item_count(Items.Power) >= config.MIN_POWER_BUFFER:
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
	if not config.ENABLE_CACTUS_MODE:
		return False
	if not has_unlock(Unlocks.Cactus):
		return False
	if item_count(Items.Cactus) >= target_cactus_buffer():
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


def polyculture_mix_crop(x, y):
	if config.ENABLE_RANDOM_POLYCULTURE and has_utilities_unlock():
		r = random()
		tree_cutoff = config.RANDOM_POLY_TREE_CHANCE
		carrot_cutoff = tree_cutoff + config.RANDOM_POLY_CARROT_CHANCE
		bush_cutoff = carrot_cutoff + config.RANDOM_POLY_BUSH_CHANCE

		if r < tree_cutoff:
			if has_unlock(Unlocks.Trees) and tree_tile_allowed(x, y):
				return Entities.Tree
			return Entities.Bush
		if r < carrot_cutoff:
			return Entities.Carrot
		if r < bush_cutoff:
			return Entities.Bush
		return Entities.Grass

	pattern = (x + y) % 4
	if pattern == 0:
		if has_unlock(Unlocks.Trees) and tree_tile_allowed(x, y):
			return Entities.Tree
		return Entities.Bush
	if pattern == 1:
		return Entities.Carrot
	if pattern == 2:
		return Entities.Bush
	return Entities.Grass


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


def decide_base_crop(world_size=None, x=None, y=None):
	# Backward compatibility: older actions.py may call with no arguments.
	if x == None:
		x = 0
	if y == None:
		y = 0

	wood = item_count(Items.Wood)
	hay = item_count(Items.Hay)
	carrots = item_count(Items.Carrot)

	if wood < config.WOOD_FOR_WATER_BOOST:
		return Entities.Bush

	if hay < target_hay_buffer():
		return Entities.Grass

	if has_unlock(Unlocks.Carrots) and carrots < target_carrot_buffer():
		return Entities.Carrot

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
	if in_early_game_phase() and config.EARLY_DISABLE_PUMPKINS:
		return False
	if not has_unlock(Unlocks.Pumpkins):
		return False
	if item_count(Items.Wood) < config.WOOD_FOR_WATER_BOOST:
		return False
	if item_count(Items.Carrot) < target_pumpkin_carrot_buffer():
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
