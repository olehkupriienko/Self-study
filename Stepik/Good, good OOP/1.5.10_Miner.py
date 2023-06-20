class Cell:
    def __init__(self, around_mies, mine):
        self.around_mies = around_mies
        self.mine = mine


class GamePole:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pole = [[Cell(0, False) for i in range(x)] for j in range(y)]


