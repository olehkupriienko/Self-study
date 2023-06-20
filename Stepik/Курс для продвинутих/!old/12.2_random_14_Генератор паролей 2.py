from random import sample, randint, shuffle

# numbers_of_passwords = int(input())
# numbers_of_symbols_in_password = int(input())

numbers_of_passwords = 2
numbers_of_symbols_in_password = 6


def generate_password(length):
    letters_lower = 'abcdefghjkmnpqrstuvwxyz'
    letters_upper = 'ABCDEFGHJKMNPQRSTUVWXYZ'
    digits = '23456789'
    all_symbols = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789'
    password = [letters_upper[randint(0, len(letters_upper) - 1)], letters_lower[randint(0, len(letters_lower) - 1)],
                digits[randint(0, len(digits) - 1)]]
    password.extend(sample(all_symbols, length-3))
    shuffle(password)
    return ''.join(i for i in password)


def generate_passwords(count, length):
    result = [generate_password(length) for _ in range(count)]
    return result


print(*generate_passwords(numbers_of_passwords, numbers_of_symbols_in_password), sep='\n')
