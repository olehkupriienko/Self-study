with open('18.1_files_exam_04_Самое длинное слово в файле.txt', 'r') as input_file:
    text = input_file.read()

word_list = text.split()
longest_words = [word for word in word_list if len(word) == max(len(word) for word in word_list)]
print(*longest_words, sep='\n')
