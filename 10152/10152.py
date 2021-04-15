

def shell_sort(current, expected):

    moves = list()
    current = [[name, i] for i, name in enumerate(current)]

    while True:
    nxt = None
        for curr in current:
            if curr[1] > expected.get(curr[0]):
                if nxt:
                    if expected.get(curr[0]) > expected.get(nxt):
                        nxt = curr[0]
                else:
                    nxt = curr[0]
        if nxt:
            for elem in current:
                if elem[0] != nxt:
                    elem[1] += 1
                else:
                    elem[1] = 0
                    moves.append(elem[0])
                    break
        else:
            for name in moves:
                print(name)
            print(" ")
            break


def main():

    with open("inputs.txt") as f:
        lines = f.readlines()

    cases = list()

    i = 1
    while i < len(lines):
        k = int(lines[i].strip())
        current = list()
        expected = dict()
        j = k
        while j:
            i += 1
            current.append(lines[i].strip())
            j -= 1
        j = k
        while j:
            i += 1
            expected.setdefault(lines[i].strip(), k-j)
            j -= 1
        cases.append([current, expected])
        i += 1

    for case in cases:
        shell_sort(*case)


if __name__ == '__main__':
    main()
