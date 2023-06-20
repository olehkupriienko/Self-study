from random import randint
class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


choice_dict = {1: Line, 2: Rect, 3: Ellipse}

elements = []
for i in range(217):
    elements.append(choice_dict[randint(1, 3)](randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)))

for element in elements:
    if isinstance(element, Line):
        element.ep = (0, 0)
        element.sp = (0, 0)
