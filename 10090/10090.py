

def marbles(N, u, v, x, y):

    solutions = []

    vn = v
    while vn < N:
        _N = N - vn
        if _N % y == 0:
            solutions.append((int(vn/v), int(_N/y)))
        vn += v

    if solutions:
        total = float("Inf")
        p = None
        q = None
        for a, b in solutions:
            if u * a + x * b < total:
                total = u * a + x * b
                p = a
                q = b
        print(f"{p} {q}")
    else:
        print("failed")


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
