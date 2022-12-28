from collections import defaultdict


def do_it():
    ss = []
    bs = []
    rs = []
    lines = []

    with open('aoc_15.txt') as my_file:
        for line in my_file:
            l = line[:-1].split(" ")
            print(l)
            ss.append((int(l[2][2:-1]), int(l[3][2:-1])))
            bs.append((int(l[8][2:-1]), int(l[9][2:])))

        beacon_set = set(bs)
        sensor_set = set(ss)
        print(ss)
        print(bs)
        print(sensor_set)
        print(beacon_set)


        for s in ss:
            r = 1000000000000
            for b in bs:
                r = min(r, abs(s[0] - b[0]) + abs(s[1] - b[1]))
            rs.append(r)

        print(rs)


        for idx, s in enumerate(ss):
            i = s[0] - rs[idx] - 1
            j = s[1]
            while i <= s[0]:
                # found = True
                for idx2, s2 in enumerate(ss):
                    #print("Sensor: ", idx, s, "  Sensor: ", idx2, s2)
                    if idx != idx2 and abs(s2[0] - i) + abs(s2[1] - j) <= rs[idx2]:
                        # found = False


                        print("Found")
                        print(i,j, 4000000 * i + j )
                        if 0 <= i <= 4000000 and 0 <= j <= 4000000:
                            print("This one is good.")
                        print()


                i += 1
                j += 1

