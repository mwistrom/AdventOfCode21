from collections import defaultdict
from collections import deque

def do_it():
    m = set()
    lc = 0

    x_min = 5
    x_max = 5
    y_min = 5
    y_max = 5
    z_min = 5
    z_max = 5

    with open('aoc_18.txt') as my_file:
        for line in my_file:
            l = line[:-1].split(',')
            x = int(l[0])
            y = int(l[1])
            z = int(l[2])


            x_min = min(x_min, x)
            x_max = max(x_max, x)
            y_min = min(y_min, y)
            y_max = max(y_max, y)
            z_min = min(z_min, z)
            z_max = max(z_max, z)



            m.add((x,y,z))
            lc += 1

    print(x_min, x_max, y_min, y_max, z_min, z_max)

    count = 0
    for p in m:
        if (p[0]+1, p[1], p[2]) in m:
            count += 1
        if (p[0]-1, p[1], p[2]) in m:
            count += 1
        if (p[0], p[1]+1, p[2]) in m:
            count += 1
        if (p[0], p[1]-1, p[2]) in m:
            count += 1
        if (p[0], p[1], p[2]+1) in m:
            count += 1
        if (p[0], p[1], p[2]-1) in m:
            count += 1

    print(count)
    print(len(m), lc)
    print(6 * len(m) - count)

    q = deque()
    q.append((0,0,0))

    dir = [[0,0,-1],
           [0,0,1],
           [0,-1,0],
           [0,1,0],
           [-1,0,0],
           [1,0,0]]

    visited = set()
    visited.add((-1,-1,-1))

    while len(q) > 0:
        node = q.popleft()
        for d in dir:
            x = node[0]+d[0]
            y = node[1]+d[1]
            z = node[2]+d[2]
            if x < 0 or x > 25 or y < 0 or y > 25 or z < 0 or z > 25:
                continue
            if (x,y,z) in visited or (x,y,z) in m:
                continue
            visited.add((x,y,z))
            q.append((x,y,z))

    print(len(visited))

    for i in range(25):
        for j in range(25):
            for k in range(25):
                if (i,j,k) in visited:
                    continue
                m.add((i,j,k))

    count = 0
    for p in m:
        if (p[0]+1, p[1], p[2]) in m:
            count += 1
        if (p[0]-1, p[1], p[2]) in m:
            count += 1
        if (p[0], p[1]+1, p[2]) in m:
            count += 1
        if (p[0], p[1]-1, p[2]) in m:
            count += 1
        if (p[0], p[1], p[2]+1) in m:
            count += 1
        if (p[0], p[1], p[2]-1) in m:
            count += 1

    print(count)
    print(len(m), lc)
    print(6 * len(m) - count)







