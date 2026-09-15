def square(number):
    return number * number


number = float(input("Enter a number: "))
result = square(number)

print(result)


def larger_number(a, b):
    if a > b:
        return a
    else:
        return b


result = larger_number(12, 7)
print(result)

result = larger_number(5, 15)
print(result)

result = larger_number(20, 18)
print(result)