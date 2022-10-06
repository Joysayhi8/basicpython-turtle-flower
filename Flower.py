Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
tao.shape('turtle')

def Flower():
    for i in range(300):
        tao.circle(190-i,90)
        tao.left(90)
        tao.circle(190-i,90)

        
def Move(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

    
Move(50,50)
Flower()
mainloop()
