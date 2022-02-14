import turtle
import random
import time

retraso=0.1

s = turtle.Screen()
s.setup(650,650)
s.bgcolor('gray')
s.title('Proyecto Serpiente')

serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape('square')
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction='stop'
serpiente.color('green')

comida = turtle.Turtle()
comida.shape('circle')
comida.color('orange')
comida.penup()
comida.goto(0,100)
comida.speed(0)


def arriba():
    serpiente.direction='up'
def abajo():
    serpiente.direction='down'
def derecha():
    serpiente.direction='right'
def izquierda():
    serpiente.direction='left'

s.listen()
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")




def movimiento():
    if serpiente.direction == 'up':
        y=serpiente.ycor()
        serpiente.sety(y + 20)
    if serpiente.direction == 'down':
        y=serpiente.ycor()
        serpiente.sety(y - 20)
    if serpiente.direction == 'rigth':
        x=serpiente.xcor()
        serpiente.setx(x + 20)
    if serpiente.direction == 'left':
        x=serpiente.xcor()
        serpiente.setx(x + 20)


while True:
    s.update()

    if serpiente.distance(comida) < 20:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape('square')
        nuevo_cuerpo.color('green')
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0, 0)
        nuevo_cuerpo.speed(0)



    movimiento()
    time.sleep(retraso)


turtle.done()
