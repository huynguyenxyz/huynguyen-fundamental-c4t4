from turtle import *
shape ("turtle")
begin_fill()
color ("red")
for i in range(3):
    forward (100)
    left(120)
end_fill()
color ("black")
for i in range (4):
    forward (100)
    right (90)

penup()
goto(15,-100)
pendown()
begin_fill()
color("blue")
for i in range(2):
    forward (30)
    left (90)
    forward (70)
    left(90)
end_fill()
penup()
goto(50, -40)
pendown()
begin_fill()
color("yellow")
for i in range (4):
    forward(35)
    left(90)
end_fill()
mainloop()