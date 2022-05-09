number = 1729
count = 0
while count != 10:
    count = 0
    for i in range(1, 33):
        for j in range(1, 33):
            if i ** 3 + j ** 3 == number:
                count += 1
                if count > 3:
                    print(number)
    number += 1
print(count)
