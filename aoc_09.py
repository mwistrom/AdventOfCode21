from collections import defaultdict
import copy
import re

def do_it():
    map = []
    md = {}
    cmds = []
    with open('aoc_22.txt') as my_file:
        done = False
        for line in my_file:
            if done:
                c = line
                cmds = get_steps(c)
                break
            x = list(line[:-1])
            if len(x) == 0:
                done = True
                continue
            map.append(x)

    print(map)
    print(cmds)

    x = (map[0].index('.'), 0)
    dir = (1,0)
    print( cmds )





def get_steps(s):
    ret = []
    while len(s) > 0:
        print(s)
        i = min(s.index('R'), s.index('L'))

        steps = int(s[:i])
        dir = s[i]
        s = s[(i+1):]
        ret.append((steps, dir))
    return ret