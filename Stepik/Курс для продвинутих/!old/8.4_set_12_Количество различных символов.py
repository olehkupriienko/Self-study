fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}

print(*[i for i in sorted(fruits, reverse=True)], sep='\n')
