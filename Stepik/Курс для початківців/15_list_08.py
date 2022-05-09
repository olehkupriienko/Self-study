keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
            'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#lengths = [len(i) for i in keywords]   ще один варіант розв'язання
lengths = [len(keywords[i]) for i in range(len(keywords))]
print(lengths)
