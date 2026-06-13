######################################################################
# Snakes & Ladders
# Muntaha Chowdhury
# June 10, 2024
# 2 player game that uses shaking and buttons to move forward
######################################################################

import microbit, turtle, random, time, tkinter
from game_board import *


######################################
#            Game starter            #
######################################
def prompt():
    extra_wn = tkinter.Tk()    #Handles the extra window that opens
    extra_wn.withdraw()
    response = tkinter.messagebox.askyesno(title="Instructions",
                                message=None,
                                detail=f"""Shake to roll the dice
Use buttons to move forward
    
This is a 2 player game
Player A moves with Button A ONLY
Player B moves with Button B ONLY
    
But you may play alone if you want ;-;

Play?""")
    return response


######################################
#           Dice mechanics           #
######################################

#Dice faces
dice1 = "44444:" \
        "40004:" \
        "40904:" \
        "40004:" \
        "44444"

dice2 = "44444:" \
        "40004:" \
        "49094:" \
        "40004:" \
        "44444"

dice3 = "44444:" \
        "40004:" \
        "49994:" \
        "40004:" \
        "44444"

dice4 = "44444:" \
        "49094:" \
        "40004:" \
        "49094:" \
        "44444"

dice5 = "44444:" \
        "49094:" \
        "40904:" \
        "49094:" \
        "44444"

dice6 = "44444:" \
        "49994:" \
        "40004:" \
        "49994:" \
        "44444"

dice = [dice1, dice2, dice3, dice4, dice5, dice6]

def roll_dice():
    # Function rolls dice and returns allowed moves
    roll = random.randint(0,5)
    rolled = microbit.Image(dice[roll])
    microbit.display.show(rolled)
    return roll + 1


def shake():
    # Function detects shake and rolls dice
    atrest_z = microbit.accelerometer.get_z()
    while True:
        current_z = microbit.accelerometer.get_z()
        if current_z > (atrest_z + 500):
            moves = roll_dice()
            return moves
        
        

######################################
#         Snakes and Ladders         #
######################################

def check_ladders(x, y, piece):
    #Checks for ladders. Advance up
    if x == 90 and (y == -260 or y== -280):   #Longest green ladder
        piece.goto(x+60*2, y+60*2)
        piece.setheading(0)
    elif x == 30 and (y == -200 or y == -220):  #Smallest yellow ladder
        piece.goto(x-60, y+60)
        piece.setheading(0)
    elif x == -150 and (y == -80 or y == -100):  #Longest yellow ladder
        piece.goto(x-60*2, y+60*2)
        piece.setheading(180)
    elif x == 30 and (y == -80 or y == -100):   #Brown ladder
        piece.goto(x+60, y+60*3)
        piece.setheading(0)
    elif x == -150 and (y == 40  or y == 20):    #Red ladder
        piece.goto(x+60*5, y+60*3)
        piece.setheading(0)
    elif x == -270 and (y == 160 or y == 140):
        piece.goto(x+60, y+60)
        piece.setheading(0)
    
    
    
def check_snakes(x, y, piece):
    #Check for snakes. Slide down
    if x == -150 and (y == -140 or y== -160):         #Small yellow snake
        piece.goto(x, y-60*2)
        piece.setheading(0)
    elif x == 90 and (y == -20 or y == -40):         # Small green snake
        piece.goto(x+60, y-60*4)
        piece.setheading(0)
    elif x == -30 and (y == 100 or y == 80):         #Large yellow snake
        piece.goto(x-60, y-60*3)
        piece.setheading(180)
    elif x == 270 and (y == 160  or y == 140):       # Pink snake
        piece.goto(x-60*2, y-60*6)
        piece.setheading(180)
    elif x == 30 and (y == 220  or y == 200):        # Purple snake
        piece.goto(x+60*3, y-60*4)
        piece.setheading(0)
    elif x == -150 and (y == 280 or y == 260):       # Large green snake
        piece.goto(x-60, y-60*6)
        piece.setheading(180)
        
        

######################################
#         Movement mechanics         #
######################################

def going_off_board(x, y):
    #Boolean function to see if pawn about to go off of board
    if x == -270 and (y == -260 or y == -280):    #Starting block doesn't count
        return False
    elif x == 270 or x == -270:                   # Sees if too right or left 
        return True
        
        
def fix_piece(x, piece):
    #Function keeps piece on board
    if x == 270:    #If on right edge
        piece.lt(90)
        piece.fd(60)
        piece.lt(90)
        
    elif x == -270:  #If on left edge
        piece.rt(90)
        piece.fd(60)
        piece.rt(90)
        
    
moved_a = 1
moved_b = 1

#move_forward
def move_pawn(moves, piece):
    # Main movement function
    global moved_a, moved_b   #Variables need to be global or they are always reset to 1 during another roll
    # Reseting buttons
    microbit.button_a.was_pressed()
    microbit.button_b.was_pressed()
    
    allowed_moves = moves
    pawn_x = round(piece.xcor())
    pawn_y = round(piece.ycor())
    
    
    while allowed_moves != 0:
        
        # User A
        if piece == pawn1:
            if microbit.button_a.was_pressed():
                if going_off_board(pawn_x, pawn_y) and moved_a == 1:
                    fix_piece(pawn_x, piece)
                    moved_a = 0
                else:
                    piece.fd(60)
                    moved_a = 1
                allowed_moves -= 1
                    
        #User B        
        else:
            if microbit.button_b.was_pressed():
                if going_off_board(pawn_x, pawn_y) and moved_b == 1:
                    fix_piece(pawn_x, piece)
                    moved_b = 0
                else:
                    piece.fd(60)
                    moved_b = 1
                allowed_moves -= 1
                    
        #Checked again since position is moved
        pawn_x = round(piece.xcor())
        pawn_y = round(piece.ycor())
        
        #If at end block
        if pawn_x == -270 and (pawn_y == 280 or pawn_y == 260):
            break
        

    check_ladders(pawn_x, pawn_y, piece)
    check_snakes(pawn_x, pawn_y, piece)

         
         

        
        
######################################
#       Player turn handlers         #
######################################     
def user_a():
    #Imstruct
    microbit.display.scroll("A")
    moves = shake()
    time.sleep(1)
    microbit.display.show(microbit.Image.ARROW_W)
    #Play
    move_pawn(moves, pawn1)
    if pawn1.xcor() == -270 and pawn1.ycor() == 280:
        turtle.bye()
        microbit.display.scroll("USER A won!")
    else:
        user_b()

    
    
def user_b():
    #Instruct
    microbit.display.scroll("B")
    moves = shake()
    time.sleep(1)
    microbit.display.show(microbit.Image.ARROW_E)
    move_pawn(moves, pawn2)
    #Play
    if pawn2.xcor() == -270 and pawn2.ycor() == 260:
        turtle.bye()
        microbit.display.scroll("USER B won!")
    else:
        user_a()


    




######################################
#           Main Program             #
######################################

while True:
    response = prompt()
    if response == True:
        ready_board()
        
        # Put in the loop so turtle window doesn't pop up
        turtle.register_shape("red_pawn.gif")
        turtle.register_shape("blue_pawn.gif")

        pawn1 = turtle.Turtle()
        pawn1.shape("red_pawn.gif")
        pawn1.up()
        pawn1.goto(-270, -260)
        
        pawn2 = turtle.Turtle()
        pawn2.shape("blue_pawn.gif")
        pawn2.up()
        pawn2.goto(-270, -280)
        
        user_a()
        
        #Reaches once game done
        for z in range(2):
            microbit.display.show(microbit.Image.HEART)
            time.sleep(0.5)
            microbit.display.show(microbit.Image.HEART_SMALL)
            time.sleep(0.5)
    else:
        print("ok")
        break


