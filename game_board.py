######################################################################
# Board drawer
# Muntaha Chowdhury
# June 10, 2024
# A library that quickly draws the board for the game. Everything is in a function to make it run only if user wants to play 
######################################################################

import turtle



def ready_board():
    line = turtle.Turtle()
    line.pensize(3)
    line.speed(0)

    wn = turtle.Screen()
    wn.bgcolor("Beige")
    wn.setup(620,620)
    turtle.tracer(False)
    # SETUP game board
    line.up()
    line.goto(-300,-300)
    line.down()
    line.speed(0)

    for d in range(10):   #Change back to 10
        for c in range(10):
            for b in range(4):
                line.fd(60)
                line.lt(90)
            line.fd(60)
        line.lt(90)
        line.fd(60)
        line.lt(90)
        line.fd(600)
        line.lt(180)
        


    # Register shapes
    line.up()

    turtle.register_shape("board_nums.gif")

    turtle.register_shape("ladder1.gif")
    turtle.register_shape("ladder2.gif")
    turtle.register_shape("ladder3.gif")
    turtle.register_shape("ladder4.gif")
    turtle.register_shape("ladder5.gif")
    turtle.register_shape("ladder6.gif")

    turtle.register_shape("snek1.gif")
    turtle.register_shape("snek2.gif")
    turtle.register_shape("snek3.gif")
    turtle.register_shape("snek4.gif")
    turtle.register_shape("snek5.gif")
    turtle.register_shape("snek6.gif")



    # Stamp board numbers
    line.shape("board_nums.gif")
    line.goto(0,0)
    line.stamp()

    # Stamp ladders
    # Ladder 1
    line.shape("ladder1.gif")
    line.goto(60,0)
    line.stamp()
    # Ladder 2
    line.shape("ladder2.gif")
    line.goto(0, 120)
    line.stamp()
    # Ladder 3
    line.shape("ladder3.gif")
    line.goto(0, -180)
    line.stamp()
    # Ladder 4
    line.shape("ladder4.gif")
    line.goto(-210, -30)
    line.stamp()
    # Ladder 5
    line.shape("ladder5.gif")
    line.goto(160, -200)
    line.stamp()
    # Ladder 6
    line.shape("ladder6.gif")
    line.goto(-240, 180)
    line.stamp()



    # Stamp snakes

    # Snake 1
    line.shape("snek1.gif")
    line.goto(-120, -210)
    line.stamp()
    # Snake 2
    line.shape("snek2.gif")
    line.goto(110, 100)
    line.stamp()
    # Snake 3
    line.shape("snek3.gif")
    line.goto(-10, 20)
    line.stamp()
    # Snake 4
    line.shape("snek4.gif")
    line.goto(150, -140)
    line.stamp()
    # Snake 5
    line.shape("snek5.gif")
    line.goto(-170, 100)
    line.stamp()
    # Snake 6
    line.shape("snek6.gif")
    line.goto(210, -20)
    line.stamp()



    turtle.update()
    turtle.tracer(True)



        