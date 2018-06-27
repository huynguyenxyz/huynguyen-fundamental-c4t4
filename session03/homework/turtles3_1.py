from turtle import *
shape("turtle")
speed(1)
for i in range (3,8):
    if i%3 == 0:
        color("red")
    elif i%4 == 0:
        color ("blue")
    elif i % 5==0:
        color("purple")
    elif i%6==0:
        color("yellow")
    else:
        color ("grey")
    for j in range (i):
        forward (100)
        left (360/i)
mainloop()
    