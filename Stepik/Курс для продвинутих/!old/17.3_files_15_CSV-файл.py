with open('17.3_files_15_CSV-файл.csv', 'r') as data_file:
    data = [line.strip().split(',') for line in data_file]

keys = data.pop(0)
data_list = []
for j in range(len(data)):
    temp_dict = {}
    for i in range(len(keys)):
        temp_dict[keys[i]] = data[j][i]
    data_list.append(temp_dict)
print(data_list)


def read_csv():

    with open('17.3_files_15_CSV-файл.csv', 'r') as data_file:
        data = [line.strip().split(',') for line in data_file]


    keys = data.pop(0)
    data_list = []
    for j in range(len(data)):
        temp_dict = {}
        for i in range(len(keys)):
            temp_dict[keys[i]] = data[j][i]
        data_list.append(temp_dict)
    return data_list