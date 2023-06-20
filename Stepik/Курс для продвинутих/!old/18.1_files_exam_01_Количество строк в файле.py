file_name = input()

with open(file_name, 'r') as f:
    text = f.readlines()

print(len(text))
