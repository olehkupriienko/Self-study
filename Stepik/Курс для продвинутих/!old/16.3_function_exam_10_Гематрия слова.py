from functools import reduce


def gemat(line: str):
    return reduce(lambda a, x: a + (ord(x)-ord('A')), sorted(line.upper()), 0), line


words = [input() for _ in range(int(input()))]

# sorted_words = sorted(words, key=lambda x: (gemat(x), x))
sorted_words = sorted(words, key=gemat)

print(*sorted_words, sep='\n')
