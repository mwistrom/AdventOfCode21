def do_it():

    b = []
    # b.append(['Z','N'])
    # b.append(['M','C','D'])
    # b.append(['P'])
#
#             [M]   [W][M]
#          [L][Q][S][C][R]
#          [Q][F][F][T][N][S]
#    [N]   [V][V][H][L][J][D]
#    [D][D][W][P][G][R][D][F]
# [T][T][M][G][G][Q][N][W][L]
# [Z][H][F][J][D][Z][S][H][Q]
# [B][V][B][T][W][V][Z][Z][M]

    b.append(['B','Z','T'])
    b.append(['V','H','T','D','N'])
    b.append(['B','F','M','D'])
    b.append(['T','J','G','W','V','Q','L'])
    b.append('W D G P V F Q M'.split(' '))
    b.append('V Z Q G H F S'.split(' '))
    b.append('Z S N R L T C W'.split(' '))
    b.append('Z H W D J N R M'.split(' '))
    b.append('M Q L F D S'.split(' '))

    print(b)

    lines = []
    with open('aoc_05.txt') as my_file:
        for line in my_file:
            a = list(line[:-1].split(' '))
            lines.append(list(map( int, [a[1], a[3], a[5]])))

    h = len(lines)
    w = len(lines[0])
    print(h, "  ", w)

    score = 0
    for line in lines:
        print(line)

        x = list(b[line[1]-1][-(line[0]):])
        print('x',x)
        b[line[1]-1] = b[line[1]-1][:-line[0]]
        print( b[line[1]-1])
        b[line[2]-1] = b[line[2]-1] + x
        print(b[line[2] - 1])
        print(b)
    print(b)
