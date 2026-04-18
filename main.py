import os, json, random, time

SAVE_FILE = "saves.json"

# ---------------- EFFECT ----------------
def slow(text):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(0.01)
    print()

# ---------------- SAVE ----------------
def load():
    if os.path.exists(SAVE_FILE):
        return json.load(open(SAVE_FILE))
    return {}

def save(data):
    json.dump(data, open(SAVE_FILE, "w"))

def choose_slot():
    saves = load()
    print("\nSlots:")
    for i in range(1,4):
        if str(i) in saves:
            print(f"{i}. {saves[str(i)]['name']}")
        else:
            print(f"{i}. Empty")
    return input("Choose slot: ")

def create_player(slot):
    saves = load()
    if slot in saves:
        return saves[slot]

    name = input("Enter hacker name: ")
    player = {
        "name": name,
        "level": 1,
        "score": 0,
        "inventory": [],
        "achievements": []
    }
    saves[slot] = player
    save(saves)
    return player

def save_player(slot, player):
    saves = load()
    saves[slot] = player
    save(saves)

# ---------------- STORY ----------------
def story(level):
    if level == 1:
        slow("""
[WELCOME]

"You are selected."
Follow or go rogue?
""")

# ---------------- GAME ----------------
def gen_pass(level):
    return ''.join(str(random.randint(0,9)) for _ in range(min(4+level, 8)))

def tutorial():
    print("""
🎯 HOW TO PLAY:

scan     → find target
connect  → connect system
inject   → inject payload
decrypt  → crack password

Follow this order!
""")

def command_mode(player, password):
    connected = False
    injected = False

    tutorial()

    print(f"🔐 Password length: {len(password)} digits")

    while True:
        cmd = input("\nhacker@system:~$ ").lower().strip()

        if cmd == "help":
            tutorial()

        elif cmd == "scan":
            print("Target IP: 192.168.0." + str(random.randint(2,254)))

        elif cmd == "connect":
            connected = True
            print("✔ Connected to system")

        elif cmd == "inject":
            if not connected:
                print("❌ Connect first")
            else:
                injected = True
                print("💉 Payload injected")

        elif cmd == "decrypt":
            if not injected:
                print("❌ Inject first")
            else:
                guess = input("Enter password: ")

                if guess == password:
                    print("✅ ACCESS GRANTED")
                    return True
                else:
                    print("❌ Wrong password")
                    print(f"💡 Hint: Starts with {password[0]}")

        elif cmd == "inventory":
            print("🎒", player["inventory"])

        elif cmd == "exit":
            return False

        else:
            print("⚠ Invalid command. Type 'help'")

# ---------------- LEVEL ----------------
def play_level(player, level):
    password = gen_pass(level)

    print(f"\n🚀 MISSION {level}")
    print("Target: Local Server")

    return command_mode(player, password)

# ---------------- BOSS ----------------
def boss(level):
    print("\n💀 BOSS LEVEL")
    password = ''.join(str(random.randint(0,9)) for _ in range(6))

    print(f"🔐 Password length: {len(password)}")

    for _ in range(3):
        guess = input("Boss password: ")
        if guess == password:
            print("🔥 BOSS DEFEATED")
            return True
        else:
            print("❌ Wrong")

    return False

# ---------------- ACHIEVEMENTS ----------------
def achievements(player):
    if player["level"] >= 2 and "first" not in player["achievements"]:
        player["achievements"].append("first")
        player["inventory"].append("Scanner")
        print("🏆 First Hack Unlocked + Scanner")

    if player["level"] >= 5 and "pro" not in player["achievements"]:
        player["achievements"].append("pro")
        player["inventory"].append("Injector")
        print("🏆 Pro Hacker + Injector")

# ---------------- MAIN ----------------
def main():
    slot = choose_slot()
    player = create_player(slot)

    print(f"\n😈 Welcome Hacker {player['name']}")

    level = player["level"]
    score = player["score"]

    while True:
        story(level)

        if level % 5 == 0:
            success = boss(level)
        else:
            success = play_level(player, level)

        if success:
            level += 1
            score += 10

            player["level"] = level
            player["score"] = score

            achievements(player)
            save_player(slot, player)

        else:
            print("\n💀 GAME OVER")
            break

if __name__ == "__main__":
    main()
