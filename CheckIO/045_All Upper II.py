def is_all_upper(text: str) -> bool:
    while text:
        upper = ''
        for char in text:
            if char.isalpha():
                upper += char
        else:
            if upper.isupper():
                return True
            else:
                return False
    else:
        return False


if __name__ == "__main__":

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper("ALL UPPER") is True
    assert is_all_upper("all lower") is False
    assert is_all_upper("mixed UPPER and lower") is False
    assert is_all_upper("") is False
    print("Coding complete? Click 'Check' to earn cool rewards!")