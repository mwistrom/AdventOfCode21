def do_04():
    lines = []
    with open('aoc_04.txt') as my_file:
        for line in my_file:
            a = list(line[:-1].split(','))
            lines.append(a)

    h = len(lines)
    w = len(lines[0])
    print(h, "  ", w)

    score = 0

    for line in lines:
        i1, i2 = list(map(int, line[0].split("-") ))
        j1, j2 = list(map(int, line[1].split("-") ))
        print(i1, i2, j1, j2)
        if i1 >= j1 and i1 <= j2:
            score = score + 1
            continue
        if i2 >= j1 and i2 <= j2:
            score = score + 1
            continue
        if j1 >= i1 and j1 <= i2:
            score = score + 1
            continue
        if j2 >= i1 and j2 <= i2:
            score = score + 1


    print(score)
