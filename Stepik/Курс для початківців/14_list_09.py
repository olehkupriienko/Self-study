words = ['Мы', 'учим', 'язык', 'Python']
new_words = '*'.join(words)

print(new_words)

new2_words = new_words.split('*')
print(*new2_words, sep='\n')
