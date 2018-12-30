import termcolor as tc
def show_board(board):
    """ prints the board in pretty way 
        board: nested list
        returns: None     """
    import termcolor
    print("".center(111,"-"))
    for i in board:
        print("|",end="")
        for j in i:
            if "*" in j:
                print(termcolor.colored(j.center(10),"red"),end="")
            else:
                print(j.center(10),end="")
            print("|",end="")
        print()
        print("".center(111,"-"))   
def make_board(players):

    """ creates a snakes and ladders board interface given the number
        of players and their beeds
        players: dictionary (name -> [beed,number])
        returns: nested list """
    c = {}
    for i in players.keys():
        c[players[i][1]] = players[i][0]
    a = []
    b = []
    for i in range(100,0,-1):
        if c.get(i):
            b.append(str(i)+c[i])
        else:
            b.append(str(i))
        if (i-1)%10 == 0:
            a.append(b)
            b = []
    for j in range(len(a)):
        if j%2:
            a[j].reverse()
    return a
dic = {"shashank":["*",1],
       "arpit":["$",5],
       "akshat":["&",29]
       }

show_board(make_board(dic))
