# объявление функции
def print_digit_sum(num):
    print(sum(int(i) for i in str(num)))

# считываем данные
num = int(input())

# вызываем функцию
print_digit_sum(num)
