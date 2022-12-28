from collections import defaultdict


def do_it():
    lines = [0] *1000
    k = 0
    with open('aoc_10.txt') as my_file:
        for line in my_file:
            x = line[:-1].split(' ')
            if x[0] == 'noop':
                lines[k] = 0
            else:
                lines[k] = (int(x[1]))
            k += 1

    h = len(lines)
    #w = len(lines[0])
    #print(h, "  ", w)

    print(lines)

    a = [0] * 2010
    i = 0
    j = 1
    a[0] = 1
    a[1] = 1
    while i < 1000:
        if i >= len(lines):
            break
        if lines[i] == 0:
            j = j + 1
            a[j] = a[j-1]
        else:
            j = j + 2
            a[j] = a[j-2] + lines[i]
            a[j-1] = a[j-2]
        i = i + 1

    print(i ,j )


    i = 0
    while i < 240:
        print(i, a[i])
        i = i + 1



    i = 0
    while i < 240:

        if i % 40 == 0:
            print()
        j = i % 40
        c = '.'
        if j - 2 == a[i] or j == a[i] or j-1 == a[i]:
            c = '#'
        print(c, end='')
        i = i + 1




