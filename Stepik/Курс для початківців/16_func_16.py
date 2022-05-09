def get_next_prime(num):
    counter = 0
    while counter != 1:
        num += 1
        counter = len([i for i in range(1, int(num ** 0.5) + 1) if num % i == 0])
        if counter == 1:
            break
    return num

n = int(input())

print(get_next_prime(n))
