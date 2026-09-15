grid = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
]

for row in grid:
    for value in row:
        print(value)

print("Row 1, Column 2:", grid[1][2])


numbers = [
    [5, 8, 2],
    [10, 3, 7],
    [4, 9, 6]
]

total = 0

for row in numbers:
    for number in row:
        total += number

print("Total:", total)