class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


ball_one = Ball()
print(ball_one.ball_type)

ball_two = Ball('super')
print(ball_two.ball_type)
