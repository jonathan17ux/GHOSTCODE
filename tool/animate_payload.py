import time
import sys


def animate_payload():
    for percent in range(0, 101, 5):  # from 0 to 100 in steps of 5
        bar = "█" * (percent // 5) + "░" * ((100 - percent) // 5)
        sys.stdout.write(f"\r> Injecting payload... {bar} {percent}%")
        sys.stdout.flush()
        time.sleep(0.4)  # speed of animation

    print("\n> Payload successfully injected.")
