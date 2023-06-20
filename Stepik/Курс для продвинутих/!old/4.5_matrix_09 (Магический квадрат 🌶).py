n = int(input())

matrix = [list(map(int, input().split())) for __ in range(n)]
matrix = [[int(_) for _ in input().split()] for __ in range(n)]

flag_row = (len(set([sum(matrix[i]) for i in range(n)])) == 1)  # True or False

new_matrix = [[matrix[-i-1][j] for i in range(n)] for j in range(n)]
flag_col = (len(set([sum(new_matrix[i]) for i in range(n)])) == 1)  # True or False

flag_diagon = (sum([matrix[i][i] for i in range(n)]) == sum([matrix[-i-1][i] for i in range(n)]))

temp_list = []
for lists in matrix:
    temp_list.extend(lists)
temp_list.sort()

check_list = [i+1 for i in range(n)]
# flag_different_numbers = (len(set(temp_list)) == n**2)
flag_different_numbers = (check_list == temp_list)


if flag_row and flag_col and flag_diagon and flag_different_numbers:
    print('YES')
else:
    print('NO')
