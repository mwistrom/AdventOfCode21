from collections import defaultdict
import json

answer = 0
count = 0
hit = 0

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
            ca.append(temp[c][:-1])
            c = c + 1
            if c == len(temp):
                break

        edges[key] = [rate, ca]

    print(edges)
    ans = dp(edges, 0, 'AA', 'aa', 'AA', 'aa', 0, 0, set(), {})
    print( ans)


def dp(edges, time, node, parent, enode, eparent, total_rate, total_flow, open_valves, memo):
    global answer, count, hit
    count += 1
    if count % 500000 == 0:
        print(time, node, enode, total_rate, total_flow, answer, hit / count)
        count = 1
        hit = 0
    if time == 26:
        return total_flow
    key = (time, node, enode, total_rate, total_flow)
    if key in memo:
        hit += 1
        return memo[key]

    rate, children = edges[node]
    ret = 0

    if rate > 0 and node not in open_valves:
        open_valves.add(node)
        ret = edp(edges, time, node, 'a', enode, eparent, total_rate, total_flow , open_valves, rate, memo)
        open_valves.remove(node)

    for child in children:
        if child == parent and len(children) > 1:
            continue
        ret = max(ret, edp(edges, time, child, node, enode, eparent,
                           total_rate, total_flow, open_valves , 0, memo))
    memo[key] = ret
    answer = max(answer, ret)

    return ret

def edp(edges, time, node, parent, enode, eparent, total_rate, total_flow, open_valves, my_rate, memo ):
    global answer
    erate, echildren = edges[enode]

    ret = 0

    if erate > 0 and enode not in open_valves:
        open_valves.add(enode)
        ret = dp(edges, time + 1, node, parent, enode, 'aa',
                 total_rate + erate + my_rate, total_flow + total_rate, open_valves, memo)
        open_valves.remove(enode)

    for echild in echildren:
        if echild == eparent and len(echildren) > 1:
            continue
        ret = max(ret, dp(edges, time + 1, node, parent, echild, eparent, total_rate + my_rate,
                total_flow + total_rate, open_valves, memo))
    return ret

