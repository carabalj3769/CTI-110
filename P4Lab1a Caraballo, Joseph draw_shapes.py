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

def draw_square(size): 
    for _ in range(4): 
        joe.forward(size) 
        joe.right(90) 

def draw_triangle(size): 
    for _ in range(3): 
        joe.forward(size) 
        joe.right(120) 

draw_square(100) 

joe.penup() 
joe.goto(150, 0) 
joe.pendown() 

draw_triangle(100) 

joe.hideturtle()  
turtle.done()