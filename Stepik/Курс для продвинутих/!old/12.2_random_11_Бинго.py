from random import sample
all_bingo_numbers = range(1, 76)

selected_bingo_numbers = sample(all_bingo_numbers, 25)
selected_bingo_numbers[12] = 0

k = 0
for i in range(5):
    for j in range(5):
        print(str(selected_bingo_numbers[k]).ljust(3), end='')
        k += 1
    print()