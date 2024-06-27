
"""

Main driver file.
Initializing objects and pygame.
Playing using the engine

"""

import pygame as p
import chessMain

p.init()
WIDTH = HEIGHT = 800
screen = p.display.set_mode((WIDTH, HEIGHT))
screen.fill(p.Color("white"))
clock = p.time.Clock()
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 60
IMAGES = {}


def loadImages():
    pieces = ["bp", "wp", "bR", "bN", "bB", "bQ", "bK", "wR", "wN", "wB", "wQ", "wK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("./images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def main():
    loadImages()
    game = chessMain.Game(p, screen, clock, MAX_FPS, DIMENSION, SQ_SIZE, IMAGES)
    game.main0()


if __name__ == "__main__":
    main()

