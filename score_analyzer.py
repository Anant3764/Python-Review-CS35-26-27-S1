def calculate_average(scores):
    total = 0

    for score in scores:
        total += score

    return total / len(scores)


def linear_search(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i

    return -1


def bubble_sort(values):
    for pass_number in range(len(values) - 1):
        for i in range(len(values) - 1 - pass_number):
            if values[i] > values[i + 1]:
                temp = values[i]
                values[i] = values[i + 1]
                values[i + 1] = temp


scores = [72, 91, 64, 85, 78, 95, 68, 88]

print("Scores:", scores)

average = calculate_average(scores)
print("Average:", average)

target = int(input("Enter a score to search for: "))

result = linear_search(scores, target)

if result != -1:
    print(f"{target} was found at index {result}.")
else:
    print(f"{target} was not found.")

bubble_sort(scores)

print("Sorted Scores:", scores)