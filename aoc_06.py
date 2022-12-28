def do_it():

    lines = []
    with open('aoc_06.txt') as my_file:
        for line in my_file:
            lines.append(line)


    h = len(lines)
    w = len(lines[0])
    print(h, "  ", w)

    score = 0
    # for line in lines:
    #     print(line)
    #     d = {}
    #     i = 0
    #     count = 0
    #     for c in line:
    #         i = i + 1
    #         if d.get(c) is None:
    #             count = count + 1
    #             d[c] = 1
    #             print(c, count)
    #         else:
    #             if d[c] == 1 and count > 0:
    #                 count = count - 1
    #             d[c] = d[c] + 1
    #             print(c, count, "    Nope")
    #
    #         if count == 4:
    #             print(i)
    #             break

    for line in lines:
        found = False
        j = 0
        for i in range(3, len(line)):
            print(i)
            d = {}
            for j in range(4):
                c = line[i-j]
                d[c] = 1
            if len(d) == 14:
                # print(i + 1, " Done")
                j = i
                break

        for i in range(j, len(line)):
            print(i)
            d = {}
            for j in range(14):
                c = line[i - j]
                d[c] = 1
            if len(d) == 14:
                print(i + 1, " Done")
                j = i + 1
                break
