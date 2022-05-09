def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    return text[0].upper() + text[1:] + ('' if text.endswith('.') else '.')



print(correct_sentence("welcome to New York."))
