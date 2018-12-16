''' Assignment number 2 '''
import random


def read_sudoku(puzzle) -> list:
    """Прочитать Судоку из указанного файла"""
    digits = [reader_var for reader_var in open(puzzle).read() if reader_var in '123456789.']
    grid = group(digits, 9)
    return grid


def group(values: list, N: int = 9) -> list:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    temp_arr1 = []
    temp_arr2 = []
    for counter in range(len(values)):
        temp_arr1.append(values[counter])
        if (counter + 1) % N == 0:
            temp_arr2.append(temp_arr1)
            temp_arr1 = []
    return temp_arr2


def display(grid: list):
    """Вывод Судоку """
    for counter_1 in range(len(grid)):
        for counter_2 in range(len(grid[counter_1])):
            print(grid[counter_1][counter_2], end=" ")
            if (counter_2 + 1) % 3 == 0:
                print('|', end=" ")
        print(' ')
        if (counter_1 + 1) % 3 == 0 and counter_1 != 8:
            print("------+-------+--------")

    print("")


def get_row(values: list, pos: tuple) -> list:
    """ Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return values[pos[0]]


def get_col(values: list, pos: tuple) -> list:
    """ Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    temp_list = []
    for counter in range(len(values)):
        temp_list += values[counter][pos[1]]

    return temp_list


def get_block(values: int, pos: int) -> list:
    """ Возвращает все значения из квадрата, в который попадает позиция pos

    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    block = []
    if(pos[0] < 3 and pos[1] < 3):
        for counter_row in range(3):
            for counter_col in range(3):
                block += values[counter_row][counter_col]
    elif(pos[0] < 3 and 6 > pos[1] >= 3):
        for counter_row in range(3):
            for counter_col in range(3, 6):
                block += values[counter_row][counter_col]
    elif(pos[0] < 3 and 9 > pos[1] >= 6):
        for counter_row in range(3):
            for counter_col in range(6, 9):
                block += values[counter_row][counter_col]
    elif(6 > pos[0] >= 3 and pos[1] < 3):
        for counter_row in range(3, 6):
            for counter_col in range(3):
                block += values[counter_row][counter_col]
    elif(6 > pos[0] >= 3 and 6 > pos[1] >= 3):
        for counter_row in range(3, 6):
            for counter_col in range(3, 6):
                block += values[counter_row][counter_col]
    elif(6 > pos[0] >= 3 and 9 > pos[1] >= 6):
        for counter_row in range(3, 6):
            for counter_col in range(6, 9):
                block += values[counter_row][counter_col]
    elif(9 > pos[0] >= 6 and pos[1] < 3):
        for counter_row in range(6, 9):
            for counter_col in range(3):
                block += values[counter_row][counter_col]
    elif(9 > pos[0] >= 6 and 6 > pos[1] >= 3):
        for counter_row in range(6, 9):
            for counter_col in range(3, 6):
                block += values[counter_row][counter_col]
    elif(9 > pos[0] >= 6 and 9 > pos[1] >= 6):
        for counter_row in range(6, 9):
            for counter_col in range(6, 9):
                block += values[counter_row][counter_col]
    return block


def find_empty_positions(grid: list) -> tuple:
    """ Найти первую свободную позицию в пазле

    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    counter = 0
    for counter_row in range(0, len(grid)):
        for counter_col in range(0, len(grid[0])):

            if grid[counter_row][counter_col] == '.':
                return tuple([counter_row, counter_col])
            else:
                counter += int(grid[counter_row][counter_col])
    if counter == 405:
        return (-1, -1)


def find_possible_values(grid: int, pos: int) -> list:
    """Вернуть множество возможных значения для указанной позиции

    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> set(values) == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> set(values) == {'2', '5', '9'}
    True
    """
    possible_values = []
    possible_values_temp = set('123456789') - set(get_block(grid, pos)) - set(get_col(grid, pos)) - set(get_row(grid, pos))
    for space in possible_values_temp:
        row = 0
        block = 0
        col = 0
        for num in get_row(grid, pos):
            if num != '.':
                row += int(num)
        for num in get_col(grid, pos):
            if num != '.':
                col += int(num)
        for num in get_block(grid, pos):
            if num != '.':
                block += int(num)
        if(row + int(space) <= 45 and col + int(space) <= 45 and block + int(space) <= 45):
            possible_values.append(space)
    return possible_values


def solve(grid: list) -> list:
    """ Решение пазла, заданного в grid"""
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла

    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """

    pos = find_empty_positions(grid)
    if pos == (-1, -1):
        return grid

    possible_val = find_possible_values(grid, pos)
    for space in possible_val:
        grid[pos[0]][pos[1]] = space
        answer = solve(grid)
        if answer:
            return answer
    grid[pos[0]][pos[1]] = '.'
    return None


def check_solution(solution: list) -> bool:
    ''' Если решение solution верно, то вернуть True, в противном случае False '''
    grid = solution
    list_1 = []
    for counter_1 in range(len(grid)):
        for counter_2 in range(len(grid[0])):
            list_1 += grid[counter_1][counter_2]
        if set(list_1) != set('123456789'):
            return False
        if sum([int(i) for i in list_1]) != 45:
            return False
        list_1 = []
    return True


def generate_sudoku(N: int) -> list:
    """ Генерация судоку заполненного на N элементов

    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    if N > 81:
        dots = 0
    dots = 81 - N
    num_dots = 0
    grid = solve([['.']*9 for i in range(9)])
    while num_dots < dots:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid[row][col] != '.':
            grid[row][col] = '.'
            num_dots += 1
    return grid


if __name__ == '__main__':
    for fname in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        display(solution)
