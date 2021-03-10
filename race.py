import turtle
import random
import time

num = int(input('How Many Races Would You Like to See? '))

win1 = 0
win2 = 0

for i in range(num):
    one = turtle.Turtle()
    two = turtle.Turtle()
    ref = turtle.Turtle()

    one.shape("turtle")
    two.shape("turtle")
    ref.shape("turtle")

    one.speed(5)
    two.speed(0)
    ref.speed(0)

    one.color("red")
    two.color("blue")

    one.penup()
    one.goto(-275,200)

    two.penup()
    two.goto(-275, -200)

    ref.penup()
    ref.goto(-275, 400)
    ref.pendown()
    ref.right(90)
    ref.forward(800)

    ref.penup()
    ref.goto(250, 400)
    ref.pendown()
    ref.forward(800)

    total_length = 525 
    distance = 0
    distance1 = 0

    while distance < 525 and distance1 < 525:
        move = random.randint(0,100)
        move1 = random.randint(0,100)
        one.forward(move)
        two.forward(move1)
        time.sleep(0.5)
        distance1 += move1
        distance += move
    one.write("Distance traveled: " + str(distance), font=('Arial', 28 , 'italic'))
    two.write("Distance traveled: " + str(distance1),font=('Arial', 28 , 'italic'))

    if distance>distance1:
        one.right(90)
        one.forward(20)
        one.left(90)
        one.write("winner yeehaw", font=('Arial', 28 , 'italic'))
        win1 += 1

    else:
        two.right(90)
        two.forward(20)
        two.left(90)
        two.write("winner yeehaw",font=('Arial', 28 , 'italic'))
        win2 += 1
        
    turtle.clearscreen()

print (f'Turtle 1 Has {win1} Wins !!!')
print ('Turtle 1 win rate is', win1/num)

print (f'Turtle 2 Has {win2} Wins !!!')
print ('Turtle 2 win rate is', win2/num)

turtle.mainloop()

