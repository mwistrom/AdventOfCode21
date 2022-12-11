# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_x(x):
    for row in x:
        for c in row:
            print(c, end='')
        print()
    print()
    print()

def do_25():
    x = []
    with open('c:\\users\\noonan\\two_five.txt') as my_file:
        for line in my_file:
            a = list(line[:-1])
            x.append(a)

    h = len(x)
    w = len(x[0])

    print(h, "  ", w)

    change = True
    c = 0
    while change:
        print(c)
        # print_x(x)
        change = False
        for i in range(h):
            n = ['.'] * w
            for j in range(w):
                # print(i, " ", j)
                if x[i][j % w] == 'v':
                    n[j % w] = 'v'
                    continue
                if x[i][j % w] == '>' and x[i][(j+1) % w] == '.':
                    n[(j+1) % w] = '>'
                    change = True
                    continue
                if x[i][j % w] == '>':
                    n[j % w] = '>'
                    continue
            x[i] = n

        for j in range(w):
            n = ['.'] * h
            for i in range(h):
                if x[i % h][j] == '>':
                    n[i % h] = '>'
                    continue
                if x[i % h][j] == 'v' and x[(i+1) % h][j] == '.':
                    n[(i+1) % h] = 'v'
                    change = True
                    continue
                if x[i % h][j] == 'v':
                    n[i % h] = 'v'
                    continue
            for i in range(h):
                x[i][j] = n[i]
        c = c + 1
        print(c)


