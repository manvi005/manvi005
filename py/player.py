from turtle import Turtle
STARTING_POSITION = (0,-250)
MOVE_DISTANCE = 10
FINISH_LINE = 200


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.backward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

# crossing
    def at_finish(self):
        if self.ycor()>280:
            return True
        else:
            return False





