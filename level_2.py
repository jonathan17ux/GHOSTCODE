# level_2.py

import tool.game_state
import level_3
import random
import time
import tool.clear as clear
import tool.typewriter as typewriter
import tool.animate_payload as animate
import tool.log as log


ATTEMPTS_ALLOWED = 6
PASSCODE_LENGTH = 8
WORD_LIST = [
    "PROTOCOL",
    "DOWNLOAD",
    "FIREWALL",
    "OVERRIDE",
    "TERMINAL",
    "BACKDOOR",
    "PAYLOADER",
    "CRYPTKEYS"
]

inside_agent = f"""[ ! ] URGENT RELAY FROM INSIDE AGENT [ ! ] 

We’re losing the signal—ICE is crawling the grid for your trace!

Just before the sweeper drones locked us out,
I injected a final payload into the system:
a shortlist of candidate passphrases.

PROTOCOL, DOWNLOAD, FIREWALL, OVERRIDE,
TERMINAL, BACKDOOR, PAYLOADER, CRYPTKEYS 

Only ONE of them is real — the vault passcode.
The rest are tripwires. Choose wrong, and they’ll lock us in.

CyberMochi’s running a brute-accel routine to give you a narrow window.
But if they find your signal before you break the code…

…it’s not exile. It’s deletion.

>> MOVE FAST. CRACK THE CORE. NO SECOND CHANCES. <<"""


def header_display(attempts_left, clue_display):
    clear.clear_terminal()
    print("╔════════════════════════════════════════════════╗")
    print("║                                                ║")
    print("║     ⚠ SYSTEM BREACH: AETHER NODE – LEVEL 2     ║")
    print("║                                                ║")
    print("╠════════════════════════════════════════════════╣")
    print("║    FIREWALL INTENSITY: [■■■□□□□] Escalating    ║")
    print("╚════════════════════════════════════════════════╝")
    print()
    print(f"ATTEMPTS LEFT: {attempts_left}")
    print(f"TARGET PASSCODE LENGTH: {PASSCODE_LENGTH}")
    print("-------------------------------------------------------")
    print(inside_agent)
    print(
        f"Choose wisely, {tool.game_state.player_name}. The hunters are getting closer."
    )
    print("-------------------------------------------------------")
    print()
    print(f"--->> {clue_display} <<---")
    print()
    print("> ENTER BYTE: ", end="", flush=True)
    print()


def generate_clue(passcode, guess, current_clue):
    # Remove spaces to work with individual characters
    new_clue = list(current_clue.replace(" ", ""))
    for i in range(min(len(guess), len(passcode))):
        if guess[i] == passcode[i]:
            new_clue[i] = guess[i]
    return " ".join(new_clue)


def level_2():
    clear.clear_terminal()
    typewriter.typewriter("\n> Initializing breach protocol...\n")
    time.sleep(1)

    passcode = random.choice(
        [word for word in WORD_LIST if len(word) == PASSCODE_LENGTH]
    )
    clue_display = "_ " * PASSCODE_LENGTH
    clue_display = clue_display.strip()  # remove trailing space
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
                "\n[ACCESS GRANTED] – Level 2 firewall neutralized. Proceed before the trace completes...\n"
            )
            animate.animate_payload()
            level_3.level_3()
            return True

        clue_display = generate_clue(passcode, guess, clue_display)
        attempts -= 1

    clear.clear_terminal()
    typewriter.typewriter("\n[ACCESS DENIED] – ICE has traced your signal.\n")
    time.sleep(2)
    clear.clear_terminal()
    log.log_failure(tool.game_state.player_name, 2)
    return False


# level_2()
