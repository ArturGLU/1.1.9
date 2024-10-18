import turtle as t

class Shape_Design:
    def __init__(self, color):
        self.turtle = t.Turtle()  
        self.turtle.penup()
        self.turtle.fillcolor(color)
        self.turtle.speed(0)

    def get_position(self):
        return self.turtle.position()

class Draw_Shapes:
    def __init__(self, num_patterns):
        self.shapes = ["square", "triangle", "circle"]
        self.colors = ["red", "yellow", "orange", "blue", "green", "pink", "purple"]
        self.num_patterns = num_patterns
        self.tloc = -100
        self.xloc = -180

    def create_shapes(self):
        for i in range(self.num_patterns):
            shape = self.shapes[i % len(self.shapes)]
            for color in self.colors:
                self.draw_shape(shape, color, (self.xloc, self.tloc))
                self.tloc += 20
            self.xloc += 60
            self.tloc = -80

    def draw_shape(self, shape, color, position):
        draw = Shape_Design(color)
        draw.turtle.goto(position)
        draw.turtle.pendown()
        draw.turtle.begin_fill()

        if shape == "square":
            for _ in range(4):
                draw.turtle.forward(30)
                draw.turtle.right(90)
        elif shape == "triangle":
            for _ in range(3):
                draw.turtle.forward(30)
                draw.turtle.right(120)
        elif shape == "circle":
            draw.turtle.circle(20)

        draw.turtle.end_fill()
        draw.turtle.penup()

while True:
    num_patterns = input("How many patterns do you want? (No more than 5) ")

    if not num_patterns.isdigit() or int(num_patterns) < 1 or int(num_patterns) > 5:
        print("Only positive whole numbers allowed")
    else:
        num_patterns = int(num_patterns)
        turtle_draw = Draw_Shapes(num_patterns)
        turtle_draw.create_shapes()
        break

wn = t.Screen()
wn.mainloop()
