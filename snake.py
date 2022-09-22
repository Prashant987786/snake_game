from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_size = []
        self.create_snake()
        self.head = self.snake_size[0]

    def create_snake(self):
        for seg in STARTING_POSITION:
            self.add_segment(seg)

    def add_segment(self, position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.snake_size.append(tim)

    def reset(self):
        for seg in self.snake_size:
            seg.goto(10000, 10000)
        self.snake_size.clear()
        self.create_snake()
        self.head = self.snake_size[0]

    def extent(self):
        self.add_segment(self.snake_size[-1].position())

    def move(self):
        for seg in range(len(self.snake_size) - 1, 0, -1):
            new_xcor = self.snake_size[seg - 1].xcor()
            new_ycor = self.snake_size[seg - 1].ycor()
            self.snake_size[seg].goto(new_xcor, new_ycor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
