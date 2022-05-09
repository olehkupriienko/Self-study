def is_password_good(password):
    if len(password) >= 8:
        if password.isdigit() == False and  password.isalpha() == False and password.isalnum() == True:
            if password.islower() == False and password.isupper() == False and password.isdigit() == False:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))