from turtle import Turtle, right
START_POST =[(0,0),(-20,0),(-40,0)] #const are capital letters and are out of class
DISTANCE = 20
UP= 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:

    def __init__(self):
        self.blocks= []
        self.createSnake()
        self.head = self.blocks[0] 

    def createSnake(self):
        for post in START_POST:
            self.newBlock(post)
    
    def newBlock(self, post):
        block = Turtle("square")
        block.color("green")
        block.penup()
        block.goto(post)
        self.blocks.append(block)

    def extend(self):
        self.newBlock(self.blocks[-1].position())

    def move(self):
        for block_num in range(len(self.blocks) - 1, 0, -1): #range (start, stop, step)
            x = self.blocks[block_num - 1].xcor()
            y = self.blocks[block_num - 1].ycor()
            self.blocks[block_num].goto(x,y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)
    
    def left(self):
        self.head.setheading(LEFT)
    
    def right(self):
        self.head.setheading(RIGHT)
    



        
        