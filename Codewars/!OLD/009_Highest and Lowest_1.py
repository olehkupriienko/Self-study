numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"
numbers2 = []
def high_and_low(numbers):
    numbers = str(max([int(x) for x in numbers.split(" ")])) + " " + str(min([int(x) for x in numbers.split(" ")]))
    return numbers

print(high_and_low(numbers))