game = {
    "title": "Tetris",
    "year": 1985,
    "players": 1,
    "genre": "Puzzle",
    "platform": "PC"
}

for key, value in game.items():
    print(f"{key}: {value}")


character = {
    "name": "Shadow",
    "health": 100,
    "level": 5,
    "class": "Warrior"
}

for key, value in character.items():
    print(f"{key}: {value}")


character["health"] = 75

print("Updated character:")

for key, value in character.items():
    print(f"{key}: {value}")