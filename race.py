import time
import turtle
import random
import pyfiglet
import termcolor
from termcolor import colored
from pyfiglet import print_figlet

print_figlet('Turtle Race', font = 'slant', colors = '64;255;115')
print (colored('-------------------------------------------------', 'red'))
num = int(input('How Many Races Would You Like to See? '))
print (colored('-------------------------------------------------', 'red'))
print(colored(f'Number of Races = {num}', 'green'))
print (colored('-------------------------------------------------', 'red'))

win1 = 0
win2 = 0
space = 20

def totalgames(num, wins, total):
    print (f'Turtle {num} Has {wins} Wins !!!')
    print (f'Turtle {num} Win Rate Is {wins/total}')


for i in range(num):
    
    turtle.bgcolor ('green')
    sq = turtle.Turtle()
    sq.shape("square")
    sq.speed(1000000000000000)
    sq.color("white")
    sq.penup()

    for i in range(20):
        sq.goto(240, (300 - (i * space * 2)))
        sq.stamp()

    for i in range(20):
        sq.goto(240 + space, ((340 - space) - (i * space * 2)))
        sq.stamp()

    sq.color("black")
    for i in range(20):
        sq.goto(240, (320 - (i * space * 2)))
        sq.stamp()

    for i in range(20):
        sq.goto(240 + space, ((320 - space) - (i * space * 2)))
        sq.stamp()

    for i in range(20):
        sq.color("white")
        sq.goto(-285, (300 - (i * space * 2)))
        sq.stamp()

    for i in range(20):
        sq.color("white")
        sq.goto(-285 + space, ((340 - space) - (i * space * 2)))
        sq.stamp()

    sq.color("black")
    for i in range(20):
        sq.goto(-285, (320 - (i * space * 2)))
        sq.stamp()

    for i in range(20):
        sq.goto(-285 + space, ((320 - space) - (i * space * 2)))
        sq.stamp()

    one = turtle.Turtle()
    two = turtle.Turtle()
    ref = turtle.Turtle()
    

    one.shape("turtle")
    two.shape("turtle")
    ref.shape("turtle")

    one.speed(1000000000000000)
    two.speed(1000000000000000)
    ref.speed(1000000000000000)

    one.color("red")
    two.color("blue")

    one.penup()
    one.goto(-275,100)

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

    one.penup()
    two.penup()
    one.goto(-130,100)
    two.goto(-130,50)
    one.write("Distance traveled: " + str(distance), font=('Arial', 28 , 'italic'))
    two.write("Distance traveled: " + str(distance1),font=('Arial', 28 , 'italic'))

    time.sleep(1)

    if distance>distance1:
        one.right(90)
        one.forward(20)
        one.left(90)
        one.write("Winner Yeehaw", font=('Arial', 28 , 'italic'))
        win1 += 1
        time.sleep(1)

    else:
        two.right(90)
        two.forward(20)
        two.left(90)
        two.write("Winner Yeehaw",font=('Arial', 28 , 'italic'))
        win2 += 1

        time.sleep(1)
        
    turtle.clearscreen()

totalgames(1, win1, num)
totalgames(2, win2, num)

turtle.mainloop()

