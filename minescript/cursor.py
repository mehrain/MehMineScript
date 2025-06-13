import time
from system.lib import minescript as m

while True:
    block = m.player_get_targeted_block()
    if block:
        print(f"Block at cursor: {block.type} at {block.position}")
    else:
        print("No block at cursor.")
        
    
    time.sleep(1)