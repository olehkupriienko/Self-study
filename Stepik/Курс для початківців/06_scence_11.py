n = int(input())
word = ''
num1 = 0
num2 = 1

for i in range(0, n):
    num1, num2 = num2, num2 + num1
    word = word + ' ' + str(num1)
print(word)
