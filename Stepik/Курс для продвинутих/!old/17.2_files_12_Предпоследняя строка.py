filename = input()

test_file = open(filename, 'r')
some_text = test_file.readlines()[-2]
test_file.close()
print(some_text)