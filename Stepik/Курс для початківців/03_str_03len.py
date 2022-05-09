word1, word2, word3 = input(), input(), input()
num1, num2, num3 = len(word1), len(word2), len(word3)

if num2 < num1 < num3:
    print(word2)
    print(word3)
elif num3 < num1 < num2:
    print(word3)
    print(word2)
elif num1 < num2 < num3:
    print(word1)
    print(word3)
elif num3 < num2 < num1:
    print(word3)
    print(word1)
elif num1 < num3 < num2:
    print(word1)
    print(word2)
else:
    print(word2)
    print(word1)