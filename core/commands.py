import random

def command_mode(player, level):
    connected = False
    injected = False

    while True:
        cmd = input("hacker@system:~$ ").lower()

        if cmd == "scan":
            print("IP:", random.randint(100,255))

        elif cmd == "connect":
            connected = True
            print("Connected")

        elif cmd == "inject":
            if connected:
                injected = True
                print("Injected")
            else:
                print("Connect first")

        elif cmd == "decrypt":
            if injected:
                guess = input("Password: ")
                if guess == player["current_password"]:
                    print("ACCESS GRANTED")
                    return True
                else:
                    print("Wrong")
            else:
                print("Inject first")

        elif cmd == "inventory":
            print(player["inventory"])

        elif cmd == "help":
            print("scan connect inject decrypt inventory exit")

        elif cmd == "exit":
            return False

        else:
            print("Unknown command")
