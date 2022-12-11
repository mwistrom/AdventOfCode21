def do_03():
    lines = []
    with open('aoc_03.txt') as my_file:
        for line in my_file:
            lines.append(line[:-1])
    o = 0
    # for line in x:
    #     print(line)
    #     l = len(line)
    #
    #     f = line[0:l//2]
    #     s = line[l//2:l]
    #     print( f, s)
    #     done = False
    #     for i in f:
    #         if done:
    #             break
    #         for j in s:
    #             if i == j:
    #                 print(i)
    #                 if i.islower():
    #                     x = ord(i) - ord('a') + 1
    #                     print(x)
    #                     o = o + x
    #                     done = True
    #                     break
    #                 x = ord(i) - ord('A') + 27
    #                 done = True
    #                 print(x)
    #                 o = o + x
    #                 break
    # print("done")
    # print(o)

    line_i = 0
    o = 0
    print(lines)
    while line_i + 2 < len(lines):
        a = lines[line_i]
        b = lines[line_i + 1]
        c = lines[line_i + 2]
        line_i = line_i + 3

        done = False

        for i in a:
            if done:
                break
            for j in b:
                if i != j:
                    continue
                if done:
                    break
                for k in c:
                    if i == k:
                        print(i)
                        if i.islower():
                            x = ord(i) - ord('a') + 1
                            print(x)
                            o = o + x
                            done = True
                            break
                        x = ord(i) - ord('A') + 27
                        done = True
                        print(x)
                        o = o + x
                        break

    print(o)



