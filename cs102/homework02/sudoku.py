''' Assignment number 2 '''
import random


def read_sudoku(puzzle):
    """ to read file sudoku.txt """
    digits = [reader_var for reader_var in open(puzzle).read() if reader_var in '123456789.']
    grid = group(digits, 9)
    return grid


def group(values, n_1=9):
    """
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    temp_arr1 = []
    temp_arr2 = []
    for a_1 in range(len(values)):
        temp_arr1.append(values[a_1])
        if (a_1 + 1) % n_1 == 0:
            temp_arr2.append(temp_arr1)
            temp_arr1 = []
    return temp_arr2


def display(grid):
    ''' This function displays 2D array in grid like format'''
    for i_1 in range(len(grid)):
        for a_1 in range(len(grid[i_1])):
            print(grid[i_1][a_1]),
            if (a_1 + 1) % 3 == 0:
                print('|'),
        print ' '
        if (i_1 + 1) % 3 == 0 and i_1 != 8:
            print "------+-------+--------"


def get_row(values, pos):
    """
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return values[pos[0]]


def get_col(values, pos):
    """
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    temp_1 = []
    for a_1 in range(len(values)):
        temp_1 += values[a_1][pos[1]]

    return temp_1


def get_block(values, pos):
    """
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
        for i_1 in range(3):
            for i_2 in range(3):
                block += values[i_1][i_2]
    elif(pos[0] < 3 and 6 > pos[1] >= 3):
        for i_1 in range(3):
            for i_2 in range(3, 6):
                block += values[i_1][i_2]
    elif(pos[0] < 3 and 9 > pos[1] >= 6):
        for i_1 in range(3):
            for i_2 in range(6, 9):
                block += values[i_1][i_2]
    elif(6 > pos[0] >= 3 and pos[1] < 3):
        for i_1 in range(3, 6):
            for i_2 in range(3):
                block += values[i_1][i_2]
    elif(6 > pos[0] >= 3 and 6 > pos[1] >= 3):
        for i_1 in range(3, 6):
            for i_2 in range(3, 6):
                block += values[i_1][i_2]
    elif(6 > pos[0] >= 3 and 9 > pos[1] >= 6):
        for i_1 in range(3, 6):
            for i_2 in range(6, 9):
                block += values[i_1][i_2]
    elif(9 > pos[0] >= 6 and pos[1] < 3):
        for i_1 in range(6, 9):
            for i_2 in range(3):
                block += values[i_1][i_2]
    elif(9 > pos[0] >= 6 and 6 > pos[1] >= 3):
        for i_1 in range(6, 9):
            for i_2 in range(3, 6):
                block += values[i_1][i_2]
    elif(9 > pos[0] >= 6 and 9 > pos[1] >= 6):
        for i_1 in range(6, 9):
            for i_2 in range(6, 9):
                block += values[i_1][i_2]
    return block


def find_empty_positions(grid):
    """

    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    k_1 = 0
    for i_1 in range(0, len(grid)):
        for i_2 in range(0, len(grid[0])):

            if grid[i_1][i_2] == '.':
                return tuple([i_1, i_2])
            else:
                k_1 += int(grid[i_1][i_2])
    if k_1 == 405:
        return (-1, -1)


def find_possible_values(grid, pos):
    """
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> set(values) == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> set(values) == {'2', '5', '9'}
    True
    """
    p_v1 = []
    p_v = set('123456789') - set(get_block(grid, pos)) - set(get_col(grid, pos)) - set(get_row(grid, pos))
    for a_1 in p_v:
        row = 0
        block = 0
        col = 0
        for t_1 in get_row(grid, pos):
            if t_1 != '.':
                row += int(t_1)
        for t_1 in get_col(grid, pos):
            if t_1 != '.':
                col += int(t_1)
        for t_1 in get_block(grid, pos):
            if t_1 != '.':
                block += int(t_1)
        if(row + int(a_1) <= 45 and col + int(a_1) <= 45 and block + int(a_1) <= 45):
            p_v1.append(a_1)
    return p_v1


def solve(grid):
    """
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """

    pos = find_empty_positions(grid)
    if pos == (-1, -1):
        return grid

    p_v = find_possible_values(grid, pos)
    for a_1 in p_v:
        grid[pos[0]][pos[1]] = a_1
        answer = solve(grid)
        if answer:
            return answer
    grid[pos[0]][pos[1]] = '.'
    return None


def check_solution(solution):
    ''' This function checks whether or not the solution is viable '''
    grid = solution
    l_1 = []
    for i_1 in range(len(grid)):
        for i_2 in range(len(grid[0])):
            l_1 += grid[i_1][i_2]
        if set(l_1) != set('123456789'):
            return False
        if sum([int(i) for i in l_1]) != 45:
            return False
        l_1 = []
    return True


def generate_sudoku(N):
    """
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
    k = 0
    grid = solve([['.']*9 for i in range(9)])
    while k < dots:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid[row][col] != '.':
            grid[row][col] = '.'
            k += 1
    return grid


if __name__ == '__main__':
    for fname in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        display(solution)
