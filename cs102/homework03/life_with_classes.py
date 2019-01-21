import pygame
import random
from copy import deepcopy
from pygame.locals import *


class Cell:

    def __init__(self, row, col, state=False):
        self.row = row
        self.col = col
        self.state = state

    def is_alive(self) -> bool:
        return self.state


class CellList:

    def __init__(self, nrows, ncols, randomize=False):
        self.nrows = nrows
        self.ncols = ncols
        self.grid = []
        if randomize:
            for i1 in range(nrows):
                for i2 in range(ncols):
                    self.grid.append(Cell(i1, i2, bool(random.randint(0, 1))))
        else:
            for i1 in range(nrows):
                for i2 in range(ncols):
                    self.grid.append(Cell(i1, i2))

    def update(self) -> object:
        new_grid = deepcopy(self.grid)
        for cell in self:
            neighbours = self.get_neighbours(cell)
            counter = sum(pop.is_alive() for pop in neighbours)
            if cell.is_alive():
                if counter < 2 or counter > 3:
                    new_grid[cell.row][cell.col].state = False
            else:
                if counter == 3:
                    new_grid[cell.row][cell.col].state = True

        self.grid = new_grid
        return self

    def get_neighbours(self, cell) -> list:
        neighbours = []

        for i1 in range(-1, 2):
            for i2 in range(-1, 2):
                if (i1 or i2) and (0 <= cell.row + i1 < self.nrows) and (0 <= cell.col + i2 < self.ncols):
                    neighbours.append(self.grid[cell.row + i1][cell.col + i2])

        return neighbours

    @classmethod
    def from_file(cls, filename) -> list:
        new_grid = []
        with open(filename) as fi:
            for row, line in enumerate(fi):
                new_grid.append([Cell(row, col, bool(int(state))) for col, state in enumerate(line) if state in '01'])
        cell_list = cls(len(new_grid), len(new_grid[0]), False)
        cell_list.grid = new_grid
        return cell_list

    def __iter__(self) -> list:
        self.row_count = 0
        self.col_count = 0
        return self

    def __next__(self) -> object:
        if self.row_count == self.nrows:
            raise StopIteration

        cell = self.grid[self.row_count][self.col_count]
        self.col_count += 1
        if self.col_count == self.ncols:
            self.col_count = 0
            self.row_count += 1

        return cell

    def __str__(self) -> str:
        str = ""
        for row in range(self.nrows):
            for col in range(self.ncols):
                if self.grid[row][col].is_alive():
                    str += "1 "
                else:
                    str += "0 "
            str += "\n"
        return str


class GameOfLife:

    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Set window size
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Compute count of cells in horizontal and vertical directions
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Speed of the game
        self.speed = speed

    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y), (self.width, y))

    def run(self):
        """Run the game"""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Create cell list
        cell_list = CellList.from_file('grid.txt')

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()

            pygame.display.flip()
            self.draw_cell_list(cell_list)
            cell_list.update()
            clock.tick(self.speed)
        pygame.quit()

    def draw_cell_list(self, cell_list: CellList) -> object:
        """Draw cells to surface"""
        surface = self.screen
        size = self.cell_size

        for cell in cell_list:
            color = pygame.Color('green') if cell.is_alive() else pygame.Color('white')
            rect = [cell.col * size, cell.row * size, size, size]
            pygame.draw.rect(surface, color, rect)

        return self


if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    game.run()
