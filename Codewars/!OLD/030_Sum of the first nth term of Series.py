def series_sum(n):
    total = 0
    znamenuk = 1
    for i in range(n):
        total += 1 / znamenuk
        znamenuk += 3
    return format(total, ".2f")


print(series_sum(int(input())))