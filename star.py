from turtle import Turtle
t = Turtle()
num = int(input("Enter the no of stars: "))
len = int(input("Enter the length: "))

def star(t,length):
    t.pencolor("red")
    t.down()
    t.fillcolor("red")
    t.begin_fill()
    t.right(75)
    t.forward(length)
    for count in range(4):
        t.down()
        t.left(144)
        t.forward(length)
    t.end_fill()

for count in range(num):
    star(t,len)
    angle=360/num
    t.up()
    t.forward(len*2)  
    t.right(angle)
