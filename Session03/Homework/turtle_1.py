from turtle import *
speed=(-1)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range (3, 8):
    for y in range(i):
        pencolor(colors[i - 3])
        forward(100)
        left(360/i)

mainloop()
