from turtle import Turtle

startpos= [(0,0), (-20,0), (-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class snake:
    def __init__(self):
      self.newsegment=[]
      self.create_snake()
      self.head=self.newsegment[0]

    def create_snake(self):
        for seg in startpos:
            self.add_segment(seg)

        
    def add_segment(self, seg):
        segments=Turtle("square")
        segments.goto(seg)
        segments.color("white")
        segments.penup()
        self.newsegment.append(segments)

    def extend(self):
        self.add_segment(self.newsegment[-1].position())

        

    def forward_movement(self):  
        for i in range(len(self.newsegment)-1,0,-1):
            newx= self.newsegment[i-1].xcor()
            newy= self.newsegment[i-1].ycor()
            self.newsegment[i].goto(newx,newy)
        self.newsegment[0].speed(4)    
        self.newsegment[0].forward(20)
          
        

    def up(self):

        if(self.head.heading()!=DOWN):
            self.head.setheading(UP)
    def down(self):
        if(self.head.heading()!=UP):
            self.head.setheading(DOWN)
    def left(self):
        if(self.head.heading()!=RIGHT):
            self.head.setheading(LEFT)
    def right(self):  
        if(self.head.heading()!=LEFT):
            self.head.setheading(RIGHT) 


