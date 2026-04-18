from data.achievements_data import ACHIEVEMENTS

def check_achievements(player):

    if player["level"] >= 2 and "first" not in player["achievements"]:
        player["achievements"].append("first")
        player["inventory"].append("Scanner")
        print("🏆", ACHIEVEMENTS["first"])

    if player["level"] >= 5 and "pro" not in player["achievements"]:
        player["achievements"].append("pro")
        player["inventory"].append("Injector")
        print("🏆", ACHIEVEMENTS["pro"])
