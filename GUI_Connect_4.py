import pygame
pygame.init()
squareSize = 100
width = 7*squareSize
height = 6*squareSize+squareSize
size = (width, height)
window = pygame.display.set_mode(size)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
pygame.draw.rect(window, blue, (0,squareSize,width,height-squareSize))
pygame.display.set_caption('Connect 4')

import sys

#invalid = True
#sys.exit()
#print("\nWrite 'q' to quit")
board = []
for row in range(6):
    board.append(['-', '-', '-','-', '-', '-', '-'])

def drawBoard(bo):
    for row in range(len(bo)):
        for sqr in range(len(bo[row])):
            if bo[row][sqr] == '-':
                color = black
            elif bo[row][sqr] == 'X':
                color = red
            elif bo[row][sqr] == 'O':
                color = yellow
            else:
                sys.exit()
            x = int(squareSize/2 + sqr*squareSize)
            y = int(squareSize/2 + squareSize*row + squareSize)
            #print(x)
            pygame.draw.circle(window, color, (x, y), int(squareSize*0.4))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

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
def turn(person):
    global pos
    move = pos[0] // squareSize + 1
    
    '''
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
                pygame.quit()
                sys.exit()
            continue
        else:
            break

            '''
    place(move)
    changePlayer()
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
'''
def main():
    global player
    global run
    
    print('\n'+player + "'s turn")
    print('1 2 3 4 5 6 7')
    for row in board:
        for box in row:
            print(box, end=' ')
        print('')
        
    
    #turn(player)
    
    if checkWin():
        print('')
        for row in board:
            for box in row:
                print(box, end=' ')
            print('')
        print(player+' wins!!!')
        run = False
    changePlayer()
'''
game_over = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            turn(player)
            #print(pos)
    drawBoard(board)
    pygame.display.update()
    if checkWin():
        '''
        print('')
        for row in board:
            for box in row:
                print(box, end=' ')
            print('')
            '''
        if player == 'X':
            player = 'Yellow'
        elif player == 'O':
            player = 'Red'
        font = pygame.font.Font('freesansbold.ttf', 70)
        text = font.render(player+' wins!!', True, white, black)
        textRect = text.get_rect()
        textRect.center = (width//2, squareSize//2)
        window.blit(text, textRect)
        pygame.display.update()
 #       pygame.time.wait(3000)

        print(player+' wins!!!')
        run = False
        game_over = True
    #if invalid:       
 #       print('\nYou cannot go there!', end='')
        #continue
while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False
pygame.quit()
