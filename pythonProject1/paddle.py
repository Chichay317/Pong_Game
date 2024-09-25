from turtle import Turtle


class MyPaddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        # Stretch wid is vertical while stretch len is horizontal (sets the width and height of turtle)
        # turtle is 20 by 20 normally. so we stretch it vertically 5 times (stretch_wid) and horizontally 1 time (stretch_len)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
