from math import factorial

n = int(input())
print([int(factorial(n) / (factorial(j) * factorial(n - j))) for j in range(n+1)])

# n = 4
# my_list = []
# for i in range(n):
#     temp_list = []
#     for j in range(i+1):
#         num = (factorial(i) / (factorial(j) * factorial(i - j)))
#         temp_list.append(int(num))
#     my_list.append(temp_list)
