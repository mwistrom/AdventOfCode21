from collections import defaultdict
import copy
import collections


def do_it():
    map = {}
    map[0] = []
    with open('aoc_24.txt') as my_file:
        for line in my_file:
            l = line[1:-2]
            if l[4] == '#':
                continue
            x = [ [] if y == '.' else [y] for y in l]
            map[0].append(list(l))

    gen_map(map, 1000)

    h = len(map[0])
    w = len(map[0][0])

    # p_m(map, 0)
    # p_m(map, 1)
    # p_m(map, 2)

    hist = set()

    q = collections.deque()
    #q.append((-1,0,0))
    #q.append((h, w-1, 283))
    q.append((-1,0,591))

    ds = [(1,0), (0,1),(-1,0),(0,-1),(0,0)]

    while len(q) > 0:
        node = q.popleft()
        r = node[0]
        c = node[1]
        t = node[2]
#        p_m(map, t, r, c)
        print(t)
        if r == -1:
            tup = (-1, 0, t + 1)
            if not tup in hist:
                hist.add(tup)
                q.append(tup)
                if len( map[t+1][0][0] ) == 0:
                    tup = (0, 0, t + 1)
                    if not tup in hist:
                        hist.add(tup)
                        q.append(tup)
            continue
        if r == h:
            tup = (h, w-1, t + 1)
            if not tup in hist:
                hist.add(tup)
                q.append(tup)
                if len(map[t + 1][0][0]) == 0:
                    tup = (h-1, w-1, t + 1)
                    if not tup in hist:
                        hist.add(tup)
                        q.append(tup)
            continue
        if r == h - 1 and c == w - 1:
            print("Time DONE: ", t+ 1)
            break
        # if r == 0 and c == 0:
        #     print("Time DONE: ", t+ 1)
        #     break
        for d in ds:
            row = r + d[0]
            col = c + d[1]
            if row < 0 or col < 0 or row >= h or col >= w:
                continue
            if len( map[t+1][row][col]) == 0:
                tup = (row, col, t+1)
                if not tup in hist:
                    hist.add(tup)
                    q.append(tup)

def gen_map(m, end):
    h = len(m[0])
    w = len(m[0][0])
    for time in range(end):
        m_next = [ [ [] for _ in range(w)] for _ in range(h)]
        for row_i, row in enumerate(m[time]):
            for col_i, elemts in enumerate(row):
                for v in elemts:
                    match v:
                        case '>':
                            m_next[row_i][(col_i + 1) % w].append('>')
                        case '<':
                            m_next[row_i][(col_i - 1) % w].append('<')
                        case '^':
                            m_next[(row_i - 1) % h][(col_i)].append('^')
                        case 'v':
                            m_next[(row_i + 1) % h][(col_i)].append('v')
        m[time+1] = m_next

def p_m(m, t, r_e, c_e):
    print("r c", r_e, c_e, "     Time: ", t)
    for i, line in enumerate(m[t]):
        for j, c in enumerate(line):
            if len(c) == 0:
                if i == r_e and j == c_e:
                    print("E", end='')
                else:
                    print('.', end='')
                continue
            if len(c) == 1:
                print(c[0], end='')
                continue
            print(len(c), end='')
        print()



