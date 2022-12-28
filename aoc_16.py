from collections import defaultdict
import json

answer = 0

def do_it():
    lines = []
    with open('aoc_16.txt') as my_file:
        for line in my_file:
            lines.append(line)

    edges = {}
    visited = {}

    for line in lines:
        temp = line.split(" ")
        key = temp[1]
        rate = int((temp[4][5:])[:-1])
        c = 9
        ca = []
        while True:
            ca.append([temp[c][:-1], 1])
            c = c + 1
            if c == len(temp):
                break

        edges[key] = [rate, ca]

    # for key, val in edges.items():
    #     for node in val[1]:
    #         print(key+"_"+str(val[0]), ' -> ', node+"_"+str(edges[node][0]))
    # print(json.dumps(edges, indent=2))

    changed = True
    while changed:
        changed = False
        x = []
        remove_key = ""
        remove_dist = 0
        for key, val in edges.items():
            if val[0] == 0 and len(val[1]) <= 2:
                x = edges[key][1]

                remove_key = key
                changed = True
                break
        if changed:
            print("Remove: ", key, "ends:", x)
            update0 = x[0]
            update1 = x[1]
            remove_dist = x[0][1] + x[1][1]
            remove_from_adj = None
            for y in edges[update1[0]][1]:
                remove_from_adj = y
                if y[0] == remove_key:
                    edges[update1[0]][1].append([update0[0], remove_dist ])
                    break
            edges[update1[0]][1].remove(remove_from_adj)
            for y in edges[update0[0]][1]:
                remove_from_adj = y
                if y[0] == remove_key:
                    edges[update0[0]][1].append([update1[0], remove_dist ])
                    break
            edges[update0[0]][1].remove(remove_from_adj)
            edges.pop(remove_key, None)
    print(len(edges))
    print(edges)
    for key, val in edges.items():
        for node in val[1]:
            print(key+"_"+str(val[0]), ' -> ', node[0]+"_"+
                  str(edges[node[0]][0]) + '  [label = "' + str(node[1]) + '"];')

    dp(edges, "AA", "AA", 0, 0, 0, set(), {})
    print(answer)


def dp(edges, node, enode, t, time, etime, total_rate, total_flow, open_valves ):
    global answer

    temp = total_flow + (total_rate * (26 - t))
    if temp > answer:
        answer = temp
        print(answer)
    if t >= 26:
        return

    rate, children = edges[node]
    erate, echildren = edges[enode]


    if t == time:     # move

        if node not in open_valves:
            open_valves.add(node)
            time_next = time + 1




        edp(edges, node, enode, time, total_rate, total_flow , open_valves)
        open_valves.remove(node)

    for child in children:
        edp(edges, child, enode, time, total_rate, total_flow, open_valves )

def edp(edges, node, enode, time, total_rate, total_flow, open_valves ):
    global answer

    if enode not in open_valves:
        open_valves.add(enode)
        dp(edges, node, enode,
           time + 1, total_rate + erate , total_flow + total_rate, open_valves)
        open_valves.remove(enode)

    for echild in echildren:
        dp(edges, node, echild,  time + 1, total_rate ,
           total_flow + total_rate, open_valves)
