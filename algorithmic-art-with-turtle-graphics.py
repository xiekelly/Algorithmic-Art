# Kelly Xie
# CSCI-UA 2
# May 11, 2015
# Algorithmic Art


# Program specifications:
#   at least five colors
#   at least five original functions
#   at least one list
#   at least one dictionary
#   at least one "for" loop
#   at least one "while" loop
#   at least one user option


from turtle import *
import random


def hexagon(s,n):
    
    color_list = ['#FFFFFF','yellow','green','blue','purple','#66FFFF','#66CCFF','#660066']
    bgcolor('black')
    
    for i in range(n//2):
        speed(0)
        color = random.choice(color_list)
        hexagon_draw(color,s) # calls function
        pu()
        backward(s*1.5)
        left(30)
        forward(s*2)
        pd()
        s*=1.2
        
    ht()
    done()
        
    
def hexagon_draw(hex_color,w):
    
    color(hex_color)

    for i in range(6):
        forward(w)
        right(60)
    
    pu()
    left(45)
    forward(w*1.5)
    pd()
            
    begin_fill()
    for i in range(6):
        forward(w)
        right(60)
    end_fill()
        
    return


def choose_circle(r,n):
    
    color_dictionary = {"warm": ['#FF3333','#FF9900','#FF9999','#FFCC33'],
                        "cool": ['#66CCFF','#660066','#CCFF00','#6666FF']}
    bgcolor('black')
    angle = random.choice([60,45,35,30])
    
    for i in range(n//2):
        speed(0)
        tone, color = color_dictionary.popitem()
        color_dictionary[tone] = color
        color = random.choice(color)
        circle_draw(color,r) # calls function
        pu()
        forward(r*2)
        left(angle) # 60,45,35,30 degrees
        backward(r*4)
        pd()
        r*=1.2

    ht()
    done()


def circle_draw(circle_color,r):

    color(circle_color)

    circle(r)
    
    pu()
    left(72)
    backward(r*1.5)
    pd()
            
    begin_fill()
    circle(r)
    end_fill()
        
    return
    

def drawing():
    
    shape = input("(h)exagons or (c)ircles? ")

    while shape.lower() not in ['h','c']:
        print("Not a valid option! Try again.\n")
        shape = input("(h)exagons or (c)ircles? ")

    if shape.lower() == 'h':
        side = int(input("What is the length of the sides of the first hexagon? "))
        num = int(input("How many hexagons do you want? (>50 for best results): "))
        hexagon(side, num) # calls function
        
    if shape.lower() == 'c':
        radius = int(input("What is the radius of the first circle? "))
        num = int(input("How many circles do you want? (>50 for best results): "))
        choose_circle(radius, num) # calls function


drawing()


