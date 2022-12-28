from collections import defaultdict
import copy
import ast
from functools import cmp_to_key


def temp(i1, i2):
    if i1 < i2:
        return 1
    return -1

def do_it():
    # aa = [3, 6, 2, 4, 9, 4, 7, 12, 5, 7]
    # a = sorted(aa, key=cmp_to_key(lambda i1, i2: temp(i1, i2)))
    #
    # print(aa)
    # print(a)
    # exit(0)

    in_lines = []
    lines = []
    with open('aoc_13.txt') as my_file:
        for line in my_file:
            if len(line) <= 1:
                continue
            in_lines.append(line[:-1])

    total = 0
    count = 0
    while count < len(in_lines):
        x = in_lines[count]
        y = in_lines[count + 1]
        count += 2

        # print(x)
        # print(y)

        x = ast.literal_eval(x)
        y = ast.literal_eval(y)
        lines.append(x)
        lines.append(y)

    ans = sorted(lines, key=cmp_to_key(lambda item1, item2: -com(item1, item2)))

    for line in ans:
        print(line)

    index1 = ans.index([[2]]) + 1
    index2 = ans.index([[6]]) + 1
    print(index1, index2, index1 * index2)



def com(x, y):
    if isinstance(x, int) and isinstance(y,int):
        if x == y:
            return 0
        elif x < y:
            return 1
        return -1

    if isinstance(x,int):
        x = [x]
    if isinstance(y,int):
        y = [y]

    i = 0

    while True:
        if i >= len(x) or i >= len(y):
            if len(x) == len(y):
                return 0
            elif len(x) < len(y):
                return 1
            return -1
        x_local = x[i]
        y_local = y[i]

        # print("in: ", x)
        # print("in: ", y)
        # print( "local :", x_local)
        # print( "local :", y_local)

        res = com(x[i], y[i])
        if res != 0:
            return res
        i += 1





      # print(x)
        # print(y)

    #     res = com(x, y)
    #     if res == 1:
    #         print(count // 2)
    #         total += (count //2)
    #
    # print(total)
    #
    # for line in lines:
    #     print(line)
    #
    # print(len(lines))
