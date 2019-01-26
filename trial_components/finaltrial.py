import random
snake_squares = {16: 4, 33: 20, 48: 24, 62: 56, 78: 69, 94: 16}
ladder_squares = {3: 12, 7: 23, 20: 56, 47: 53, 60: 72, 80: 94}
def Roll_dice():
    return random.randint(1,6)
def Setup_Players():
    players=6
    while True:
        try:
            print("How many players are in the game?")
            players = int(input())
            if players > 4 or players < 2:
                print("Must be less than 5 and greater than 1")
            else:
                return players
        except:
            print("Must be a number")
def Player_Names(NumP):
    Names = []
    for i in range(1,NumP+1):
        Names.append(input("What is the name of Player"+str(i)+"?"))
    Names.append("")
    return Names


