import sys
invalid = True
#sys.exit()
print("\nWrite 'q' to quit")
board = []
for row in range(6):
    board.append(['-', '-', '-','-', '-', '-', '-']) 

player = 'X'
def changePlayer():
    global player
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'
def place(move):
    global invalid
    global player
    invalid = True
    for row in range(len(board)):
        if board[-1*(row+1)][move-1] == '-':
            board[-1*(row+1)][move-1] = player
            invalid = False
            break
def turn(person=player):
    while True:
        try:
            move = (input('where do you want to go: '))
            
            move = int(move)
            if move > 7 or move < 1:
                print('Your number is too big or too small')
                raise
            
        except:
            if str(move) == 'q':
                print('You have force quitted')
                sys.exit()
            continue
        else:
            break
    place(move)
def checkH():
    global board
    check = []
    for row in range(len(board)):
        for i in range(4):
            for j in range(4):
                check.append(board[row][i+j])
            if '-' not in check:
                if (check[0] == check[1] == check[2] == check[3]):
                    return True
            check = []
    return False

def checkV():
    global board
    check = []
    for col in range(len(board)):
        for i in range(3):
            for j in range(4):
                check.append(board[i+j][col])
            if '-' not in check:
                if (check[0] == check[1] == check[2] == check[3]):
                    return True
            check = []
    return False
def checkD1():
    global board
    check = []
    for row in range(1, 4):
        for col in range(4):
            for j in range(4):
                check.append(board[-1 * (row+j)][col+j])
            if '-' not in check:
                if (check[0] == check[1] == check[2] == check[3]):
                    return True
            check = []
    return False
def checkD2():
    global board
    check = []
    for row in range(3):
        for col in range(4):
            for j in range(4):
                check.append(board[(row+j)][col+j])
            if '-' not in check:
                if (check[0] == check[1] == check[2] == check[3]):
                    return True
            check = []
    return False
def checkWin():
    if checkH() or checkV() or checkD1() or checkD2():
        #print('horizontal win')
        return True
    return False
                
run = True                     
def main():
    global player
    global run
    print('\n'+player + "'s turn")
    print('1 2 3 4 5 6 7')
    for row in board:
        for box in row:
            print(box, end=' ')
        print('')
    
    turn()
    
    if checkWin():
        print('')
        for row in board:
            for box in row:
                print(box, end=' ')
            print('')
        print(player+' wins!!!')
        run = False
    changePlayer()
   
while run:
    
    main()
    if invalid:
        print('\nYou cannot go there!', end='')
        continue
    
    
