numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"
numbers2 = []
def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])

print(high_and_low(numbers))