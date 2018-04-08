import numpy as np

#from cell import Cell
from grid import Grid
from world import World


START_DATE = (2000, 1)
GRID_DIMS = np.array((100, 100))


def main():
    world = World(START_DATE[0], START_DATE[1])
    print(world)
    grid = Grid(GRID_DIMS)
    print(grid)


if __name__ == '__main__':
    main()
