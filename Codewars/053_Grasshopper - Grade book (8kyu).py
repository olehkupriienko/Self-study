a, b, c = 95, 93, 90


def get_grade(s1, s2, s3):
    avarege = (s1 + s2 + s3) / 3
    if 90 <= avarege <= 100:
        return 'A'
    elif 80 <= avarege < 90:
        return 'B'
    elif 70 <= avarege < 80:
        return 'C'
    elif 60 <= avarege < 70:
        return 'D'
    else:
        return "F"


print(get_grade(a, b, c))
