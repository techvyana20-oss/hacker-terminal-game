from systems.save_system import choose_slot, create_or_load_player, save_progress
from systems.achievements import check_achievements
from systems.cloud import cloud_save
from core.game import play_level
from core.boss import boss_fight
from core.story import show_story

def start_game():
    slot = choose_slot()
    player = create_or_load_player(slot)

    print(f"\nWelcome Hacker {player['name']} 😈")

    level = player["level"]
    score = player["score"]

    while True:
        show_story(level, player)

        if level % 5 == 0:
            success = boss_fight(player, level)
        else:
            success = play_level(player, level)

        if success:
            level += 1
            score += 10

            player["level"] = level
            player["score"] = score

            check_achievements(player)

            save_progress(slot, player)
            cloud_save()

        else:
            print("💀 GAME OVER")
            break
