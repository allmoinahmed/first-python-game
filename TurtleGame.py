import turtle as t
import random as ra
import time as ti

screen = t.Screen()
# screen.screensize(1800, 1280)
screen.bgcolor('gray')

# Player One Basic Setup
pl_one = t.Turtle()
# pl_one.speed(100)
pl_one.color('white')
pl_one.shape('turtle')
pl_one.shapesize(2)


# Setup a referee
referee = pl_one.clone()
referee.penup()
referee.color('black')
referee.shape('turtle')
referee.shapesize(4)

# Player Two Basic Setup
pl_two = pl_one.clone()
pl_two.color('black')


# Moving the Player to Starting point
pl_one.penup()
pl_one.goto(-400,350)

pl_two.penup()
pl_two.goto(-400,-325)


# Save Line positions in List/Array:p 
linePos = []


# Drawing Food Line For Player One
i = 1
for i in range(1, 10):
    pl_one.color('black')
    if i != 1:
        pl_one.forward(100)
        pl_one.write(round(pl_one.xcor()), font='40')
        linePos.append(pl_one.pos())
    else:
        pl_one.forward(50)
        pl_one.write(round(pl_one.xcor()), font='40')
    pl_one.pendown()    
    pl_one.left(90)
    pl_one.forward(30)
    pl_one.back(70)
    pl_one.penup()
    pl_one.forward(30+(5*2))
    pl_one.right(90)
    pl_one.penup()

pl_one.penup()
pl_one.color('white')
pl_one.goto(-400,350)

# Drawing Food Line For Player Two
j = 1
for j in range(1, 10):
    pl_two.color('white')
    if j != 1:
        pl_two.forward(100)
        pl_two.write(round(pl_two.xcor()), font='40')
    else:
        pl_two.forward(50)
        pl_two.write(round(pl_two.xcor()), font='40')
    pl_two.pendown()    
    pl_two.left(90)
    pl_two.forward(30)
    pl_two.back(70)
    pl_two.penup()
    pl_two.forward(30+(5*2))
    pl_two.right(90)
    pl_two.penup()

pl_two.penup()
pl_two.color('black')
pl_two.goto(-400,-325)

# Lets start the racing 
referee.goto(-200,0)
referee.write('Lets start the Race', font=('Arial', 25, 'normal'))
referee.goto(-400,0)
referee.color('red')

# Set Counter / Game / Race Time
def setCounter(rt):
    while rt:
        mins, secs = divmod(rt, 60)
        screen.title('Race Time Left: {:02d}:{:02d}'.format(mins, secs))        
        ti.sleep(1)
        rt -= 1      

# Turtle Move
rndNum = [50,100]
for s in range(30):
    if pl_one.xcor() >= 400:
        pl_one.write('Winner', font=('Arial', 25, 'normal'))
        break
    elif pl_two.xcor() >= 400:
        pl_two.write('Winner', font=('Arial', 25, 'normal'))
        break
    else:
        moveForward = ra.choice(rndNum)
        pl_one.forward(moveForward)
        ti.sleep(1)
        moveForward2 = ra.choice(rndNum)
        pl_two.forward(moveForward2)    
setCounter(int(5))    








# To Keep Drawing Board  on Screen
t.done()
