# level_1.py

import tool.game_state
import level_2
import random
import time
import tool.clear as clear
import tool.typewriter as typewriter
import tool.animate_payload as animate
import tool.log as log

ATTEMPTS_ALLOWED = 8
PASSCODE_LENGTH = 5
WORD_LIST = ["NODES", "BYTES", "CODES", "TRACE",
             "DELTA", "INPUT", "HACKS", "CRACK"]

inside_agent = f"""
We've made contact with our inside agent...
Just before the firewall went live,
they grabbed a short list of code words.

NODES - BYTES - CODES - TRACE  
DELTA - INPUT - HACKS - CRACK

One of these is the real passcode. The rest are decoys.
"""


def header_display(attempts_left, clue_display):
    clear.clear_terminal()
    print("╔════════════════════════════════════╗")
    print("║    SYSTEM: AETHER NODE – LEVEL 1   ║")
    print("╚════════════════════════════════════╝")
    print()
    print(f"ATTEMPTS LEFT: {attempts_left}")
    print(f"TARGET PASSCODE LENGTH: {PASSCODE_LENGTH}")
    print("-------------------------------------------------------")
    print(inside_agent)
    print(
        f"Choose wisely, {tool.game_state.player_name}. The system is watching.")
    print("-------------------------------------------------------")
    print()
    print(f"--->> {clue_display} <<---")
    print()
    print("> ENTER BYTE: ", end="", flush=True)
    print()


def generate_clue(passcode, guess, current_clue):
    # Preserve previously revealed correct letters
    new_clue = list(current_clue.replace(" ", ""))
    for i in range(min(len(guess), len(passcode))):
        if guess[i] == passcode[i]:
            new_clue[i] = guess[i]
    return " ".join(new_clue)


def level_1():
    clear.clear_terminal()
    typewriter.typewriter("\n> Initializing breach protocol...\n")
    time.sleep(1)

    passcode = random.choice(
        [word for word in WORD_LIST if len(word) == PASSCODE_LENGTH]
    )
    clue_display = "_ " * PASSCODE_LENGTH
    clue_display = clue_display.strip()
    attempts = ATTEMPTS_ALLOWED

    while attempts > 0:
        header_display(attempts, clue_display)

        guess = input().strip().upper()

        if len(guess) != PASSCODE_LENGTH:
            print("\n[!] BYTE REJECTED: Incorrect length.")
            time.sleep(1.5)
            continue

        if guess == passcode:
            clear.clear_terminal()
            typewriter.typewriter(
                "\n[ACCESS GRANTED] – Vault breach successful.\n")
            animate.animate_payload()
            level_2.level_2()
            return True

        clue_display = generate_clue(passcode, guess, clue_display)
        attempts -= 1

    clear.clear_terminal()
    typewriter.typewriter("\n[ACCESS DENIED] – ICE has traced your signal.\n")
    time.sleep(2)
    clear.clear_terminal()
    log.log_failure(tool.game_state.player_name, 1)
    return False


# level_1()
