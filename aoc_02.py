def do_02():
    x = []
    with open('aoc_02.txt') as my_file:
        for line in my_file:
            a = list(line[:-1].split(' '))
            x.append(a)

    h = len(x)
    w = len(x[0])

    print(h, "  ", w)

    score = 0
    # for l in x:
    #     if (len(l[0]) < 1):
    #         continue
    #     # print(l)
    #     z = ( ord(l[0]) - ord(l[1]) + 23) % 3
    #     # print(z)
    #     if z == 1:
    #         score = score + 0
    #     if z == 2:
    #         score = score + 6
    #     if z == 0:
    #         score = score + 3
    #
    #     if l[1] == 'X':
    #         score = score + 1
    #     if l[1] == 'Y':
    #         score = score + 2
    #     if l[1] == 'Z':
    #         score = score + 3

    print (score)

    score = 0
    for l in x:
        print(l)

        match l:
            case ['A', 'X']:
                score = score + 3
            case ['B', 'X']:
                score = score + 1
            case ['C', 'X']:
                score = score + 2
            case ['A', 'Y']:
                score = score + 4
            case ['B', 'Y']:
                score = score + 5
            case ['C', 'Y']:
                score = score + 6
            case ['A', 'Z']:
                score = score + 8
            case ['B', 'Z']:
                score = score + 9
            case ['C', 'Z']:
                score = score + 7
    print(score)
