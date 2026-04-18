import random
from core.commands import command_mode
from data.targets import targets

def generate_password(level):
    return ''.join(str(random.randint(0,9)) for _ in range(min(4+level, 8)))

def play_level(player, level):
    target = targets[(level-1) % len(targets)]

    password = generate_password(level)
    player["current_password"] = password

    print(f"\nMISSION {level}")
    print("Target:", target["name"])
    print(target["desc"])

    return command_mode(player, level)
