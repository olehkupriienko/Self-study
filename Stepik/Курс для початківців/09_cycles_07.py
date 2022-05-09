for b in range (1, int(100/10)+1):
    for k in range (1, int(100/5)+1):
        for t in range(1, int(100/0.5)+1):
            if (10*b + 5*k + 0.5*t) == 100 and (b + k + t) == 100:
                print(b, k, t)