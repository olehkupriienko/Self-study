n = int(input())
ip_adressess = [input() for _ in range(n)]


def ip_sort(line: str):
    x = line.split('.')
    total = 0
    for i in range(4):
        total += int(x[i])*256**(3-i)
    return total


print(*sorted(ip_adressess, key=ip_sort), sep='\n')
