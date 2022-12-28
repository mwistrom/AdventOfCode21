from collections import defaultdict
from collections import deque

def do_it():
    a = []
    i = 0
    with open('aoc_12.txt') as my_file:
        for line in my_file:
            x = list(line[:-1])
            print(x)
            a.append(x)
            if 'S' in x:
                s_i = i
                s_j = x.index('S')
                x[s_j] = 'a'
            if 'E' in x:
                e_i = i
                e_j = x.index('E')
                x[e_j] = 'z'
            i += 1

    h = len(a)
    w = len(a[0])
    print(h, "  ", w, s_i, s_j, e_i, e_j)

    print(a)

    ans = 1000000

    for s_i in range(h):
        for s_j in range(w):
            if a[s_i][s_j] == 'a':
                v = [[False] * w for i in range(h)]
                q = deque([])
                q.append((s_i, s_j, 0))
                v[s_i][s_j] = True

                while len(q) > 0:
                    i, j, steps = q.popleft()
                    # print(i, j, steps)
                    val = a[i][j]
                    if i == e_i and j == e_j:
                        print(steps)
                        ans = min(steps, ans)
                        break
                    if i + 1 < h and not v[i+1][j] and ord(a[i+1][j]) - 1 <= ord(a[i][j]):
                        q.append((i+1, j, steps + 1))
                        v[i+1][j] = True
                    if i - 1 >= 0 and not v[i-1][j] and ord(a[i-1][j])- 1 <= ord(a[i][j]):
                        q.append((i-1, j, steps+1))
                        v[i-1][j] = True

                    if j + 1 < w and not v[i][j+1] and ord(a[i][j+1]) - 1 <= ord(a[i][j]):
                        q.append((i, j+1, steps+1))
                        v[i][j+1] = True
                    if j - 1 >= 0 and not v[i][j-1] and ord(a[i][j-1]) - 1 <= ord(a[i][j]):
                        q.append((i, j-1, steps+1))
                        v[i][j-1] = True
    print(ans)




