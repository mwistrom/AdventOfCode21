def do_01():
    m = 0
    a = 0
    y = []
    with open('C:\\Users\\noonan\\AppData\\Roaming\\JetBrains\\PyCharmCE2022.2\\scratches\\AOC_01.txt') as my_file:
        for line in my_file:
            if len(line) == 1:
                m = max(m, a)
                y.append(a)
                a=0
                continue

            x = int(line)
            a = a + x
    print(m)
    y.sort(reverse=True)
    print(y)
    print(y[0] + y[1] + y[2])

def do_02a():


if __name__ == '__main__':
    do_02a()


