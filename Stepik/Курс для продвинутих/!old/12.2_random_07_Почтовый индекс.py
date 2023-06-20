def generate_index():
    import random
    import string
    return f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.randint(0, 99)}_\
{random.randint(0, 99)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}"


print(generate_index())
