import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Traffic Light")
wn.bgcolor("lightgreen")
light = turtle.Turtle()

def draw_housing():
    light.pensize(3)
    light.color("black","darkgrey")
    light.begin_fill()
    light.forward(80)
    light.left(90)
    light.forward(200)
    light.circle(40,180)
    light.forward(200)
    light.left(90)
    light.end_fill()

draw_housing()

light.penup()

light.forward(40)
light.left(90)
light.forward(50)
light.shape("circle")
light.shapesize(3)
light.fillcolor("green")

#Traffic light has three states - lets use following numbers 
#for following colors: 0 - Green, 1- Orange, 2 - Red
state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0:
        light.forward(70)
        light.fillcolor("orange")
        state_num = 1
    elif state_num == 1:
        light.forward(70)
        light.fillcolor("red")
        state_num = 2
    else:
        light.back(140)
        light.fillcolor("green")
        state_num = 0
    
wn.ontimer(advance_state_machine,30)

wn.listen()
wn.mainloop()
        