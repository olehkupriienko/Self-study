# объявление функции
def print_digit_sum(num):
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10
    print(total)

# считываем данные
num = int(input())

# вызываем функцию
print_digit_sum(num)
