import random

def roll_die ():
    r = random.randrange(1, 6)
    return r

def take_turn(player):
    point=0
    keep_rolling=1
    print ("\tits your turn player-->", player)
    input( "press enter to begin")
    while keep_rolling==1:
        r = roll_die()
        print("\n\tyou got a", r)
        if r == 1:
            point=0
            keep_rolling=0
        else:
            point += r
            print(" your total point is", point)
            if player=="You":
            	y= input("do you want to continue? y=yes n=no>>>")
            if player=="Computer":
            	tuple=("y","n")
            	y=random.choice(tuple)
            	print("do you want to continue? y=yes n=no>>>",y)
            if y== "y":
                keep_rolling= 1
            else:
                keep_rolling= 0
    print("\t",player,"'s turn is over")
    return point
    
def show_instructions():
	print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ---Rules---
    Number of players: 1 (You versus Computer)
    Number of dice: 1
    1) Decide who will start by having each player roll a dice – the one with the highest score starts the game.
    2) A player’s turn starts by rolling only one dice. The player continues to roll the dice again, as long as he does not roll a 1 or decides to add his points to his overall score.
    Each time the player rolls the dice, the following options exist:
        ~ The player rolls a 1 – his turn ends without any points (he also loses the points from any previous rolls in the current turn).
        ~ Any other number than a 1 is rolled – the player can add that number to the points scored in his current turn and continue by rolling the dice again.
        ~ The player decides to end his current turn and add all the points from his turn to his overall score.
    3) The game ends when a player has reached 100 points and becomes the winner of the game!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
""")
def main():
    show_instructions()
    p1 = 0
    p2 = 0
    players=(input("Your name>>>"),"Computer")
    a=random.choice(players)
    if a=="You":
    	b="Computer"
    else:
    	b="You"
    while p1<100 and p2<100:
        r = take_turn(a)
        p1 += r
        print("Player",a,"'s points are:" +str(p1))
        print ("Player",b,"'s points are:" +str(p2))
        r = take_turn(b)
        p2 += r
        print (" The game is over")
        print (" Player",a,"'s points are:" +str(p1))
        print (" Player",b,"'s points are:" +str(p2))
    if p1>p2:
        print("You are the winner-->",a)
    elif p2>p1:
        print ("Computer is the winner-->",b)
    else:
        print(" Tie game")
       
        
main()
take_turn("You")
take_turn("Computer")

