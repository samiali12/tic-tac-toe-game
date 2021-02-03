# importing pygame library
import pygame

# GUI library
from tkinter import *
from tkinter import messagebox

#to hide the main window
Tk().wm_withdraw()

#initializing game module
pygame.init()

#game window Height and Width
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# set initialize game window with 400 width and 400 height
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Tic Toc Toe Game") # set game window title

# game board 
board = [
    [None,None,None],
    [None,None,None],
    [None,None,None],
]

# mouse x-axis and y-axis position
x = 0
y = 0

# keep track of game 
game_winner = None
game_draw = None

# Keep track of time
CLOCK = pygame.time.Clock()

#FPS
FPS = 30

#computer_can_play
computer_play = None

choice = "X"

#game state 
gameEnd = False

# game font 
font = pygame.font.SysFont("comicsansms", 72)
big_font = pygame.font.SysFont("arial",72)

text = font.render("X", True, (0, 128, 0))

# current choice 
choice = "x"

#draw game broundries
def draw_lines():

    pygame.draw.rect(screen, (150,220,255), ((SCREEN_WIDTH//2)-70,0,5,SCREEN_HEIGHT))
    pygame.draw.rect(screen, (150,220,255), ((SCREEN_WIDTH//2)+70,0,5,SCREEN_HEIGHT))
    pygame.draw.rect(screen, (150,220,255), (0,(SCREEN_HEIGHT//2)-70,SCREEN_HEIGHT,5))
    pygame.draw.rect(screen, (150,220,255), (0,(SCREEN_HEIGHT//2)+70,SCREEN_HEIGHT,5))

def draw_sign(row,col):

    global text,choice 

    text = font.render(choice, True, (0, 128, 0))
    # check for rows
    if row == 1 and col == 1:
        screen.blit(text,(30,10))
    
    elif row == 1 and col == 2:
        screen.blit(text,(180,10))

    elif row == 1 and col == 3:
        screen.blit(text,(320,10))

    # check for column
    if row == 2 and col == 1:
        screen.blit(text,(30,150))
    
    elif row == 2 and col == 2:
        screen.blit(text,(180,150))

    elif row == 2 and col == 3:
        screen.blit(text,(320,150))


    if row == 3 and col == 1:
        screen.blit(text,(30,300))
    
    elif row == 3 and col == 2:
        screen.blit(text,(180,300))

    elif row == 3 and col == 3:
        screen.blit(text,(320,300))

    board[row-1][col-1] = choice
    
    if choice == "x" or choice == "X":
        choice = "O"    
    else:
        choice = "X"
    pygame.display.update()

def user_clicks(x,y):

    row = 0
    col = 0

    if ( (x > 0 and x < 130) ):
        col = 1

    if (x > 132 and x < 260):
        col = 2

    if (x  > 260 and x < 360):
        col = 3

    if (y > 0 and y < 130):
        row = 1

    if (y > 132 and y < 260):
        row = 2

    if (y  > 260 and y < 360):
        row = 3

    if ( row and col and board[row-1][col-1] is None):
        draw_sign(row,col)
        check_winner()



def game_status():
    
    if game_winner == "X":
        confirm = messagebox.askquestion("Player Won ","Do you want continue..")

    if game_winner == "O":
        confirm = messagebox.askquestion("Computer Won ","Do you want continue..")


    if game_draw == True:
        confirm = messagebox.askquestion("Game Draw ","Do you want continue..")


def check_winner():

    global game_draw, game_winner,board

    #checking for rows 
    for row in range(0, 3): 
        if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] is not None)): 
            game_winner = board[row][0] 
            pygame.draw.line(screen, (250, 0, 0), 
                        (0, (row + 1)* SCREEN_HEIGHT / 3 - SCREEN_HEIGHT / 6), 
                        (SCREEN_WIDTH, (row + 1)* SCREEN_HEIGHT / 3 - SCREEN_HEIGHT / 6 ), 4) 
            break

    # checking for winning columns 
    for col in range(0, 3): 
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)): 
            game_winner = board[0][col] 
            pygame.draw.line (screen, (250, 0, 0),
                         ((col + 1)* SCREEN_WIDTH / 3 - SCREEN_WIDTH / 6, 0), 
                          ((col + 1)* SCREEN_WIDTH / 3 - SCREEN_WIDTH / 6, SCREEN_HEIGHT), 4) 
            break

    # check for diagonal winners 
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None): 
          
        # game won diagonally left to right 
        game_winner = board[0][0] 
        pygame.draw.line (screen, (250, 70, 70), (50, 50), (350, 350), 4) 
          
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None): 
          
        # game won diagonally right to left 
        game_winner = board[0][2] 
        pygame.draw.line (screen, (250, 70, 70), (350, 50), (50, 350), 4) 

    if(all([all(row) for row in board]) and game_winner is None ): 
        game_draw = True

    game_status()


# game loop 
while not gameEnd:

    # Did user click close button on window 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #if yes user click gameEnd value = True and loop become end and program continue execution
            gameEnd = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            user_clicks(x,y)


    #screen.fill((255,255,255)) # (255,255,255) represent white color in RGB 

    #draw game boundries line
    draw_lines()
    
    # update game window 
    pygame.display.flip()

    CLOCK.tick(FPS)

pygame.quit()