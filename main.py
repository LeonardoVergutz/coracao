from turtle import *

color("red")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

penup()
goto(-70, -100)
pendown()
write("Te odeio, chatinha!", font=("Arial", 12, "normal"))  # Escreve o texto
hideturtle()

done()