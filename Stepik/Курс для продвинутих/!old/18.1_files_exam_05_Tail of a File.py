with open('18.1_files_exam_05_Tail of a File.txt', 'r') as input_file:
    text = [line.strip() for line in input_file.readlines()][-10:]

print('\n'.join(text))
