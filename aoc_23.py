from collections import defaultdict
import copy


def do_it():
    map_1 = []
    map = []
    count = 0
    padding = 100
    num_elves = 0
    elf_moved = False
    with open('aoc_23.txt') as my_file:
        for line in my_file:
            x = ( list('.' * padding) +
                  list(line[:-1]) +
                  list('.' * padding) )
            y = []
            for z in x:
                if z == '#':
                    y.append(num_elves)
                    num_elves += 1
                else:
                    y.append(z)

            map_1.append(y)

    for i in range(padding):
        map.append(list('.' * (len(map_1[0]))))
    for i in map_1:
        map.append(i)
    for i in range(padding):
        map.append(list('.' * (len(map_1[0]))))
    print_map(map)

    w = len(map[0])
    h = len(map)

    dir_step =  [[(-1, -1), (-1, 0), (-1, 1)],
                [( 1,  -1), ( 1, 0), (1,  1)],
                [(-1, -1), (0, -1), (1, -1)],
                [(-1,  1), (0,  1), (1,  1)]]

    dir_iter = 0

    count = 0
    while True:
        step_map = [ [[] for _ in range(w)] for _ in range(h) ]
        elf_moved = False
        for i, row in enumerate(map):
            for j, elf in enumerate(row):
                if elf == '.':
                    continue
    #            print("Elf: ", elf)
                num_neighbors = 0
                for check_i in [-1, 0, 1]:
                    for check_j in [-1, 0, 1]:
                        ne = map[i+check_i][j+check_j]
                        if ne != '.':
                            num_neighbors += 1
                if num_neighbors == 1:
                    continue

                for e_local_dir in range(4):
                    local_move = True
                    w_iter = (dir_iter + e_local_dir) % 4
                    for step in dir_step[w_iter]:
                        if map[step[0]+i][step[1]+j] != '.':
                            local_move = False
                            break
                    if local_move:
                        step_map_x = dir_step[w_iter][1][0] + i
                        step_map_y = dir_step[w_iter][1][1] + j
    #                    print("step map: ", step_map_x, step_map_y, elf)
                        step_map[step_map_x][step_map_y].append((elf,i,j))
                        break

        # print("Step Map")
        # print_map(step_map)

        num_elves_moved = 0
        for i, row in enumerate(step_map):
            for j, elf in enumerate(row):
                if len(elf) != 1:
                    continue
                e = elf[0]
        #        print("Moving: ", e)
                map[e[1]][e[2]] = '.'
                map[i][j] = e[0]
                elf_moved = True
                num_elves_moved += 1

        # for line in step_map:
        #     print(line)

        dir_iter = (dir_iter + 1) % 4

        count += 1
        print("**********", count, num_elves_moved)

        # print("map at end of move.")
        # print_map(map)
        #
        # min_x = 10000000
        # max_x = -100
        # min_y = 10000000
        # max_y = -100
        #
        # for row, line in enumerate(map):
        #     for col, c in enumerate(line):
        #         if c != '.':
        #             min_x = min(min_x, row)
        #             max_x = max(max_x, row)
        #             min_y = min(min_y, col)
        #             max_y = max(max_y, col)
        # print(min_x, max_x, min_y, max_y)
        # print(num_elves)
        # print( (max_x - min_x + 1) * (max_y - min_y +1 ) - num_elves)

        if not elf_moved:
            print(count)
            break



# 132 = 11 * 12

def print_map(map):
    # for line in map:
    #     for c in line:
    #         try:
    #             print((c%10), end='')
    #         except TypeError:
    #             print(c, end='')
    #     print()
    print("Hi.")