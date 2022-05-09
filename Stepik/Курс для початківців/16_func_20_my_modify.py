# объявление функции
def is_valid_password(password):
    password_elements = password.split(':')
    return (len(password_elements) == 3) and (password_elements[0] == password_elements[0][::-1]) and \
           len([i for i in range(1, int(password_elements[1])+1) if int(password_elements[1]) % i == 0]) == 2


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
