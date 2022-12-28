from collections import defaultdict


def do_it():
    a = []
    b =[]
    count = 0
    d = {}
    f = {}

    zero = 0
    with open('aoc_20.txt') as my_file:
        for line in my_file:
            count += 1
            x = int(line[:-1]) * 811589153
            print(x)
            d[count] = x
            a.append(count)
            b.append(count)
            if x == 0:
                zero = count - 1
    print( d)
    print(len(d))

    for y in range(10):
        for x in a:
            i1 = b.index(x)
            for j in range(abs(d[x]) % (len(a)-1)):
                if d[x] < 0:
                    i2 = (i1 - 1) % len(a)
                else:
                    i2 = (i1 + 1) % len(a)
                t1 = b[i1]
                b[i1] = b[i2]
                b[i2] = t1
                i1 = i2
            #print([d[i] for i in b])
            #print(x)
        print([d[i] for i in b])

    ans = [d[i] for i in b]
    print(ans)

    count = 0
    index = b.index(a[zero])
    ret = 0
    while count < 3010:
        index = index % len(a)
        if count % 1000 == 0:
            ret += d[b[index]]
            print(d[b[index]])
        count += 1
        index += 1

    print(ret)