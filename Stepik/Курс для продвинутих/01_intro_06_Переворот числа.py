number = input()
print(int((number[:-5] + number[::-1][:5])))
