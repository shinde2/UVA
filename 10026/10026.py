

def main():

    cases = list()

    with open("tests.txt") as f:
        lines = f.readlines()

    i = 2
    while i < len(lines):
        j = int(lines[i].strip())
        case = list()
        while j:
            i += 1
            case.append(list(map(int, lines[i].strip().split())))
            j -= 1
        i += 2
        cases.append(case)

    with open("outputs.txt", "w") as f:
        for case in cases:
            #f.write(" ".join([str(i[0]+1) for i in sorted(enumerate(case), key=lambda x:x[1][1]/x[1][0],
            # reverse=True)]))
            f.write(" ".join([str(i[0]+1) for i in sorted(enumerate(case), key=lambda x:x[1][0]/x[1][1])]))
            f.write(" ")


if __name__ == '__main__':
    main()
