from turtle import *
#Hello_word:
def hello():
    for i in range (3):
        print ("Hello world")
#Sum
def summ(x,y):
    res = x+y
    print (res)
#square
def draw_square(length,colors):
    
    color (colors)
    for j in range (4):
        forward(length)
        left(90)
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

          





