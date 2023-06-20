file_name = input()

test_file = open(file_name, 'r')
some_text = test_file.read()
test_file.close()
print(some_text)