
from turtle import *
color('red')
for i in range(4):
        for i in range(2):
                left(60)
                forward(60)
        left(120)
        forward(60)
        left(60)
        forward(60)
        right(30)
color('white')
forward(300)
for i in range(4):
        n=180-(180+180*i)/(i+3)
        if i%2==0: color('blue')
        else :color('red')
        for j in range(i+3):
                left(n)
                forward(60)


mainloop()