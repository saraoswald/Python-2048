import random

board = [[0 for i in range(4)] for i in range(4)] 

def printboard():
     lnbreak = " ------------------"
     print(lnbreak)
     for i in range(4):
          print('|%4s|%4s|%4s|%4s|' % (str(board[i][0]),str(board[i][1]),str(board[i][2]),str(board[i][3])))
          print(lnbreak)

def getnum():
     #generate number, where
     #2 is more likely than 4
     n = (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4)
     num = n[random.randint(0,(len(n)-1))]
     return(num)

def placenum(point):
     num = getnum()
     a = False
     #up
     if point == "i":
          for i in range(3,-1,-1):
               for j in range(0,4):
                    if board[i][j] == 0:
                         board[i][j] = num
                         a = True
                         break
               if a == True:
                    break
     #down
     if point == "k":
          for i in range(0,4):
               for j in range(0,4):
                    if board[i][j] == 0:
                         board[i][j] = num
                         a = True
                         break
               if a == True:
                    break
     #left
     if point == "j":
          for i in range(3,-1,-1):
               for j in range(0,4):
                    if board[j][i] == 0:
                         board[j][i] = num
                         a = True
                         break
               if a == True:
                    break
     #right
     if point == "l":
          for i in range(0,4):
               for j in range(0,4):
                    if board[j][i] == 0:
                         board[j][i] = num
                         a = True
                         break
               if a == True:
                    break

def add(point):
     #up
     count = 0
     if point == "i":
          for i in range(0,4):
               line = []

               #push them up
               for r in range(0,4):
                    if board[r][i] != 0:
                         line.append(board[r][i])
               if len(line) < 4:
                    for z in range(len(line), 4):
                         line.append(0)
               for g in range(0,4):
                    board[g][i] = line[g]

               #add
               for j in range(0,4):
                    
                    try:
                         if board[j][i] == board[j+1][i]:
                              board[j][i] += board[j+1][i]
                              board[j+1][i] = 0                            
                    except IndexError:
                         break
          for i in range(0,4):
               line = []
               #push them up
               for r in range(0,4):
                    if board[r][i] != 0:
                         line.append(board[r][i])
               if len(line) < 4:
                    for z in range(len(line), 4):
                         line.append(0)
               for g in range(0,4):
                    board[g][i] = line[g]
     #down
     if point == "k":
          for i in range(0,4):
               line = []

               #push them down
               for r in range(0,4):
                    if board[r][i] != 0:
                         line.append(board[r][i])
               if len(line) < 4:
                    for z in range(0, (4-len(line))):
                         line.insert(0,0)

               #put new order on board
               for g in range(0,4):
                    board[g][i] = line[g]
               
               #add matching numbers
               for j in range(3,-1,-1):
                    try:
                         if board[j][i] == board[j-1][i]:
                              board[j][i] += board[j-1][i]
                              board[j-1][i] = 0                            
                    except IndexError:
                         break
          for i in range(0,4):
               line = []
               #push them down
               for r in range(0,4):
                    if board[r][i] != 0:
                         line.append(board[r][i])
               if len(line) < 4:
                    for z in range(0, (4-len(line))):
                         line.insert(0,0)

               #put new order on board
               for g in range(0,4):
                    board[g][i] = line[g]
     #left
     if point == "j":
          for i in range(0,4):
               line = []

               #push them left
               for r in range(0,4):
                    if board[i][r] != 0:
                         line.append(board[i][r])
               if len(line) < 4:
                    for z in range(len(line), 4):
                         line.append(0)

               #put new order on board
               for g in range(0,4):
                    board[i][g] = line[g]
               
               #add matching numbers
               for j in range(0,4):
                    try:
                         if board[i][j] == board[i][j+1]:
                              board[i][j] += board[i][j+1]
                              board[i][j+1] = 0
                         elif (board[i][j] == 0) and (board[i][j+1] != 0):                              
                              board[i][j] = board[i][j+1]
                              board[i][j+1] = 0                             
                    except IndexError:
                         break
     #right
     if point == "l":
          for i in range(0,4):
               line = []

               #push them right
               for r in range(0,4):
                    if board[i][r] != 0:
                         line.append(board[i][r])
               if len(line) < 4:
                    for z in range(0, (4-len(line))):
                         line.insert(0,0)

               #put new order on board
               for g in range(0,4):
                    board[i][g] = line[g]
               
               #add matching numbers
               for j in range(3,-1,-1):
                    try:
                         if board[i][j] == board[i][j-1]:
                              board[i][j] += board[i][j-1]
                              board[i][j-1] = 0                            
                    except IndexError:
                         break
          for i in range(0,4):
               line = []
               #push them down
               for r in range(0,4):
                    if board[i][r] != 0:
                         line.append(board[i][r])
               if len(line) < 4:
                    for z in range(0, (4-len(line))):
                         line.insert(0,0)

               #put new order on board
               for g in range(0,4):
                    board[i][g] = line[g]



def play():
     test = True
     point = "i"
     placenum(point)
     printboard()
     point = input("Welcome to 2048! Use 'i', 'j', 'k', and 'l' for up, left, down, and right, respectively.\n>")
     add(point)
     placenum(point)
     while test:
          printboard()
          point = input("Type up ('i'), left ('j'), down ('k'), or right ('l').\n>")
          add(point)
          placenum(point)

play()
