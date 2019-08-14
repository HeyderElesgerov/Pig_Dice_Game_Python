import random
import time

class Player():
    def __init__(self, Dice):
        self.Dice = Dice
    
    def play(self):
        TurnPoint = 0
        while True:
            Dice = random.randint(1,6)
            print('It\'s', Dice)
            if Dice == 1:
                print('It\'s 1. You lost your points!')
                return 0
            else:
                TurnPoint += Dice
                print('It\'s', Dice, 'This turn\'s point is', TurnPoint, 'Roll again?(y)')
            c = input()
            if c == 'y' or c == 'Y':
                print('Rolling again!')
                continue
            else:
                return TurnPoint
    
    def rollagain(self):
        poss = random.randint(0,1)
        return poss

print('~~~Welcome to \'Pig\' game! To begin playing, input 1. \nTo see the rules, input 2.')
while True:
    a = input()
    if a == '1':
        print('Game is beginning!')
        Computer = Player(0)
        Opponent = Player(0)
        Comp_Point = 0
        Opp_Point = 0
        while True:
            print('Rolling the Dice to choose who starts the game!')
            time.sleep(1)
            Comp_begin_dice = random.randint(1, 6)
            Opp_begin_dice = random.randint(1, 6)
            if Comp_begin_dice > Opp_begin_dice:
                #Computer begins and plays
                print('Computer Begins! Computer dice : Your dice', Comp_begin_dice, Opp_begin_dice)
                a = 0
                print('Computer is rolling the dice!')
                while Comp_Point < 100 and Opp_Point < 100:
                    time.sleep(1)
                    if a%2 == 0:
                        Computer.play()
                        a += 1
                        continue
                    if a%2 == 1:
                        Opponent.play()
                        a += 1
                        continue
                if Comp_Point > Opp_Point:
                    print('Computer won! Computer\'s Points:', Comp_Point)
                else:
                    print('You won! Your Points:', Opp_Point)
            elif Comp_begin_dice == Opp_begin_dice:
                #Draw
                print('Draw, both are:', Comp_begin_dice)
                print('Rolling again!')
                continue
            else:
                #You begin and play
                print('You begin! Computer dice : Your dice', Comp_begin_dice, Opp_begin_dice)
                while Comp_Point < 100 and Opp_Point < 100:
                    print('You are rolling the dice!')
                    Opponent.play()
                if Comp_Point > Opp_Point:
                    print('Computer won! Computer\'s Points:', Comp_Point)
                else:
                    print('You won! Your Points:', Opp_Point)

    elif a == '2':
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
        continue
    else:
        print('Input 1 or 2 only!')
        continue
