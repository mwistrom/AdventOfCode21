from collections import defaultdict
import copy


def do_it():
    m = []
    orig = []
    ord = ""
    with open('aoc_22.txt') as my_file:
        max_w = 0
        for line in my_file:
            l = line[:-1]
            max_w = max(max_w, len(l))
            if l.count('R') > 0:
                ord = l
                continue
            if len(l) > 0:
                orig.append(l)

        for l in orig:
            x = (l.ljust(max_w))
            m.append(list(x))

    for line in m:
        print(''.join(line))
    ord = ord + 'X'
    print(ord)

    orders = []
    while len(ord) > 0:
        temp = ""
        o_list = list(ord)
        for idx,c in enumerate(o_list):
            if c == 'R' or c == 'L' or c == 'X':
                sub = ord[:idx]
                num = int(sub)
                orders.append((num, c))
                temp = ord[idx+1:]

                break
        ord = temp

    print(orders)

    dir_m = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dir_d = [">", "v","<","^"]
    dir = 0

    col = m[0].index('.')
    row = 0

    h = len(m)
    w = len(m[0])

    for o in orders:
        s = o[0]
        nd = o[1]

        next_row = (row + dir_m[dir][0]) % h
        next_col = (col + dir_m[dir][1]) % w

        while True:
            if s == 0 or m[next_row][next_col] == '#':
                if nd == 'X':
                    break
                if nd == 'R':
                    dir = (dir + 1 ) % 4
                    break
                if nd == 'L':
                    dir = (dir - 1) % 4
                    break
            if m[next_row][next_col] == ' ':
                next_row = (next_row + dir_m[dir][0]) % h
                next_col = (next_col + dir_m[dir][1]) % w
                continue

            row = next_row
            col = next_col
            m[row][col] = dir_d[dir]
            next_row = (next_row + dir_m[dir][0]) % h
            next_col = (next_col + dir_m[dir][1]) % w
            print("row:", row, "col:", col)
            s = s - 1

    print("row:", row + 1, "col:", col + 1, dir)
    print( 1000 * (row + 1) + 4 * (col + 1) + dir )

    for line in m:
        print(''.join(line))