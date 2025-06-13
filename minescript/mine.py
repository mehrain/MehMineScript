import time
import random
from system.lib import minescript as m

jump_timer = 0.1
jump_interval = random.uniform(10, 20   )  # Random interval between jumps (seconds)

while True:
    block = m.player_get_targeted_block(max_distance=2)
    if block:
        print(f"mine.py: Block at cursor: {block.type}")
        m.player_press_attack(True)
    else:
        print('not mining')
        m.player_press_attack(False)

    # Timed random jump
    jump_timer += 1 
    if jump_timer >= jump_interval:
        print("Jumping!")
        m.player_press_jump(True)
        time.sleep(3)
        m.player_press_jump(False)
        jump_timer = 0
        jump_interval = random.uniform(10, 20)

    time.sleep(0.1)  # Adjust sleep time as needed
