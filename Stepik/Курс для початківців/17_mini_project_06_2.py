eng_alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng_alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
input_phrase = input().split()
result = []

for i in input_phrase:
    count = 0
    for k in range(len(i)):
        if i[k] in eng_alphabet_lower or i[k] in eng_alphabet_upper :
            count += 1
    output_phrase = ''
    for j in range(len(i)):
        if i[j] in eng_alphabet_upper:
            if 0 <= eng_alphabet_upper.index(i[j]) + count <= 25:
                output_phrase += eng_alphabet_upper[eng_alphabet_upper.index(i[j]) + count]
            else:
                output_phrase += eng_alphabet_upper[eng_alphabet_upper.index(i[j]) + count - 26]
        if i[j] in eng_alphabet_lower:
            if 0 <= eng_alphabet_lower.index(i[j]) + count <= 25:
                output_phrase += eng_alphabet_lower[eng_alphabet_lower.index(i[j]) + count]
            else:
                output_phrase += eng_alphabet_lower[eng_alphabet_lower.index(i[j]) + count - 26]
        if i[j] not in eng_alphabet_upper and i[j] not in eng_alphabet_lower:
                output_phrase += i[j]
    result.append(output_phrase)

print(*result)