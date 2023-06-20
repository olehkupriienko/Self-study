def is_acceptable_password(line: str):
    return len(line) >= 6 and not all(i.isdigit() for i in line) \
           and any(i.isdigit() for i in line) and any(i.isalpha() for i in line)



print(is_acceptable_password('short') is False)
print(is_acceptable_password('muchlonger') is False)
print(is_acceptable_password('ashort') is False)
print(is_acceptable_password('muchlonger5') is True)
print(is_acceptable_password('sh5') is False)
print(is_acceptable_password('1234567') is False)