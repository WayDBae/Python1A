import turtle 
pen = turtle.Turtle()
speed = 5 

def moveUp():
    x = pen.position()[0]
    y = pen.position()[1]
    pen.setposition(x,y+speed)

def moveDown():
    x,y = pen.position()[0]
    pen.setposition(x, y - speed)

def moveLeft():
    x,y = pen.position()
    pen.setposition(x-speed, y)

def moveRight():
    x,y = pen.position()
    pen.setposition(x+speed,y)

def change():
    if pen.isvisible():
        pen.up()
        pen.hideturtle()
    else:
        pen.down()
        pen.showturtle()

def speedUp():
    global speed
    speed+=1
def speedDown():
    global speed
    speed = max(0, speed-1)

window = turtle.Screen()
pen = turtle.Turtle()

window.onkey(moveUp, "Up")
window.onkey(moveDown, "Down")
window.onkey(moveLeft, "Left")
window.onkey(moveRight, "Right")
window.onkey(moveRight, "Right")
window.onkey(change, "space") #событие меняющее местоположение
window.onkey(speedUp, "q")
window.onkey(speedDown, "w")

window.listen()
window.mainloop()
turtle.done()
