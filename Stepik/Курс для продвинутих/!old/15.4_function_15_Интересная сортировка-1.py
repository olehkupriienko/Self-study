numbers = '12 14 79 7 4 123 45 90 111'
# numbers = input()


def sorting(lst: str) -> str:
    lst = lst.split()
    lst = [i for i in lst]

    def inner_sort(num: str) -> int:
        res = 0
        for j in num:
            res += int(j)
        return res

    lst.sort(key=inner_sort)
    return ' '.join(str(i) for i in lst)


print(sorting(numbers))
