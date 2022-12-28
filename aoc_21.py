from collections import defaultdict
import copy


def do_it():
    d = {}
    o = {}
    count = 0
    with open('aoc_21.txt') as my_file:
        for line in my_file:
            count += 1
            x = line[:-1].split(": ")
            # print(x)
            if x[1].isnumeric():
                d[x[0]] = int(x[1])
            else:
                y = x[1].split(' ')
                o[x[0]] = (y[0], y[1], y[2])

    print(d)
    print(o)

    # while len(d) < count:
    #     x = 0
    #     for k, v in o.items():
    #         if v[0] in d and v[2] in d:
    #             match v[1]:
    #                 case '*':
    #                     x = d[v[0]] * d[v[2]]
    #                 case '+':
    #                     x = d[v[0]] + d[v[2]]
    #                 case '-':
    #                     x = d[v[0]] - d[v[2]]
    #                 case '/':
    #                     x = d[v[0]] // d[v[2]]
    #             d[k] = x
    #
    # print(d['root'], d['qntq'], d['qgth'])
    # exit(0)


    # x = calc(o, copy.deepcopy(d), 30000000000000, count)
    # print(x)
    # x = calc(o, copy.deepcopy(d), 30, count)
    # print(x)

    le = 0
    r = 100000000000000
    while le <= r:
        m = (le + r) // 2
        x = calc(o, copy.deepcopy(d), m, count)
        print(le, r, m, x)
        if x[1] > x[2]:
            le = m + 1
        elif x[1] < x[2]:
            r = m - 1
        else:
            print(m, x)
            break


# 31017034901322 22790998779089 8226036122233
# 31017018513462 22,790,982,391,229 8226036122233
#                 8226036122233


def calc(o, d, human, count):
    d['humn'] = human
    while len(d) < count:
        x = 0
        for k, v in o.items():
            if v[0] in d and v[2] in d:
                match v[1]:
                    case '*':
                        x = d[v[0]] * d[v[2]]
                    case '+':
                        x = d[v[0]] + d[v[2]]
                    case '-':
                        x = d[v[0]] - d[v[2]]
                    case '/':
                        x = d[v[0]] / d[v[2]]
                    case '=':
                        continue
                d[k] = x
    return d['root'], d['qntq'], d['qgth']
    # return d['root'], d['pppw'], d['sjmn']