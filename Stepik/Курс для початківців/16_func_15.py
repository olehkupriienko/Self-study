def is_prime(num):
    counter = len([i for i in range(1, int(num ** 0.5) + 1) if num % i == 0])
    if counter == 1:
        return True
    else:
        return False


n = int(input())

print(is_prime(n))
