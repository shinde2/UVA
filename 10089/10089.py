

def repack(packages):

    pass

def main():

    with open("inputs.txt") as infile:
        lines = infile.readlines()

    n = 0
    while n < len(lines):
        N = int(lines[n].strip())
        if N:
            u, v = map(int, lines[n+1].strip().split())
            x, y = map(int, lines[n+2].strip().split())
            marbles(N, u, v, x, y)
        n += 3


if __name__ == '__main__':
    main()