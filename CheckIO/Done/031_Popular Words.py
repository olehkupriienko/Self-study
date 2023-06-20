some_text = '''
When I was One
I had just begun
When I was Two
I was nearly new
'''
some_words = ['i', 'was', 'three', 'near']


def popular_words(text: str, words: list) -> dict:
    # your code here

    # string = text.replace('\n', ' ')
    # string_list = [i.lower() for i in string.split()]
    # result = {word: string_list.count(word) for word in words}

    lower_count = text.lower().split().count
    result = {word: lower_count(word) for word in words}

    return result


print(popular_words(some_text, some_words))
