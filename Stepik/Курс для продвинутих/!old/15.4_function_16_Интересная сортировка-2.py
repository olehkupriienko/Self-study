test = '111 14 79 7 4 123 90 45 12 171'
# numbers = input()


def sorting(numbers):
    numbers = numbers.split()
    numbers = [int(i) for i in numbers]
    numbers.sort()
    def comparator(num):
        res = 0
        for i in str(num):
            res += int(i)
        return res

    numbers.sort(key=comparator)
    return ' '.join(str(i) for i in numbers)


print(sorting(test))
