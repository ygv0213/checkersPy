from math import pi

import pygame
from checkers.constans import *
from checkers.Board import Board
from checkers.game import Game
from minimax.algorithm import *

FPS = 60

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")
pygame.display.update()


def get_row_col_from_mouse(pos):
    x, y = pos
    return y // SQUARE_SIZE, x // SQUARE_SIZE


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        try:
            if game.turn == WHITE:
                value, new_board = minimax(game.get_board(), 2,  WHITE, game)
                game.ai_move(new_board)
                if game.board.winner() is not None:
                    WIN.fill(game.board.winner())
                    pygame.time.wait(4000)
                    pygame.display.update()
                    run = False
        except AttributeError:
            print("no more moves")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        game.update()
    pygame.quit()


main()
