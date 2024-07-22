# Caraballo, Joseph
# 8 July 2024
# P4Lab1
# Drawing shapes with Turtle graphic program with loops

import turtle

screen = turtle.Screen() 
screen.bgcolor("white")

joe = turtle.Turtle() 
joe.shape("turtle") 
joe.color("black") 

def draw_J(size): 
    joe.penup() 
    joe.goto(-50, 50) 
    joe.pendown() 
    joe.right(90) 
    joe.forward(size) 
    joe.circle(-size // 2, 180) 
    joe.penup() 
    joe.goto(0, 0) 
    joe.pendown() 

def draw_C(size): 
    joe.penup() 
    joe.goto(50, 50) 
    joe.pendown() 
    joe.circle(size, 180) 
    joe.penup() 
    joe.goto(0, 0) 
    joe.setheading(0)
    joe.pendown() 

draw_J(100) 

joe.penup() 
joe.goto(100, 50) 
joe.pendown() 

draw_C(50) 

joe.hideturtle() 
turtle.done()
