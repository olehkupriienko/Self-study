def is_acceptable_password(line: str):
    length = len(line)
    at_least_three_different_character = len(set(i for i in line)) >= 3
    at_least_one_digit = any(i.isdigit() for i in line)
    only_digit = all(i.isdigit() for i in line)
    password_in = 'password' in line.lower()
    return ((6 <= length <= 9 and at_least_one_digit and not only_digit)
            or length > 9) \
            and not password_in and at_least_three_different_character


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    assert is_acceptable_password("password12345") == False
    assert is_acceptable_password("PASSWORD12345") == False
    assert is_acceptable_password("pass1234word") == True
    assert is_acceptable_password("aaaaaa1") == False
    assert is_acceptable_password("aaaaaabbbbb") == False
    assert is_acceptable_password("aaaaaabb1") == True
    assert is_acceptable_password("abc1") == False
    assert is_acceptable_password("abbcc12") == True
    print("Coding complete!")
