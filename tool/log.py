# tool/log.py
import os
from datetime import datetime


def log_failure(player_name, level):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = (
        "\n"
        f"        ✖ GAME OVER – TRACE COMPLETE ✖       \n"
        f"═════════════════════════════════════════════\n"
        f"   PLAYER: {player_name}                     \n"
        f"   LEVEL FAILED: {level}                     \n"
        f"   TIME OF DEFEAT: {timestamp}               \n"
        f"   STATUS: Signal isolated. Access purged.   \n"
        f"═════════════════════════════════════════════\n"
    )

    print(message)
    exit_game()
    with open("failure_log.txt", "a") as file:
        file.write(message + "\n")


def exit_game():
    print("\nPress ENTER to exit...")
    input()
    if input == "":
        clear_terminal()
    else:
        clear_terminal()


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# log_failure("ARIONOX", "3")
