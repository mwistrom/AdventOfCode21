from collections import defaultdict
import copy
import collections


def do_it():
    a = []
    with open('aoc_25.txt') as my_file:
        for line in my_file:
            a.append(line[:-1])
    print(a)
    tots = 0
    for word in a:
        print(word)
        x = list(word)
        x.reverse()
        print(x)
        z = 1
        y = 0
        for c in x:
            match c:
                case '2':
                    y = y + z*2
                case '1':
                    y = y + z*1
                case '0':
                    y = y + z*0
                case '-':
                    y = y + z*(-1)
                case '=':
                    y = y + z*(-2)
            z = z * 5
        # print(y)
        tots = tots + y
    print("Totals: ", tots)

    # print(2022, baseN(2022, 5))
    # print(12345, baseN(12345, 5))

    print(snafu(tots))

    print("Range")

    # for i in range(1,200):
    #     print(i, snafu(i) )

def snafu(x):
    s = baseN(x, 5)
    sl = list(s)
    sl.reverse()
    for i in range(50):
        sl.append('0')
    # print(sl)

    for idx in range(len(sl)):
        c = sl[idx]
        match c:
            case '5':
                sl[idx] = '0'
                sl[idx + 1] = str(int(sl[idx + 1]) + 1)
            case '4':
                sl[idx] = "-"
                sl[idx + 1] = str(int(sl[idx + 1]) + 1)
            case '3':
                sl[idx] = "="
                sl[idx + 1] = str(int(sl[idx+1]) + 1)
            case other:
                sl[idx] = c
    # print(sl)
    while sl[-1] == '0':
        sl.pop()
    sl.reverse()
    ret = ''.join(sl)
    return ret

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


