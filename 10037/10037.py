import operator


def get_remaining(start):

    r = 0

    for _, typ in start:
        if typ == "A":
            r += 1

    return r


def two_slowest(start):

    s0 = None
    s1 = None

    for time, typ in start[::-1]:
        if typ == "A":
            if not s0:
                s0 = (time, typ)
            elif not s1:
                s1 = (time, typ)
            else:
                return s0, s1

    return s0, s1


def two_fastest(start):

    f0 = None
    f1 = None

    for time, typ in start:
        if typ == "A":
            if not f0:
                f0 = (time, typ)
            elif not f1:
                f1 = (time, typ)
            else:
                return f0, f1

    return f0, f1


def fastest_inB(start, s0, s1):

    slower = s1[0] if s1 else s0[0]

    for time, typ in start:
        if typ == "B" and time < slower:
            return time, typ


def change_type(start, people):

    for p in people:
        for s in start:
            if p[0] == s[0] and p[1] == s[1]:
                s[1] = "A" if p[1] == "B" else "B"
                break


def cross(start):

    time = 0
    remaining = len(start)
    moves = list()

    while remaining > 0:
        s0, s1 = two_slowest(start)
        f0, f1 = two_fastest(start)

        fB = fastest_inB(start, s0, s1)
        ct = []

        if fB:
            time += s0[0]
            ct.append(s0)
            ct.append(s1)
            moves.append([s1[0], s0[0]])
            time += fB[0]
            ct.append(fB)
            moves.append([fB[0]])
            change_type(start, ct)
        else:
            if remaining == 2:
                ct.append(f0)
                time += f1[0]
                ct.append(f1)
                moves.append([f0[0], f1[0]])
                change_type(start, ct)
            else:
                time += f0[0]
                time += f1[0]
                ct.append(f1)
                moves.append([f0[0], f1[0]])
                moves.append([f0[0]])
                change_type(start, ct)

        remaining = get_remaining(start)

    print(time)
    for move in moves:
        print(" ".join(map(str, move)))


def main():

    #start = [5, 2, 1, 10]
    #start = [5, 2, 1]
    #start = [1, 10, 10, 10, 100, 100]

    starts = list()

    with open("tests.txt") as f:
        lines = f.readlines()

    i = 2
    while i < len(lines):
        num = int(lines[i].strip())
        start = lines[i+1:i+1+num]
        start = [int(i.strip()) for i in start]
        starts.append(start)

        i += i+num+2

    for start in starts:
        start = [[i, "A"] for i in start]
        start.sort(key=operator.itemgetter(0))
        if len(start) <= 2:
            print(sum(start))
            print(" ".join(map(str, start)))
            print(" ")
        else:
            cross(start)
            print(" ")


if __name__ == '__main__':
    main()
