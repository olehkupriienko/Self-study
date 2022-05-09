s = input()
first_index = s.index('h')
last_index = s.rindex('h')

first_part = s[:first_index+1]
last_part = s[last_index:]
midl_part = s[first_index+1:last_index]
mid2_part = ''

for i in range(1, len(midl_part)+1):
    mid2_part = mid2_part + midl_part[-i]

new = first_part + mid2_part + last_part
print(new)
