def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    return text[text.index(begin)+1:text.index(end)]


print(between_markers('What is >apple<', '>', '<'))
print(between_markers('What is ><', '>', '<'))
