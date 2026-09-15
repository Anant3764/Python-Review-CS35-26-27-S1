def linear_search(values, target):
    for i in range(len(values)):
        print(f"At index {i} is {values[i]}.")

        if values[i] == target:
            return i

    return -1


names = ["Alex", "Jordan", "Sam", "Taylor", "Morgan"]

target = input("Enter a name: ")

result = linear_search(names, target)

if result != -1:
    print(f"{target} found at index {result}.")
else:
    print(f"{target} was not found.")