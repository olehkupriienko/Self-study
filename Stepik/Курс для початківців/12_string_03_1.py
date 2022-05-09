s = input()
ss = s.lower()
cont = 0
for i in range(len(s)):
    if s[i] == ss[i] and "a" <= s[i] <= "z":
        cont += 1
print(cont)
