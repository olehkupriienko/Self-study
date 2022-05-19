word = input() + ' запретил букву'

letter = 1072
while len(word) != 0:
    if chr(letter) in word:
        print(word + " " + chr(letter))
        word = word.replace(chr(letter), '').replace('  ', ' ').strip()
    letter += 1