words = input().split()

new_words = sorted(words, key=lambda x: x.lower())

print(*sorted(input().split(), key=lambda x: x.lower()))
