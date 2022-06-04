#adding librarires 
import random
import time
import os
import sys

#welcome screen
print("----Welcome to the dice game!----")
print('for first player:', 1)
print('for second player:', 2)

gamer = int(input("Please choose the player:"))

if gamer == 1:
    print('you select the first player.')
elif gamer == 2:
    print('you select the second player.')
else :
    print('please follow the instruction.')

number_of_game = 1 #total number of game
total_win1 = 0 #number ofgame won by player 1
total_win2= 0  ##number ofgame won by player 2
while(True):
    throw_1 = random.randint(1,6)
    time.sleep(2)   #add time delay    
    throw_2 = random.randint(1,6)
    if throw_1 > throw_2:
        print("{0}{1} : Fist player won the game!".format('Game ',number_of_game))
        total_win1 += 1
    elif throw_2 > throw_1:
        print("{0}{1} : Second player won the game!".format('Game ',number_of_game))
        total_win2 += 1
    else :
        print("{0}{1} : Tied game!".format('Game ',number_of_game))
    if number_of_game == 3:
        print('\n')
        if total_win1 > total_win2:
            print('Fist player won the game!')
        elif total_win2 > total_win1:
            print('Second player won the game!')
        else :
            print('Tied game!')
        print('Game Over')
        break
    number_of_game +=1
    
# to restart the program
restart = input('\nDo you wanna replay the game?[y/n]>')
if restart == 'y':
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
else :
    print('\nThe game is being closed...')
    sys.exit(0)
    







