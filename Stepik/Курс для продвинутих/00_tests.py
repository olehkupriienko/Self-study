data_collection_2 = [[True, False], [False, False], [True, True], 
                     [10, 100, 1000], [0, 0, 0, 0], ['Python', 'C#'], 
                     ['', '', 'language'], [(1, 2, 3), []], [], [[], []], 
                     {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday'},
                     {0: 'Monday'}, {'name': 'Timur', 'age': 28}, {'': 'None', 'age': 28}]

for i in data_collection_2:
    print(any(i))