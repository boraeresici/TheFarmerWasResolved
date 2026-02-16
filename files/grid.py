__version__ = "0.3.4"

import actions
import config
import economy
import state


def _update_game_time():
	if economy.unlock_count(Unlocks.Timing) > 0:
		state.timing_unlocked = True
		state.game_time = get_time()
		return
	state.timing_unlocked = False
	state.game_time = -1


def _resolve_world_size():
	if economy.unlock_count(Unlocks.Expand) >= 2:
		return get_world_size()
	return config.FALLBACK_WORLD_SIZE


def _run_single_tile():
	state.current_x = 0
	state.current_y = 0
	actions.handle_tile(1)


def _run_line_mode():
	# Expand1 phase: movement exists, but world-size helpers may not.
	y = 0
	while y < config.FALLBACK_LINE_TILES:
		state.current_x = 0
		state.current_y = y
		actions.handle_tile(config.FALLBACK_WORLD_SIZE)
		y += 1
		if y < config.FALLBACK_LINE_TILES:
			move(North)


def _run_square_mode(world_size):
	state.last_world_size = world_size

	# Traverses exactly world_size * world_size tiles every cycle.
	x = 0
	while x < world_size:
		y = 0
		while y < world_size:
			state.current_x = x
			state.current_y = y
			actions.handle_tile(world_size)
			y += 1
			if y < world_size:
				move(North)
		x += 1
		move(East)


def run_once():
	expand_level = economy.unlock_count(Unlocks.Expand)
	if expand_level <= 0:
		_run_single_tile()
		return
	if expand_level == 1:
		_run_line_mode()
		return

	world_size = _resolve_world_size()
	_run_square_mode(world_size)


def run_forever():
	while True:
		state.loop_count = state.loop_count + 1
		_update_game_time()
		run_once()
