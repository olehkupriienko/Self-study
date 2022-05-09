num = int(input())
dig1 = num // 100
dig2 = num % 100 // 10
dig3 = num // 10
mx = max(dig1, dig2, dig3)
mn = min(dig1, dig2, dig3)
sr = dig1 + dig2 + dig3 - mx - mn
if (mx - mn) == sr:
    print('Число интересное')
else:
    print('Число неинтересное')