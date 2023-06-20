test1 = "... and so on ..."
test2 = "don't touch it"
test3 = 'Hello.World'


def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    # your code here
    text = text.replace('.', ' ')
    text = text.replace(',', ' ')
    result = [i for i in text.split()]
    return result[0].strip(',. ')


print(first_word(test1))
print(first_word(test2))
print(first_word(test3))
