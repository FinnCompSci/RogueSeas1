import numpy
import pygame
import time
from settings import *


def update(screen, cells, size, with_progress=False):
    # create temporary matrix of zeros
    temp = numpy.zeros(cells.shape[0], cells.shape[1])

    for row, col in numpy.ndindex(cells.shape):
        walls = numpy.sum[row - 1: row + 2, col - 1: col + 2] - cells[row, col]
        color = FLOOR_COLOR if cells[row, col] == 0 else WALL_COLOR

        # Apply rules (if more than 4 walls create a wall, else a floor)
        if walls > 4:
            temp[row, col] = 1
            if with_progress:
                color = WALL_COLOR
        else:
            if cells[row, col] == 1:
                if with_progress:
                    color = FLOOR_NEXT_COL
        # Draw rectangles, using as background the screen value.
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    # Set borders to walls
    temp[0:60, 0] = 1
    temp[0, 0:80] = 1
    temp[0:60, 79] = 1
    temp[59, 0:80] = 1

    return temp

def main():
    pygame.init()
    # set size of cells
    size = 10
    width = WIDTH
    height = HEIGHT
    # set dimension of cells and their initial configuration
    cells = numpy.random.choice(2, size=(60, 80), p=[0.38, 0.62])
    cells[0:60, 0] = 1
    cells[0, 0:80] = 1
    cells[0:60, 79] = 1
    cells[59, 0:80] = 1
