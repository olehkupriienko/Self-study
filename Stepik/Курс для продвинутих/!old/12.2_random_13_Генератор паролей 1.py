from random import sample

numbers_of_passwords = int(input())
numbers_of_symbols_in_password = int(input())


def generate_password(length):

    all_symbols = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789'
    password = sample(all_symbols, length)
    return ''.join(i for i in password)


def generate_passwords(count, length):
    result = [generate_password(length) for _ in range(count)]
    return result


print(*generate_passwords(numbers_of_passwords, numbers_of_symbols_in_password), sep='\n')
