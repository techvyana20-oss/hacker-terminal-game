import json
import os
from config import SAVE_FILE

def load_saves():
    if os.path.exists(SAVE_FILE):
        return json.load(open(SAVE_FILE))
    return {}

def save_saves(data):
    json.dump(data, open(SAVE_FILE, "w"))

def choose_slot():
    saves = load_saves()

    for i in range(1,4):
        if str(i) in saves:
            print(f"{i}. {saves[str(i)]['name']}")
        else:
            print(f"{i}. Empty")

    return input("Choose slot: ")

def create_or_load_player(slot):
    saves = load_saves()

    if slot in saves:
        return saves[slot]

    name = input("Enter name: ")

    player = {
        "name": name,
        "level": 1,
        "score": 0,
        "inventory": [],
        "achievements": []
    }

    saves[slot] = player
    save_saves(saves)
    return player

def save_progress(slot, player):
    saves = load_saves()
    saves[slot] = player
    save_saves(saves)
