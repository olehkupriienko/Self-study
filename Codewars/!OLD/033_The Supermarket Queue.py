customers = [2,2,3,3,4,4]
n = 2


def queue_time(customers, n):
    result = [0 for i in range(n)]
    for i in customers:
        result[result.index(min(result))] += i
    return max(result)


print(queue_time(customers, n))
