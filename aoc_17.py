import copy
from collections import defaultdict
import json
from collections import deque

def do_it():
    lines = []
    h_list = []
    with open('aoc_17.txt') as my_file:
        for line in my_file:
            lines.append(line[:-1])
    a = []
    b = [0 for _ in range(100000)]
    b[1] = 1
    wind = lines[0]
    print( len(wind))

    check_down = [[(-1,0),(-1,1),(-1,2),(-1,3)],
                  [(0,0), (-1,1), (0,2)],
                  [(-1,0),(-1,1),(-1,2)],
                  [(-1,0)],
                  [(-1,0),(-1,1)]]

    check_right = [[(0,4)],
                   [(0,2),(1,3),(2,2)],
                   [(0,3),(1,3),(2,3)],
                   [(0,1),(1,1),(2,1),(3,1)],
                   [(0,2),(1,2)]]

    check_left = [[(0,-1)],
                  [(0,0),(1,-1),(2,0)],
                  [(0, -1), (1, 1), (2,1)],
                  [(0,-1), (1,-1),(2,-1),(3,-1)],
                  [(0,-1), (1,-1)]]
    sh_array = [
        [list("@@@@")],
        [list(".@."),
         list("@@@"),
         list(".@.")],
        [list("@@@"),
         list("..@"),
         list("..@")
         ],
        [list("@"),
         list("@"),
         list("@"),
         list("@")
         ],
        [list("@@"),
         list("@@")
        ]
    ]

    for i in range(5):
        print(sh_array[i])

    bo = deque()
    bo.append(list("#########"))
    for i in range(100200):
        bo.append(list("#       #"))
    h = 0
    preh = 0
    sh_idx = 0
    wind_idx = 0

    i = -1
    while i < 8000:
        i = i + 1
        shape = sh_array[sh_idx]
        row = h + 3 + 1
        col = 3

        while True:
            match wind[wind_idx]:
                case ">":
                    col = move_right(bo, row, col, check_right[sh_idx])
                case "<":
                    col = move_left(bo, row, col, check_left[sh_idx])

            wind_idx = (wind_idx + 1 ) % len(wind)
            is_attached, row = move_down(bo, row, col, check_down[sh_idx])
            if is_attached:
                add_shape(shape, bo, row , col)
                break

        h = max(h, row + len(shape) - 1)
        sh_idx = (sh_idx + 1) % 5

        print(h, h-preh)
        a.append(str(h-preh))
        b[i + 1] = b[i] + h - preh
        preh = h
    print(''.join(a))
    print(b)
    dh = b[44+70] - b[44]
    print(b[44], b[44+70], dh)
    num_shapes = 1000000000000
    start = 1239
    period = 1710
    repeating_section = num_shapes - start
    print(repeating_section)
    num_of_res = repeating_section // period
    print(num_of_res)
    last_bit = num_shapes - start - (num_of_res * period)
    print(last_bit)
    final_height = b[start] + (num_of_res * (b[start + period] - b[start])) + b[start+last_bit]-b[start]

    print(final_height)
    print(1514285714288)


def move_down(bo, row, col, check):
    for point in check:
        if bo[row + point[0]][col + point[1]] == "#":
            return True, row
    return False, row - 1

def move_right(bo, row, col, check):
    for point in check:
        if bo[row + point[0]][col + point[1]] == "#":
            return col
    return col+1

def move_left(bo, row, col, check):
    for point in check:
        if bo[row + point[0]][col + point[1]] == "#":
            return col
    return col-1


def add_shape(shape, bo, srow, scol):
    for i, row in enumerate(shape):
        for j, v in enumerate(row):
            if v == '@':
                bo[i+srow][j+scol] = '#'


def print_board( bo, h, shape, srow, scol):
    b = copy.deepcopy(bo)

    for i, row in enumerate(shape):
        for j, v in enumerate(row):
            if v == '@':
                b[i+srow][j+scol] = '@'

    for row_idx in range(h+10,-1,-1):
        for col_idx in range(0,9):
            v = b[row_idx][col_idx]
            print(v, end='')
        print()
    print()