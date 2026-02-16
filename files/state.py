__version__ = "0.3.9"

loop_count = 0
last_world_size = -1
last_base_crop = None
current_x = 0
current_y = 0

# Timing state (set by grid loop when Unlocks.Timing is available).
timing_unlocked = False
game_time = -1

# Hat rotation state.
last_hat_change_loop = -1
last_hat_index = -1

# Buffer recovery state (hysteresis).
hay_recovery_mode = False
carrot_recovery_mode = False

# Per-loop resource snapshot for stable decisions.
snapshot_loop = -1
snapshot_wood = 0
snapshot_hay = 0
snapshot_carrot = 0
snapshot_power = 0
snapshot_cactus = 0
snapshot_weird_substance = 0

# Pumpkin mode hysteresis state.
pumpkin_mode_active = False
sunflower_mode_active = False
cactus_mode_active = False

# Strategy scheduler state.
current_mode = "init"
current_mode_score = 0
last_mode_change_loop = -1

# Locked-goal planner state.
locked_target_name = "none"
locked_focus_item_name = "none"
locked_missing_amount = 0
