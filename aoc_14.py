from collections import defaultdict
import copy
import ast
from functools import cmp_to_key


def do_it():
    min_x = 10000000
    max_x = -min_x
    max_y = max_x

    map = [['.' for _ in range(1000)] for _ in range(200)]
    # for line in map:
    #     print(''.join(line))

    with open('aoc_14.txt') as my_file:
        for line in my_file:
            points = line[:-1].split(' -> ')
            p0_split = points[0].split(',')
            row_0, col_0 = int(p0_split[0]), int(p0_split[1])
            max_y = max(max_y, col_0)
            # print(row_0, col_0)
            for idx, point in enumerate(points):
                if idx == 0:
                    continue
                p = point.split(',')
                row_1, col_1 = int(p[0]), int(p[1])
                max_y = max(max_y, col_1)
                if row_1 == row_0:
                    for col in range( min(col_1, col_0), max(col_1,col_0)+1):
                        map[col][row_0] = "#"
                else:
                    for row in range( min(row_1, row_0), max(row_1,row_0)+1):
                        map[col_0][row] = "#"
                row_0 = row_1
                col_0 = col_1

    print( max_y)
    # for line in map:
    #     print(''.join(line))

    r, c = 0, 500
    sand = 0
    while r < 199:
        if map[0][500] != '.':
            break
        if map[r+1][c] == '.':
            r += 1
            continue
        if map[r+1][c-1] == '.':
            r += 1
            c -= 1
            continue
        if map[r+1][c+1] == '.':
            r += 1
            c += 1
            continue
        map[r][c] = 'o'
        r, c = 0, 500
        sand += 1

    for lines in map:
        print(''.join(lines))
    print(sand)