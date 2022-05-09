s = input()
first_part_of_s = s[:int(len(s)//2 + len(s) % 2)]
second_part_of_s = s[int(len(s)//2 + len(s) % 2):]
print(second_part_of_s + first_part_of_s)
