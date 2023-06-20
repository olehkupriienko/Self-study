import random
length = int(input())    # длина пароля

password = ''
for i in range(length):
    password += random.choice([chr(random.randint(65, 90)), chr(random.randint(97, 122))])

password2 = ''.join(random.choice([chr(random.randint(65, 90)), chr(random.randint(97, 122))]) for _ in range(length))
print(password)
print(password2)