# def dice(chance):
#     print("".center(9,"_"))
    
#     print("|",end="")
#     if chance == 4 or chance == 6 or chance == 5:
#         print("*   *".center(7),end="")
#     elif chance == 2:
#         print("*".center(7),end="")
#     elif chance == 3:
#         print("*".rjust(7),end="")
#     elif chance == 1:
#         print("".rjust(7),end="")
#     print("|")
    
#     print("|",end="")
#     if chance == 4 or chance == 6:
#         print("*   *".center(7),end="")
#     elif chance == 3 or chance == 5:
#         print("*".center(7),end="")
#     elif chance == 2 or chance == 1:
#         print("*".center(7),end="")
#     print("|")

#     if chance != 4 and chance != 2:
#         print("|",end="")
#         if chance == 5 or chance == 6:
#             print("*   *".center(7),end="")
#         elif chance == 1:
#             print("".center(7),end="")
#         elif chance == 3:
#             print("*".ljust(7),end="")
#         print("|")

#     print("".center(9,"-"))

# dice(1)
# dice(2)
# dice(3)
# dice(4)
# dice(5)
# dice(6)

# def a():
#     return (1,2,3)
# print("this is number %d" %(a()[1]))
    #      /\
    #     //\\           |-----|
    #    ||              |-----|
    #    ||   and        |-----|
    #    ||              |-----|
    # \\//               |-----|
    #  \/

# print(r"""        /\		     |-----|
#        //\\                  |-----|
#        ||                    |-----|
#        || SNAKES     and     |-----| LADDERS
#        ||                    |-----|
#     \\//                     |-----|
#      \/	                     |-----|
# """)
# import random,termcolor as tc

# def assign_color(players):
#     """ assigns different colors to different player's beeds
#         players: dictionary(name -> [beed,position])
#         returns: dictionary(beed -> color)"""
#     cl = ["red","green","yellow","cyan","magenta"]
#     random.shuffle(cl)
#     colors = {}
#     counter = 0
#     for m in players.keys():
#         colors[players[m][0]] = cl[counter]
#         counter += 1
#     return colors

# def prepare_board():
#     """ make board in form of nested lists 
#         returns: nested lists  """
 
#     board = []
#     temp = []
#     for i in range(100,0,-1):
#         temp.append(str(i))
#         if (i-1)%10 == 0:
#             board.append(temp)
#             temp = []
#     for j in range(len(board)):
#         if j%2:
#             board[j].reverse()
#     return board

# def display_board(players,board,colors):
#     """ prints the board in a pretty manner
#         players: dictionary(name -> [beed,position])
#         board: list of numbers(use prepare_board() function
#         returns: None
#         """
#     snakes_blocks = {16: 4, 33: 20, 48: 24, 62: 56, 78: 69, 94: 16,99: 9}
#     ladder_blocks = {3: 12, 7: 23, 20: 56, 47: 53, 60: 72, 80: 94}
#     # creates a dictionary (position -> (beed)) list is used due possibility of many beeds at a position                              
#     beed_place = {}
#     for i in players:
#         if beed_place.get(players[i][1]):
#             beed_place[players[i][1]].append(players[i][0])
#         else:
#             beed_place[players[i][1]] = list(players[i][0])
    

#     print("".center(131,"-"))
#     for i in board:
#         print("|",end="")
#         for j in i:
#             if beed_place.get(int(j)):
#                 print(j.rjust(7),end="")
#                 for k in beed_place.get(int(j)):
#                     print(tc.colored(k,colors[k],None,["bold"]),end="")
#                 print("".ljust(5-len(beed_place.get(int(j)))),end="")
#             else:
#                 if snakes_blocks.get(int(j)):
#                     print(j.rjust(7),end="")
#                     print(tc.colored("∫","white",None,["blink","bold"]),end="")
#                     print(" "*4,end= "")
#                 elif ladder_blocks.get(int(j)):
#                     print(j.rjust(7),end="")
#                     print(tc.colored("†","yellow",None,["blink","bold"]),end="")
#                     print(" "*4,end= "")
#                 else:
#                     print(j.center(12),end= "")
#             print("|",end="")
#         print()
#         print("".center(131,"-"))   

# dic = {"shashank":["*",1],
#        "arpit":["$",1],
#        "akshat":["&",1],
#        "kishlay":["#",1]
#        }  

# display_board(dic,prepare_board(),assign_color(dic))

# print("hello")
# print("\n"*47)
# print("shashank")
# print("\n"*47,"\b"*47*130)
# input()
import snakes
snakes.dice(3)