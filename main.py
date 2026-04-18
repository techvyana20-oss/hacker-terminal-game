import os, json, random, time
from colorama import Fore, Style, init

init(autoreset=True)

SAVE_FILE = "saves.json"

# ---------------- EFFECTS ----------------
def type_text(text, delay=0.02, color=Fore.GREEN):
    for c in text:
        print(color + c, end="", flush=True)
        time.sleep(delay)
    print()

def matrix_effect():
    print(Fore.GREEN)
    for _ in range(10):
        print("".join(str(random.randint(0,1)) for _ in range(60)))
        time.sleep(0.05)
    print(Style.RESET_ALL)

def banner():
    print(Fore.GREEN + """
███████╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████╗███████║██║     █████╔╝ █████╗  ██████╔╝
╚════██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
███████║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    """)

# ---------------- SAVE ----------------
def load():
    if os.path.exists(SAVE_FILE):
        return json.load(open(SAVE_FILE))
    return {}

def save(data):
    json.dump(data, open(SAVE_FILE, "w"))

def choose_slot():
    saves = load()
    print(Fore.YELLOW + "\n[SELECT SLOT]")
    for i in range(1,4):
        if str(i) in saves:
            print(f"{i}. {saves[str(i)]['name']}")
        else:
            print(f"{i}. Empty")
    return input("> ")

def create_player(slot):
    saves = load()
    if slot in saves:
        return saves[slot]

    name = input("Enter hacker name: ")
    player = {"name": name, "level": 1, "score": 0, "inventory": [], "achievements": []}
    saves[slot] = player
    save(saves)
    return player

def save_player(slot, player):
    saves = load()
    saves[slot] = player
    save(saves)

# ---------------- GAME ----------------
def tutorial():
    print(Fore.CYAN + """
[GUIDE]
scan → connect → inject → decrypt
""")

def gen_pass(level):
    return ''.join(str(random.randint(0,9)) for _ in range(min(4+level, 8)))

def command_mode(player, password):
    connected = False
    injected = False

    tutorial()
    print(Fore.YELLOW + f"Password length: {len(password)}")

    while True:
        cmd = input(Fore.GREEN + "\nhacker@system:~$ ").lower()

        if cmd == "scan":
            print(Fore.GREEN + f"IP: 192.168.0.{random.randint(2,254)}")

        elif cmd == "connect":
            connected = True
            print(Fore.GREEN + "Connected ✔")

        elif cmd == "inject":
            if not connected:
                print(Fore.RED + "Connect first")
            else:
                injected = True
                print(Fore.GREEN + "Payload injected 💉")

        elif cmd == "decrypt":
            if not injected:
                print(Fore.RED + "Inject first")
            else:
                guess = input("Password: ")
                if guess == password:
                    print(Fore.GREEN + "ACCESS GRANTED 🔓")
                    return True
                else:
                    print(Fore.RED + "Wrong ❌")
                    print(Fore.YELLOW + f"Hint: Starts with {password[0]}")

        elif cmd == "inventory":
            print(Fore.CYAN + str(player["inventory"]))

        elif cmd == "help":
            tutorial()

        elif cmd == "exit":
            return False

        else:
            print(Fore.RED + "Invalid command")

# ---------------- LEVEL ----------------
def play_level(player, level):
    password = gen_pass(level)

    print(Fore.YELLOW + f"\n🚀 MISSION {level}")
    matrix_effect()
    type_text("Connecting...")
    type_text("Bypassing firewall...")
    type_text("Injecting shell...")

    return command_mode(player, password)

# ---------------- BOSS ----------------
def boss(level):
    print(Fore.RED + "\n💀 BOSS SYSTEM")
    matrix_effect()

    password = ''.join(str(random.randint(0,9)) for _ in range(6))
    print(Fore.YELLOW + f"Password length: {len(password)}")

    for _ in range(3):
        guess = input("Boss Password: ")
        if guess == password:
            print(Fore.GREEN + "🔥 BOSS DEFEATED")
            return True
        else:
            print(Fore.RED + "Wrong ❌")

    return False

# ---------------- MAIN ----------------
def main():
    banner()
    slot = choose_slot()
    player = create_player(slot)

    type_text(f"Welcome Hacker {player['name']} 😈")

    level = player["level"]

    while True:
        if level % 5 == 0:
            success = boss(level)
        else:
            success = play_level(player, level)

        if success:
            level += 1
            player["level"] = level
            save_player(slot, player)
        else:
            print(Fore.RED + "\n💀 GAME OVER")
            break

if __name__ == "__main__":
    main()
