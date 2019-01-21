"""The Game of Life """
import random
import pygame
from pygame.locals import *


class GameOfLife:
    '''Class which generates game of life '''
    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self):
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.width, y))

    def run(self):
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        grid = self.cell_list(True)
        self.draw_cell_list(grid)
        # PUT YOUR CODE HERE

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()
            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            # PUT YOUR CODE HERE
            pygame.display.flip()
            grid = self.update_cell_list(grid)
            self.draw_cell_list(grid)
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize=False) -> list:
        """ Создание списка клеток.

        :param randomize: Если True, то создается список клеток, где
        каждая клетка равновероятно может быть живой (1) или мертвой (0).
        :return: Список клеток, представленный в виде матрицы
        """
        clist = []
        # PUT YOUR CODE HERE
        for row in range(self.cell_height):
            clist.append([])
            for col in range(self.cell_width):
                if randomize:
                    clist[row].append(random.randint(0, 1))
                else:
                    clist[row].append(0)
        return clist

    def draw_cell_list(self, clist):
        """ Отображение списка клеток

        :param rects: Список клеток для отрисовки, представленный в виде матрицы
        """
        size = self.cell_size
        for row in range(len(clist)):
            for col in range(len(clist[0])):
                color = pygame.Color('white') if clist[row][col] == 0 else pygame.Color('green')
                rect = [col*size, row*size, size, size]
                pygame.draw.rect(self.screen, color, rect)

    def get_neighbours(self, cell, cell_list) -> list:
        """ Вернуть список соседей для указанной ячейки

        :param cell: Позиция ячейки в сетке, задается кортежем вида (row, col)
        :return: Одномерный список ячеек, смежных к ячейке cell
        """
        neighbours = []
        # PUT YOUR CODE HERE
        row = cell[0]
        col = cell[1]
        if (row != 0) and (col != 0):
            neighbours.append(cell_list[row - 1][col - 1])
        if row != 0:
            neighbours.append(cell_list[row - 1][col])
        if (row != 0) and (col != (self.cell_width - 1)):
            neighbours.append(cell_list[row - 1][col + 1])
        if col != (self.cell_width - 1):
            neighbours.append(cell_list[row][col + 1])
        if (row != (self.cell_height - 1)) and (col != (self.cell_width - 1)):
            neighbours.append(cell_list[row + 1][col + 1])
        if row != (self.cell_height - 1):
            neighbours.append(cell_list[row + 1][col])
        if (row != (self.cell_height - 1)) and (col != 0):
            neighbours.append(cell_list[row + 1][col - 1])
        if col != 0:
            neighbours.append(cell_list[row][col - 1])


        return neighbours

    def get_copy(self, clist) -> list:
        ''' Just copies one list to another '''
        clist_new = []
        for row in range(len(clist)):
            clist_new.append(clist[row].copy())

        return clist_new

    def update_cell_list(self, cell_list) -> list:
        """ Выполнить один шаг игры.

        Обновление всех ячеек происходит одновременно. Функция возвращает
        новое игровое поле.

        :param cell_list: Игровое поле, представленное в виде матрицы
        :return: Обновленное игровое поле
        """
        new_clist = self.get_copy(cell_list)
        # PUT YOUR CODE HERE
        for row in range(len(cell_list)):
            for col in range(len(cell_list[0])):
                neighbours = self.get_neighbours((row, col), cell_list)
                if cell_list[row][col] == 1:
                    if((neighbours.count(1) > 3) or (neighbours.count(1) < 2)):
                        new_clist[row][col] = 0
                else:
                    if neighbours.count(1) == 3:
                        new_clist[row][col] = 1

        return new_clist


if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    game.run()
