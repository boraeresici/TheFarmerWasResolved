# The Farmer Was Replaced — Project Handover (2026-02-16) amass oyunun doğru mantıkta ideal hedefleri adım adım aktif edip geliştirilmesi

## Current Goal
Build a self-balancing farm controller that:
- Follows HARD goal: keep Wood >= 3200 (required for water progress / upgrades)
- Dynamically adapts to world size changes (e.g., Expand unlock from 6x6 to 8x8+)
- Avoids leaving unplanted/unmanaged tiles
- Uses Pumpkin as a high-yield strategy ONLY when economy allows (not the main focus)

## Environment / Constraints
- macOS
- Game scripting is Python-like but limited (no real file I/O, no full Python stdlib).
- Some APIs may not exist; we rely on `num_items`, `plant`, `harvest`, `till`, `can_harvest`, movement, `get_world_size`, `get_pos_x/get_pos_y` if available.

## Known Issues Encountered
1) `config.wood_for_water_boost does not exist`
   - Root cause: mismatched naming (lowercase vs uppercase constant).
   - Fix: add alias in config: `wood_for_water_boost = WOOD_FOR_WATER_BOOST`.

2) `grid handle_tile takes 0 arguments you called it with these arguments`
   - Root cause: grid calls `actions.handle_tile(size)` but actions defined `handle_tile()` with no params.
   - Fix: define `handle_tile(world_size)` in actions.

3) "Some tiles are still unplanted/unhandled"
   - Likely root cause: traversal logic skips tiles when world_size increases.
   - Fix: deterministic serpentine traversal that processes exactly `size*size` tiles.

## Version Map (latest recommended)
- main.py __version__ = "0.3.0"
- state.py __version__ = "0.3.2"
- config.py __version__ = "0.6.10"
- economy.py __version__ = "0.7.15"
- pumpkin.py __version__ = "0.4.6"
- actions.py __version__ = "0.5.4"
- grid.py __version__ = "0.3.4"

## Key Design
### Economy (not pumpkin-first)
- `decide_base_crop()` controls grass/bush/carrot.
- HARD: if wood < 3200 => bush.
- Soft balancing: maintain hay, carrot buffer, avoid wood lagging behind.
- Pumpkin is enabled only when economy allows: wood goal met + carrot buffer.
- Sunflower fallback is enabled when power is low and economy headroom is safe.
- Tree boost mode is enabled while wood is below hard-goal headroom.
- Timing-aware phase logic is enabled when `Unlocks.Timing` is available.
- Utilities-aware random polyculture mode is enabled when `Unlocks.Utilities` is available.
- Sunflower/Pumpkin can run with time-window duty cycles.
- Cactus mode is enabled with economy + stock + time-window gating.

### Pumpkin Area
- Square is centered and adaptive: size is computed by economy `pumpkin_square_size(world_size)`.
- This prevents static 6x6 issues after Expand.

### Grid
- Must process every tile each loop, independent of world size.

## Next Steps
1) Reintroduce water/fertilizer logic into actions once grid traversal + signatures are stable.
2) Add "Goal/Unlock queue" if unlock APIs are not available, but keep it config-driven (avoid touching economy each time).
3) Improve dependency graph for costs (carrot costs, pumpkin costs, water requirements).

---

## Current Stable Snapshot (2026-02-16)

This snapshot reflects the latest synced state after overwrite recovery.

### File Versions
- `files/main.py` -> `__version__ = "0.3.0"`
- `files/state.py` -> `__version__ = "0.3.2"`
- `files/config.py` -> `__version__ = "0.6.10"`
- `files/economy.py` -> `__version__ = "0.7.15"`
- `files/pumpkin.py` -> `__version__ = "0.4.6"`
- `files/actions.py` -> `__version__ = "0.5.4"`
- `files/grid.py` -> `__version__ = "0.3.4"`

### Required Contracts
- `actions.handle_tile(world_size)` exists and is called by grid traversal.
- `economy.decide_base_crop(world_size, x, y)` signature must match action calls.
- `grid.run_forever()` is the main execution entry called by `main.py`.

### Compatibility Behavior
- Expand level `0`: single-tile mode.
- Expand level `1`: line traversal mode (fallback tile count).
- Expand level `>= 2`: full square traversal using `get_world_size()`.
- Before `Unlocks.Costs`, planting checks avoid direct `get_cost()` dependency.
- `economy.should_run_pumpkin_program(world_size)` alias exists for old `actions.py`.
- `economy.decide_base_crop(...)` accepts both old no-arg and new `(world_size, x, y)` calls.
- `state.py` is syntax-safe for game parser (no `global` statements).
- Sunflower compatibility uses `Entities.Sunflower` (singular).
- Trees use checkerboard placement with headroom-based boost window.
- If Timing is unlocked, `grid` updates `state.game_time` from `get_time()` each loop.
- Early phase gates can disable Sunflower/Pumpkin modes temporarily.
- If Utilities is unlocked, random polyculture weighting can be used.
- Time windows can gate Sunflower/Pumpkin activity within each cycle.
- Cactus uses `Unlocks.Cactus` + `Entities.Cactus` with configurable stock/headroom/time thresholds.

### Hard Rules
- Keep `Wood >= 3200` as hard floor.
- Process all tiles in square mode (`size * size` per cycle).
- Pumpkin is gated by economy (`wood + carrot buffer`) and uses centered adaptive area.
