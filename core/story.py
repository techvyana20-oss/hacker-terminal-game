from utils.effects import slow_text

def show_story(level, player):

    if level == 1:
        slow_text("""
[WELCOME]

"You are selected."
Follow or go rogue?
""")

        c = input("1. Follow\n2. Rogue\n> ")
        player["path"] = "loyal" if c == "1" else "rogue"

    elif level == 3:
        if player.get("path") == "rogue":
            slow_text("You break rules...")
        else:
            slow_text("Stay in control...")

    elif level == 5:
        slow_text("⚠ AI SYSTEM ACTIVE")
