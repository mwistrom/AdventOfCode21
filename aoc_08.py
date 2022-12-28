from collections import defaultdict

def do_it():

    lines = []
    with open('aoc_08.txt') as my_file:
        for line in my_file:
            x = list(line[:-1])
            print(x)
            y = list(map(int, x))
            lines.append(y)

    h = len(lines)
    w = len(lines[0])
    print(h, "  ", w)

    v = [ [False] * w for _ in range(h)]

#    print (v)
    print (lines)

    o = 0
    ans = 0
    cur = 0
    for i1 in range(h):
        for j1 in range(w):
            cur = 0

            o = 0
            t = -1
            for i in range(i1+1,h):
                if lines[i][j1] >= lines[i1][j1]:
                    o += 1
                    break
                # if lines[i][j1] >= t:
                #     t = lines[i][j1]
                o += 1
            print("down: ", o)
            cur = o

            o = 0
            t = -1
            for i in range(i1-1, -1, -1):
                if lines[i][j1] >= lines[i1][j1]:
                    o += 1
                    break
                # if lines[i][j1] >= t:
                #     t = lines[i][j1]
                o += 1
            print("up", o)
            cur = cur * o

            o = 0
            t = -1
            for j in range(j1+1,w):
                if lines[i1][j] >= lines[i1][j1]:
                    o += 1
                    break
                # if lines[i1][j] >= t:
                #     t = lines[i1][j]
                o += 1
            print("right", o)
            cur = cur * o

            o = 0
            t = -1
            for j in range(j1-1,-1,-1):
                if lines[i1][j] >= lines[i1][j1]:
                    o+=1
                    break
                # if lines[i1][j] >= t:
                #     t = lines[i1][j]
                o += 1
            print("left", o)
            cur = cur * o

            ans = max(ans, cur)
            print(i1, j1, cur)

    print(ans)

    #for line in lines: