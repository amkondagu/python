from sys import exit
print("\nWrite 'quit' to quit")
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
    global player
    for row in range(len(board)):
        if board[-1*(row+1)][move-1] == '-':
            board[-1*(row+1)][move-1] = player
            break
def turn(person=player):
    while True:
        try:
            move = int(input('where do you want to go: '))
            if move >= 7 or move <= 1:
                raise
        except:
            if str(move) == 'quit':
                exit()
            continue
        else:
            break
    place(move)
while True:
    print(player + "'s turn")
    print('1 2 3 4 5 6 7')
    for row in board:
        for box in row:
            print(box, end=' ')
        print('')
    turn()
    changePlayer()
