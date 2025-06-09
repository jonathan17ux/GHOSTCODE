## 🧠 GHOSTCODE

> A terminal-based cyberpunk hacking game built in Python.
> Breach encrypted systems. Outsmart ICE. Extract the Omega Key.
> You only get one shot or you vanish with the data.

---

### 🔐 About

**GHOSTCODE** is a cinematic, multi-stage password cracking game that immerses you in a dystopian cyberpunk grid.
You play a ghost-runner supported by CyberMochi, your rogue AI assistant, trying to break through encrypted AETHER vaults before you're traced and deleted.

Each level increases in complexity, word length, and tension — complete with animated payload injections, system warnings, and dramatic consequences if you fail.

---

### 🎮 Gameplay Flow

* **Intro** (`intro.py`): Connect to the grid, enter your hacker ID, accept the mission.
* **Level 1** (`level_1.py`): 5-letter passcode. First breach.
* **Level 2** (`level_2.py`): 8-letter system core. ICE is aware.
* **Level 3** (`level_3.py`): 11-letter final vault protected by neural defense.
* **Endgame** (`end_congrats.py`): If you succeed, unlock the Omega Key with full cinematic finale.
* **Failure Logging**: Every trace/failure is recorded in `failure_log.txt` with timestamp and level reached.

---

### 🧩 Features

* 💻 Fully terminal-based
* 🧠 Progressive clue system that reveals correct letters
* 🕶️ Typewriter-style text rendering for cinematic effect
* 📡 Animated payload bar simulates real-time hacking
* ❌ Fails trigger ICE trace and printed game-over logs
* ✅ Modular: easy to expand with more levels or difficulty scaling

---

### ⚙️ Requirements

* **Python 3.7+**
* No external libraries — 100% standard library!

---

### 🚀 How to Run

Clone the repo and launch the game:

```
git clone https://github.com/jonathan17ux/GHOSTCODE.git
cd GHOSTCODE
python intro.py
```
---

### 📁 File Structure

```
GHOSTCODE/
│
├── intro.py             # Entry point, player ID, mission briefing
├── level_1.py           # Level 1: 5-character passcode
├── level_2.py           # Level 2: 8-character passcode
├── level_3.py           # Level 3: 11-character Omega Vault
├── end_congrats.py      # ASCII art victory screen
│
├── tool/
│   ├── animate_payload.py  # Payload loading bar
│   ├── clear.py            # Terminal clear utility
│   ├── game_state.py       # Stores player's name
│   ├── log.py              # Logs game-over messages
│   └── typewriter.py       # Typewriter-style text display
│
├── failure_log.txt      # Auto-generated log of failed breaches
└── README.md
```
---

### 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

### 🤖 Credits

* Game Design, Code & Lore: **@jonathan17ux**
* ASCII Art: Created using online generators and customized for the game
https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

---

### 🧠 Final Words

> EXECUTE THE BREACH OR BE SWALLOWED BY THE SILENCE.
