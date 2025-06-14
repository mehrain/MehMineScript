import time
import random
from system.lib import minescript as m

def spamcrouch():
    """Spam crouch for 30 seconds."""
    # print("Spamming crouch for 30 seconds...")
    # for _ in range(30):
    m.player_press_sneak(True)
    time.sleep(0.031)
    m.player_press_sneak(False)

while True:
    spamcrouch()