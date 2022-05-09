num = int(input())
def summation(num):
    return sum(xrange(num + 1))
print(summation(num))

def summation2(num):
    return sum([i for i in range(1, num + 1)])
print(summation2(num))