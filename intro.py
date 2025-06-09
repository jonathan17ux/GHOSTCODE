""" ᛉ Cyberpunk Password Cracker - Intro Sequence ᛉ

This script starts the game by clearing the terminal,
simulating a secure connection, and welcoming the player.
"""

import time
import level_1
import tool.clear as clear
import tool.animate_payload as animate_payload
import tool.typewriter as typewriter
import tool.game_state

mission_brief = """
-----------------------------------------------------------------------------------
MISSION BRIEF:
The grid went dark 17 minutes ago.
AETHER–Δ is exposed, vulnerable — a crack in the city’s encrypted heart.
You’ve been ghost-running black ICE for months, but this time it’s different.
No contract. No backup. Just a pulse, a trace, and a one-way connection.
-----------------------------------------------------------------------------------
Your objective: breach the vault, exfiltrate the Omega Key, and vanish.
But the deeper you go, the tighter the ICE coils.
If the system identifies your signal... it won’t just trace you. It will erase you.
-----------------------------------------------------------------------------------
You have one shot.
EXECUTE THE BREACH OR BE SWALLOWED BY THE SILENCE.
-----------------------------------------------------------------------------------
"""
banner = r"""
  ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗ ██████╗ ██████╗ ██████╗ ███████╗
 ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
 ██║  ███╗███████║██║   ██║███████╗   ██║   ██║     ██║   ██║██║  ██║█████╗  
 ██║   ██║██╔══██║██║   ██║╚════██║   ██║   ██║     ██║   ██║██║  ██║██╔══╝  
 ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ╚██████╗╚██████╔╝██████╔╝███████╗
  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
"""


def intro():
    clear.clear_terminal()
    print("Connecting to secure node...")
    time.sleep(0.5)  # ← waits 0.5 seconds
    print("> Establishing VPN route through neural uplink...")
    time.sleep(0.5)  # ← waits 0.5 secondsÍ
    print("> Spoofing node credentials...")
    time.sleep(0.5)  # ← waits 0.5 secondsÍ
    animate_payload.animate_payload()
    time.sleep(1)  # ← waits 1 seconds
    print("-> Connection established <-")

    print("")  # ← print empty line

    typewriter.typewriter(banner)

    print("")  # ← print empty line

    # user input name
    tool.game_state.player_name = input("Hacker ID name -> ").upper()

    print("")  # ← print empty line

    # welcome
    print(f"Welcome back, {tool.game_state.player_name}.")
    time.sleep(0.7)

    # display the mission
    typewriter.typewriter(mission_brief)
    print("")  # ← print empty line

    # player select if he want continue or not with the mission
    player_desicion_1 = input("Do you accept the mission? (Y/N) -> ").upper()

    if player_desicion_1 == "Y" or player_desicion_1 == "YES":
        level_1.level_1()
    else:
        print("-> Connection Down <-")
        time.sleep(1)  # ← waits 1 seconds
        clear.clear_terminal()


intro()
