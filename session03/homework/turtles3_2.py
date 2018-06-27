from turtle import*
import random, turtle
shape("turtle")
turtle.width = 10

speed(-5)
# color("red")
# color("blue")
choices = ["black","grey"]

for i in range(1,101):
    forward (i*5)
    left (90)

    turtle.color (random.choice(choices))
mainloop()