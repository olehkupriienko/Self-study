s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
ss = [i for i in s.split()]
# result = {}
# for item in ss:
#     key, value = item.split(':')
#     result[key] = value
# print(result)


result = {key: value for key, value in (i.split(':') for i in s.split())}
print(result)
