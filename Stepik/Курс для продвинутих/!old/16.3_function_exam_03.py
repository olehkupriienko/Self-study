words = 'the world is mine take a look what you have started'.split()

# words2 =
print(*[i for i in map(lambda x: f'"{x}"', words)])