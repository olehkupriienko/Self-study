test = 'moOse'


def is_isogram(string):
    # temp1 = set((i for i in string.lower() if i.isalfa()))
    return len(string) == len(set((i for i in string.lower() if i.isalpha())))


print(is_isogram(test))
