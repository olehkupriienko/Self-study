def is_acceptable_password(line: str):
    return any(i.isdigit() for i in line) and len(line) >= 6



print(is_acceptable_password('short') is False)
print(is_acceptable_password('muchlonger') is False)
print(is_acceptable_password('ashort') is False)
print(is_acceptable_password('muchlonger5') is True)
print(is_acceptable_password('sh5') is False)