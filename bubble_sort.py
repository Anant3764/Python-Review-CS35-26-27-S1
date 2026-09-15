def bubble_sort(values):
    for pass_number in range(len(values) - 1):
        for i in range(len(values) - 1 - pass_number):
            if values[i] > values[i + 1]:
                temp = values[i]
                values[i] = values[i + 1]
                values[i + 1] = temp

        print(values)


numbers = [8, 3, 6, 1, 7, 2]

print(numbers)

bubble_sort(numbers)

print(numbers)