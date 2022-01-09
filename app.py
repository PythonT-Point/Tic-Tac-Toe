from turtle import *
import turtle as tur
 
 
# getting a Screen to work on
wd=tur.Screen()
 
# Defining Turtle instance
turt=tur.Turtle()
tur.title("Pythontpoint") 
# setting up turtle color to green
turt.color("blue")
 
# Setting Up width to 2
turt.width("4")
 
# Setting up speed to 2
turt.speed(2)
 
# Loop for making outside square of
# length 300
for i in range(4):
    turt.forward(300)
    turt.left(90)
 
 
# code for inner lines of the square
turt.penup()
turt.goto(0,100)
turt.pendown()
 
turt.forward(300)
 
turt.penup()
turt.goto(0,200)
turt.pendown()
 
turt.forward(300)
 
turt.penup()
turt.goto(100,0)
turt.pendown()
 
turt.left(90)
turt.forward(300)
 
turt.penup()
turt.goto(200,0)
turt.pendown()
 
 
turt.forward(300)

tur.done()