numbers = [1, 2, 3]


def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0


print(find_average(numbers))
