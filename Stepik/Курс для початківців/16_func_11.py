def find_all(target, symbol):
    return [i for i in range(len(target)) if target[i] == symbol]


target = input()
symbol = input()

print(find_all(target, symbol))
