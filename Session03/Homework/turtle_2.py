from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for n in range(5):
        color(colors.pop(0))
        begin_fill()
        for i in range(2):
            forward(50)
            left(90)
            forward(100)
            left(90)
        end_fill()
        forward(50)
mainloop()
