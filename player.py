from turtle import Turtle

STARTING_POSITIION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITIION)
        self.setheading(90)

    def go_up(self):
        self.fd(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False