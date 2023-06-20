class Ghost(object):

    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        from random import choice
        self.color = choice(colors)


    # def __init__(self):
    #     from random import randint
    #     colors = ["white", "yellow", "purple", "red"]
    #     self.color = colors[randint(0, 3)]


ghosts = [Ghost().color for _ in range(10)]
print(*ghosts)
