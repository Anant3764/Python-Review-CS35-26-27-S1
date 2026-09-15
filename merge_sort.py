def merge_sort(values):
    if len(values) <= 1:
        return values

    middle = len(values) // 2

    left = values[:middle]
    right = values[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    print(f"Merging {left} and {right}")

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


numbers = [12, 4, 9, 2, 15, 7, 1, 10]

print("Original:", numbers)

numbers = merge_sort(numbers)

print("Sorted:", numbers)