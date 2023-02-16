import turtle, random, time
pen = turtle.Turtle()
pen.speed(0)
def starFill(n,dlina): #Функция закрашивания звезды
    pen.begin_fill()
    if n % 2 !=0:
        for i in range(n):
            pen.forward(dlina)
            #pen.color("yellow")
            angle = n // 2 * 360 / n
            pen.left(angle)
        pen.end_fill()

window = turtle.Screen()
window.bgcolor('black')
window.setup(600,500) #размеры экрана

pen.color('yellow')
for i in range(50):
    x = random.randint(-640,640) #Возвращает случайное целое в каком-либо диапазоне координаты x
    y = random.randint(-440,400) #Возвращает случайное целое в каком-либо диапазоне координаты y
    pen.up()
    pen.setposition(x,y)
    pen.down()
    size = random.randint(10,20)
    vershina = random.choice([5,7,9,11,13,15])
    starFill(vershina,size)
time.sleep(5) #таймер замирания
turtle.done()