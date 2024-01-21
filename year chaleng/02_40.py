'''Exercise: Simulating Player Data

You are developing a small program to simulate player data for a game. 
Create a Python code that uses basic concepts such as function 
declaration, loops, lists, conditionals, and random number generation 
to generate information about fictional players.

Code Objective:

The program should generate and display, for each player, their name, 
level, and health points. Use a list to store the players' names, and 
for each player, randomly generate a level between 1 and 10 and health 
points between 50 and 100.'''

from random import choice
from random import randint

def main():

    name=['Mosiah', 'Alma', 'Nephi', 'Lehi', 'Sarha', 'Marie', 'Jhon']
    player_number = int(input('How many player are: '))
    print()
    player_data(name, player_number)

def player_data(name, player_number):
    for player in range(player_number):
        print(f'Name = {choice(name)}')
        print(f'level = {randint(1, 10)}')
        print(f'Life Point = {randint(50, 100)}')
        print()

main()