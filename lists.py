games = ["Minecraft", "Portal", "Tetris"]

games.append("Celeste")
games.append("Fortnite")

games[1] = "GTA 5"

for game in games:
    print(game)

print("Total games:", len(games))


numbers = [5, 8, 2, 10, 4]

total = 0

for number in numbers:
    total += number

print("Total:", total)