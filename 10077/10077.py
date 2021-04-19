
class Fraction:

    def __init__(self, N, D):
        self.N = N
        self.D = D


def SternBrocot(*args):

    a, b, f = args

    if a == 1 and b == 1:
        return

    seq = list()
    N = a/b

    if N > 1:
        seq.append("R")
        L = Fraction(1, 1)
        R = Fraction(1, 0)
    else:
        seq.append("L")
        R = Fraction(1, 1)
        L = Fraction(0, 1)

    curr = Fraction(L.N+R.N, L.D+R.D)
    while not (curr.N == a and curr.D == b):
        if N - (curr.N/curr.D) < 0:
            R = curr
            seq.append("L")
        else:
            L = curr
            seq.append("R")
        curr = Fraction(L.N+R.N, L.D+R.D)

    f.write("".join(seq))
    f.write("\n")


def main():

    with open("inputs.txt") as infile:
        lines = infile.readlines()

    with open("outputs.txt", "w") as outfile:
        for line in lines:
            SternBrocot(*map(int, line.strip().split()), outfile)


if __name__ == '__main__':
    main()
