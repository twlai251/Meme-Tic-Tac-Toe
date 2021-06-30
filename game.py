import pygame
import sys
import time

xo = "Salad Cat"

winner = None
draw = False

# border lines
width = 400
height = 400

screen = pygame.display.set_mode((width, height+100), 0, 32)
pygame.display.set_caption("Meme Tic Tac Toe")

white = (255, 255, 255)
border_line = (10, 10, 10)

# 3x3 board
board = [[None]*3, [None]*3, [None]*3]


pygame.init()
fps = 30
clock = pygame.time.Clock()


# images
title = pygame.image.load('img/title_screen.png')
x_img = pygame.image.load('img/salad.png')
o_img = pygame.image.load('img/doge_coin.png')

# resizing img
x_img = pygame.transform.scale(x_img, (80, 80))
o_img = pygame.transform.scale(o_img, (80, 80))


def start_game():
    screen.blit(title, (0, 0))
    pygame.display.update()
    time.sleep(2)
    screen.fill(white)

    # vertical lines
    pygame.draw.line(screen, border_line, (width / 3, 0),
                     (width / 3, height), 7)

    pygame.draw.line(screen, border_line, (width / 3*2, 0),
                     (width / 3*2, height), 7)

    # horizontal lines
    pygame.draw.line(screen, border_line, (0, height / 3),
                     (width, height / 3), 7)

    pygame.draw.line(screen, border_line, (0, height / 3*2),
                     (width, height / 3*2), 7)

    draw_status()


def draw_status():
    global draw

    if winner is None:
        message = xo.upper() + "'s Turn"
    else:
        message = winner.upper() + " Won!"

    if draw:
        message = 'Game Draw!'
    # font
    game_font = pygame.font.Font("fonts/RetroGaming.ttf", 20)

    text = game_font.render(message, 1, (255, 255, 255))
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 450))
    screen.blit(text, text_rect)

    pygame.display.update()


def check_win():
    global board, winner, draw

    # checking winning rows
    for row in range(0, 3):
        if ((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            # row won
            winner = board[row][0]
            pygame.draw.line(screen, (250, 0, 0), (0, (row + 1) * height /
                                                   3 - height/6), (width, (row + 1) * height/3 - height/6), 4)
            break

    # checking winning column
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None):
            # row won
            winner = board[0][col]
            pygame.draw.line(screen, (250, 0, 0), ((
                col + 1) * width / 3 - width/6, 0), ((col + 1) * width/3 - width/6, height), 4)
            break

    # check for diagonal winner
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        # diagonally left to right
        winner = board[0][0]
        pygame.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        # diagonally left to right
        winner = board[0][2]
        pygame.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)

    if (all([all(row) for row in board]) and winner is None):
        draw = True

    draw_status()


def draw_xo(row, col):
    global board, xo
    if row == 1:
        posX = 30
    if row == 2:
        posX = width/3 + 30
    if row == 3:
        posX = width/3*2 + 30

    if col == 1:
        posY = 30
    if col == 2:
        posY = height/3 + 30
    if col == 3:
        posY = height/3*2 + 30

    board[row - 1][col-1] = xo
    if (xo == 'Salad Cat'):
        screen.blit(x_img, (posY, posX))
        xo = 'Doge Dog'

    else:
        screen.blit(o_img, (posY, posX))
        xo = 'Salad Cat'

    pygame.display.update()


def userClick():
    x, y = pygame.mouse.get_pos()

    # column 1-3
    if (x < width / 3):
        col = 1
    elif (x < width / 3*2):
        col = 2
    elif (x < width):
        col = 3
    else:
        col = None

    # row 1-3
    if (y < height / 3):
        row = 1
    elif (y < height / 3*2):
        row = 2
    elif (y < height):
        row = 3
    else:
        row = None

    if (row and col and board[row-1][col-1] is None):
        global xo

        draw_xo(row, col)
        check_win()


def reset_game():
    global board, winner, xo, draw, font
    time.sleep(3)
    xo = 'Salad Cat'
    draw = False
    winner = None
    board = [[None]*3, [None]*3, [None]*3]

    start_game()


start_game()
running = True
click = False
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            userClick()
            if(winner or draw):
                reset_game()

    # update
    pygame.display.update()
    clock.tick(fps)
