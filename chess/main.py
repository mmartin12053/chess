from random import gammavariate
import pygame
from chess import *

pygame.init()

WIDTH = HEIGHT = 512

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Chess')

dim = 8

sqsize = HEIGHT // dim

FPS = 60

# board = Gamestate.board
gs = Gamestate

# makemove = Gamestate.makemove()

img = {}

def loadImg():
    peices = ['wp','bp','bK','wK','bQ','wQ','bN','wN','bB','wB','bR','wR']
    for i in peices:
        img[i] = pygame.transform.scale(pygame.image.load(f'./images/{i}.png'), (sqsize, sqsize))
    # print(img)

def drawBoard():
    color = [pygame.Color('white'), pygame.Color('gray')]
    for r in range(dim):
        for c in range(dim):
            burt = color[((r+c) % 2)]
            pygame.draw.rect(WIN, burt, pygame.Rect(c*sqsize, r*sqsize, sqsize, sqsize))

def drawPiece():
    for r in range(dim):
        for c in range(dim):
            piece = Gamestate().board[r][c]
            if piece != '--':
                WIN.blit(img[piece], pygame.Rect(c*sqsize, r*sqsize, sqsize, sqsize))

def drawgame():
    drawBoard()
    drawPiece()
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    WIN.fill(pygame.Color('white'))
    gs = Gamestate()
    # print(gs.board)
    loadImg()

    run = True

    sqSelected = ()
    playerclicks = []
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // sqsize
                row = location[1] // sqsize
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerclicks = []
                else:
                    sqSelected = (row, col)
                    print(str(row) + ' ' + str(col))
                    playerclicks.append(sqSelected)
                if len(playerclicks) == 2:
                    move = Move(playerclicks[0], playerclicks[1], gs.board)
                    print(playerclicks)
                    print(move.getchessnotaion())
                    gs.makemove(move)
                    sqSelected = ()
                    playerclicks = []
                    print(gs.board)
                    print(gs.board[4][4])


        clock.tick(FPS)
        drawgame()

    pygame.quit()

if __name__ == '__main__':
    main()