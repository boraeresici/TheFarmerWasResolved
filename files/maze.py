__version__ = "0.2.0"

import config
import economy
import state


def maze_enabled(world_size):
	if not config.ENABLE_MAZE_PROGRAM:
		return False
	if economy.unlock_count(Unlocks.Mazes) <= 0:
		return False
	if economy.item_count(Items.Weird_Substance) < config.MAZE_PROGRAM_MIN_SUBSTANCE:
		return False
	return True


def _substance_amount(world_size):
	amount = config.MAZE_PROGRAM_SUBSTANCE_AMOUNT
	if amount <= 0:
		# Full-field amount for current maze upgrade level.
		level = economy.unlock_count(Unlocks.Mazes)
		if level < 1:
			level = 1
		amount = world_size * 2 ** (level - 1)
	if amount < 1:
		amount = 1
	if economy.item_count(Items.Weird_Substance) < amount:
		return 0
	return amount


def _ensure_bush():
	entity = get_entity_type()
	if entity == Entities.Bush:
		return True
	if entity == Entities.Treasure:
		if can_harvest():
			harvest()
		return False
	if entity == Entities.Hedge:
		# Reset maze tile if we are not on treasure.
		if can_harvest():
			harvest()
		return False
	if entity != None and can_harvest():
		harvest()
	if economy.can_plant(Entities.Bush):
		plant(Entities.Bush)
		return True
	return False


def _harvest_treasure_if_present():
	if get_entity_type() == Entities.Treasure and can_harvest():
		harvest()
		return True
	return False


def _return_to_origin():
	if not config.MAZE_PROGRAM_RETURN_TO_ORIGIN:
		return
	while get_pos_x() != 0:
		move(West)
	while get_pos_y() != 0:
		move(South)


def _solve_maze_wall_follow():
	if not config.MAZE_PROGRAM_ENABLE_SOLVER:
		return
	directions = [North, East, South, West]
	index = 0
	steps = 0
	while steps < config.MAZE_PROGRAM_MAX_STEPS:
		steps += 1
		if get_entity_type() == Entities.Treasure:
			return

		right = (index + 1) % 4
		if can_move(directions[right]):
			index = right
			move(directions[index])
			continue

		if can_move(directions[index]):
			move(directions[index])
			continue

		left = (index - 1) % 4
		if can_move(directions[left]):
			index = left
			move(directions[index])
			continue

		back = (index + 2) % 4
		index = back
		if can_move(directions[index]):
			move(directions[index])
			continue
		return


def _solve_existing_maze():
	_harvest_treasure_if_present()
	if get_entity_type() != Entities.Hedge:
		return
	_solve_maze_wall_follow()
	_harvest_treasure_if_present()


def handle_maze_tile(world_size):
	if config.MAZE_PROGRAM_ONLY_ON_ORIGIN:
		if state.current_x != 0 or state.current_y != 0:
			return False

	entity = get_entity_type()
	if entity == Entities.Hedge or entity == Entities.Treasure:
		_solve_existing_maze()
		_return_to_origin()
		return True

	if not _ensure_bush():
		return True

	amount = _substance_amount(world_size)
	if amount <= 0:
		return True

	use_item(Items.Weird_Substance, amount)

	_harvest_treasure_if_present()
	_solve_existing_maze()
	_return_to_origin()
	return True
