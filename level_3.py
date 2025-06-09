# level_3.py

import tool.game_state
import end_congrats
import random
import time
import tool.clear as clear
import tool.typewriter as typewriter
import tool.animate_payload as animate
import tool.log as log

ATTEMPTS_ALLOWED = 4
PASSCODE_LENGTH = 11
WORD_LIST = [
    "OVERCLOCKED",
    "BLACKHOLEFX",
    "DATACASCADE",
    "MINDJACKERX",
    "NULLSEEKERS",
    "GLITCHWRAITH",
    "CORESHATTER",
    "CRYPTOVIRUS"
]

inside_agent = f"""[ ☠ ] FINAL TRANSMISSION — ECHO FRACTURED

The vault is sealed behind the Omega Lock.
ICE is evolving. Trace filters are failing.

CyberMochi breached the neural firewall just long enough
to inject a set of potential override vectors:

OVERCLOCKED, BLACKHOLEFX, DATACASCADE, MINDJACKERX, 
NULLSEEKERS, GLITCHWRAITH, CORESHATTER, CRYPTOVIRUS

Only one bypasses the core without triggering a meltdown.

The others? Viral decoys hardwired to shred your trace.

>> ONE SHOT. ONE PASSCODE. NO RESCUE. <<"""


def header_display(attempts_left, clue_display):
    clear.clear_terminal()
    print("╔═══════════════════════════════════════════════╗")
    print("║                                               ║")
    print("║     ☠ FINAL BREACH: OMEGA VAULT – LEVEL 3     ║")
    print("║                                               ║")
    print("╠═══════════════════════════════════════════════╣")
    print("║  SECURITY STATUS: [■■■■■□] MAXIMUM            ║")
    print("║  NEURAL NET DEFENSE: ACTIVE                   ║")
    print("╚═══════════════════════════════════════════════╝")
    print()
    print(f"ATTEMPTS LEFT: {attempts_left}")
    print(f"TARGET PASSCODE LENGTH: {PASSCODE_LENGTH}")
    print("-------------------------------------------------------")
    print(inside_agent)
    print(
        f"This is it, {tool.game_state.player_name} — the Omega Lock won’t open twice."
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


def level_3():
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
                "\n[ACCESS GRANTED] – Core breach successful. The Omega Key is in your hands. Get out before it implodes...\n"
            )
            animate.animate_payload()
            end_congrats.end_congrats(tool.game_state.player_name)
            return True

        clue_display = generate_clue(passcode, guess, clue_display)
        attempts -= 1

    clear.clear_terminal()
    typewriter.typewriter(
        "\n[ACCESS DENIED] – Vault defense triggered. Your digital footprint has been erased.\n"
    )
    time.sleep(2)
    clear.clear_terminal()
    log.log_failure(tool.game_state.player_name, 3)
    return False


# level_3()
