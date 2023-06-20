n = int(input())

city = {input() for i in range(n)}

if input() in city:
    print('REPEAT')
else:
    print('OK')