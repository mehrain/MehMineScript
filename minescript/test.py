# Basic MineScript: Make the player run in circles
import time
from system.lib import minescript

# Helper to set orientation (yaw in degrees)
def set_yaw(yaw):
    # Keep pitch at 0 (horizontal)
    minescript.player_set_orientation(yaw, 0)
    time.sleep(0.05)

# Start moving forward
def start_forward():
    minescript.player_press_forward(True)

def stop_forward():
    minescript.player_press_forward(False)

# Main loop: run in a circle
def run_in_circle(duration=10, speed=90):
    '''
    duration: seconds to run
    speed: degrees per second to turn
    '''
    start_forward()
    yaw = 0
    t0 = time.time()
    while time.time() - t0 < duration:
        set_yaw(yaw)
        yaw = (yaw + speed * 0.05) % 360
        time.sleep(0.05)
    stop_forward()

if __name__ == "__main__":
    run_in_circle(duration=10, speed=90)
