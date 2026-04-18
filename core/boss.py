import random

def boss_fight(player, level):
    print("\n💀 BOSS LEVEL")

    password = ''.join(str(random.randint(0,9)) for _ in range(6))

    for _ in range(3):
        if input("Boss password: ") == password:
            print("BOSS DEFEATED")
            return True
        print("Wrong")

    return False
