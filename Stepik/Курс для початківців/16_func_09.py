def get_fatcors(num):
    return [i for i in range(1, num + 1) if num % i == 0]


n = int(input())

print(get_fatcors(n))
