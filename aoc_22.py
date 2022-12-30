from collections import defaultdict
import copy

# too high 171030
# too high 23454

def do_it():
    m = []
    orig = []
    ord = ""
    with open('aoc_22.txt') as my_file:
        max_w = 0
        for line in my_file:
            l = line[:-1]
            max_w = max(max_w, len(l))
            if l.count('R') > 0 or l.count('L') > 0:
                ord = l
                continue
            if len(l) > 0:
                orig.append(l)

        for l in orig:
            x = (l.ljust(max_w))
            # x = x.replace('#', '.')
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

    d = len(m) // 4
    print(d)

    for o in orders:
        s = o[0]
        nd = o[1]

        next_row, next_col, new_dir = go(m, row, col, d, dir_m, dir)
        # next_row = (row + dir_m[dir][0]) % h
        # next_col = (col + dir_m[dir][1]) % w

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
                exit(33)

            row = next_row
            col = next_col
            dir = new_dir
            m[row][col] = dir_d[dir]
            next_row, next_col, new_dir = go(m, row, col, d, dir_m, dir)
            print("Row:", row, "col:", col, "dir:", dir_d[dir])
            s = s - 1

    print("row:", row + 1, "col:", col + 1, "dir:", dir_d[dir])
    print(1000 * (row + 1) + 4 * (col + 1) + dir)

    for line in m:
        print(''.join(line))

    print(1000 * (row + 1) + 4 * (col + 1) + dir)

def go(m, row, col, l, dir_m, dir):
    # 0  >
    # 1  v
    # 2  <
    # 3  ^
    # 1   Alpha check
    if row == 0 and col <= 2 * l - 1 and dir == 3:
        n_row = col - l + 3 * l
        col = 0
        return n_row, col, 0
    if row >= 3 * l and col == 0 and dir == 2:
        n_row = 0
        col = row - 3 * l + l
        return n_row, col, 1
    # 2 Alpha checked
    if row <= l - 1 and col == l and dir == 2:
        n_row = (l - row - 1) + 2 * l
        col = 0
        return n_row, col, 0
    if 2 * l <= row <= 3 * l - 1 and col == 0 and dir == 2:
        n_row = (l-(row - 2 * l) - 1)
        col = l
        return n_row, col, 0
    # 3 Alpha checked
    if l <= row <= 2 * l - 1 and col == l and dir == 2:
        n_row = 2 * l
        col = row - l
        return n_row, col, 1
    if row == l * 2 and col <= l-1 and dir == 3:
        n_row = col + l
        col = l
        return n_row, col, 0
    # 0  >
    # 1  v
    # 2  <
    # 3  ^
    # 4 Alpha checked
    if row >= 3 * l and col == l - 1 and dir == 0:
        n_row = 3 * l - 1
        col = row - 3 * l + l
        return n_row, col, 3
    if row == 3 * l - 1 and col >= l and dir == 1:
        n_row = col - l + 3 * l
        col = l - 1
        return n_row, col, 2
    # 5 Alpha checked
    if row == l - 1 and col >= 2 * l and dir == 1:
        n_row = col - 2 * l + l
        col = 2 * l - 1
        return n_row, col, 2
    if l <= row <= 2 * l - 1 and col == 2 * l - 1 and dir == 0:
        n_row = l - 1
        col = row - l + 2 * l
        return n_row, col, 3
    # 0  >
    # 1  v
    # 2  <
    # 3  ^
    # 6 Alpha checked
    if row <= l - 1 and col == 3 * l - 1 and dir == 0:
        n_row = (l-row - 1) + 2 * l
        col = 2 * l - 1
        return n_row, col, 2
    if row >= 2 * l and col == 2 * l - 1 and dir == 0:
        n_row = l - (row - 2 * l) - 1
        col = 3 * l - 1
        return n_row, col, 2
    # 7 Alpha checked
    if row == 0 and col >= 2 * l and dir == 3:
        n_row = 4 * l - 1
        col = col - 2 * l
        return n_row, col, 3
    if row == 4 * l - 1 and col <= l - 1 and dir == 1:
        n_row = 0
        col = col + 2 * l
        return n_row, col, 1

    return row + dir_m[dir][0], col + dir_m[dir][1], dir