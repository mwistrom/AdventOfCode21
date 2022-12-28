from collections import defaultdict


def do_it():
    # nm = 4
    # items = [[79, 98],
    #          [54, 65, 75, 74],
    #          [79, 60, 97],
    #          [74]]
    # op = [lambda x: x*19,
    #       lambda x: x + 6,
    #       lambda x: x * x,
    #       lambda x:x+3]
    # test = [23,19,13,17]
    # tr = [2,2,1,0]
    # fl = [3,0,3,1]

    nm = 8
    items = [[98, 97, 98, 55, 56, 72],
             [73, 99, 55, 54, 88, 50, 55],
             [67, 98],
             [82, 91, 92, 53, 99],
             [52, 62, 94, 96, 52, 87, 53, 60],
             [94, 80, 84, 79],
             [89],
             [70, 59, 63]
             ]
    op = [lambda x: x * 13,
          lambda x: x + 4,
          lambda x: x * 11,
          lambda x: x + 8,
          lambda x: x * x,
          lambda x: x + 5,
          lambda x: x + 1,
          lambda x: x + 3,
          ]
    test = [11,17,5,13,19,2,3,7]
    tr = [4,2,6,1,3,7,0,4]
    fl = [7,6,5,2,1,0,5,3]

    inspect = [0 for _ in range(nm)]

    for iter in range(10000):

        for m_idx in range(nm):
            while len(items[m_idx]) > 0:
                inspect[m_idx] += 1
                x = items[m_idx].pop(0)
                x = op[m_idx](x)
                x = x % (11 * 17 * 5 * 13 * 19 * 2 * 3 *7)
                if iter % 100 == 0:
                    print(iter, x)
                if x % test[m_idx] == 0:
                    items[tr[m_idx]].append(x)
                else:
                    items[fl[m_idx]].append(x)

    print(inspect)
    inspect.sort(reverse=True)
    print(inspect)
    print(inspect[0] * inspect[1])
