test1 = ['What is >apple<', '>', '<']
test2 = ['No[/b] hi', '[b]', '[/b]']
test3 = ["<head><title>My new site</title></head>", "<title>", "</title>"]


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    if begin in text:
        start_index = text.index(begin) + len(begin)
    else:
        start_index = 0

    if end in text:
        finish_index = text.index(end)
    else:
        finish_index = len(text) + 1

    return text[start_index:finish_index]
    # return text[text.index(begin) + len(begin) if begin in text else 0:text.index(end) if end in text else len(text) + 1]


print(between_markers(*test1))
print(between_markers(*test2))
print(between_markers(*test3))
