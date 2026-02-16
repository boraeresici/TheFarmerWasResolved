__version__ = "0.1.3"


def _print_line(a=None, b=None, c=None, d=None, e=None, f=None, g=None, h=None):
	# Always print to air for visibility. Also mirror to output via quick_print if available.
	use_quick = num_unlocked(Unlocks.Timing) > 0
	if b == None:
		print(a)
		if use_quick:
			quick_print(a)
		return
	if c == None:
		print(a, b)
		if use_quick:
			quick_print(a, b)
		return
	if d == None:
		print(a, b, c)
		if use_quick:
			quick_print(a, b, c)
		return
	if e == None:
		print(a, b, c, d)
		if use_quick:
			quick_print(a, b, c, d)
		return
	if f == None:
		print(a, b, c, d, e)
		if use_quick:
			quick_print(a, b, c, d, e)
		return
	if g == None:
		print(a, b, c, d, e, f)
		if use_quick:
			quick_print(a, b, c, d, e, f)
		return
	if h == None:
		print(a, b, c, d, e, f, g)
		if use_quick:
			quick_print(a, b, c, d, e, f, g)
		return
	print(a, b, c, d, e, f, g, h)
	if use_quick:
		quick_print(a, b, c, d, e, f, g, h)


def _run_single(seed, speedup):
	filename = "main"
	sim_unlocks = {}
	sim_items = {}
	sim_globals = {}
	return simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)


def run_locked_benchmark(seeds=None, speedup=64):
	# Benchmarks current farm automation route from a clean start state.
	_print_line("[sim] benchmark requested")
	if num_unlocked(Unlocks.Simulation) <= 0:
		_print_line("[sim] Unlocks.Simulation is not unlocked, skipping benchmark")
		return None

	if seeds == None:
		seeds = [1, 2, 3, 4, 5]

	if len(seeds) <= 0:
		_print_line("[sim] no seeds")
		return None

	total = 0
	best = None
	worst = None

	_print_line("[sim] note", "quick test:", "3-5 seeds")
	_print_line("[sim] note", "release test:", "30+ seeds")
	_print_line("[sim] start", "speedup=", speedup, "seeds=", len(seeds))
	for seed in seeds:
		run_time = _run_single(seed, speedup)
		total = total + run_time

		if best == None or run_time < best:
			best = run_time
		if worst == None or run_time > worst:
			worst = run_time

		# Keep output concise to avoid clutter in air-print mode.
		_print_line("[sim]", "seed=", seed, "time=", run_time)

	avg = total / len(seeds)
	_print_line("[sim] done", "avg=", avg, "best=", best, "worst=", worst)
	return {
		"avg": avg,
		"best": best,
		"worst": worst,
		"count": len(seeds),
	}


def _start_live_main():
	if num_unlocked(Unlocks.Import) <= 0:
		_print_line("[sim] import unlock missing, cannot auto-start main")
		return
	_print_line("[sim] switching to live main")
	import main


def main():
	# Run benchmark first, then continue with live farm loop automatically.
	result = run_locked_benchmark()
	if result == None:
		_print_line("[sim] running live main directly")
	_start_live_main()


main()
