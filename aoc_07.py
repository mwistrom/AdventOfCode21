from collections import defaultdict
import  json
from typing import Dict
import copy


def do_it():

    d = {}
    path = []
    with open('aoc_07.txt') as my_file:
        for line in my_file:
            x = line[:-1]
            # print(x)
            if x == "$ cd ..":
                path.pop()
                continue
            if x[:4] == "$ cd":
                dir = x[5:]
                path.append(dir)
                p = '/'.join(path)
                d[p] = ([], [])
                continue
            if x[:4] == "$ ls":
                continue
            if x[:3] == "dir":
                dir = x[4:]
                p = '/'.join(path)
                n = p + '/' + dir
                d[p][0].append(n)
                continue
            l = x.split(" ")
            size = int(l[0])
            p = '/'.join(path)
            d[p][1].append(size)

    print(json.dumps(d, indent=2))

    size = {}
    dfs(d, "/", size)

    ans = 0
    for key, val in size.items():
        print(key, val)
        if val <= 100000:
           ans += val
    print(ans)

    tot = []
    for key, val in size.items():
        print(key, val)
        tot.append(val)
        if val <= 100000:
            ans += val
    tot.sort()
    print("/", size['/'])
    print(70000000 - size['/'])
    tar = 30000000 - (70000000 - size['/'])
    print(tar)

    print(tot)

    for t in tot:
        if t > tar:
            print(t)
            break

def dfs(d, node, size):
    child_size = 0
    for child in d[node][0]:
        child_size += dfs(d, child, size)
    file_size = 0
    for file in d[node][1]:
        file_size += file
    total = child_size + file_size
    size[node] = total
    return total
