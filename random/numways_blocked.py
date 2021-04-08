

def numways(blocked, a, b, y, z, allways):

    if a == y and b == z:
        return 1
    elif a > y or b > z:
        return 0
    elif blocked[a][b] == 1:
        return 0
    elif allways[a][b]:
        return allways[a][b]
    else:
        ways = numways(blocked, a+1, b, y, z, allways) + numways(blocked, a, b+1, y, z, allways)
        allways[a][b] = ways
        return ways


def numways_bottomup(blocked, a, b, y, z, allwaysbu):

    allwaysbu[a][b] = 0

    #for j in range(b+1, z+1):
    #    allwaysbu[a][j] = 1

    j = b+1
    while j < z+1:
        if blocked[a][j] == 1:
            break
        else:
            allwaysbu[a][j] = 1
            j += 1
    while j < z+1:
        allwaysbu[a][j] = 0
        j += 1

    #for i in range(a+1, y+1):
    #    allwaysbu[i][b] = 1

    i = a+1
    while i < y+1:
        if blocked[i][b] == 1:
            break
        else:
            allwaysbu[i][b] = 1
            i += 1
    while i < y+1:
        allwaysbu[i][b] = 0
        i += 1

    for i in range(a+1, y+1):
        for j in range(b+1, z+1):
            if blocked[i][j] == 1:
                allwaysbu[i][j] = 0
            else:
                allwaysbu[i][j] = allwaysbu[i][j-1] + allwaysbu[i-1][j]

    return allwaysbu[y][z]


def main():

    #cost = [
    #        [1, 8, 8, 1, 5],
    #        [4, 1, 1, 8, 1],
    #        [4, 2, 8, 8, 1],
    #        [1, 5, 8, 8, 1]
    #       ]

    blocked = [
        [0, 1, 0],
        [0, 0, 0],
        [1, 1, 0]
    ]

    allways = [[None] * len(row) for row in blocked]
    allwaysbu = [[None] * len(row) for row in blocked]

    a = 0
    b = 0
    y = 2
    z = 2

    ways = numways(blocked, a, b, y, z, allways)
    print(f"Num ways blocked: {ways}")

    waysbu = numways_bottomup(blocked, a, b, y, z, allwaysbu)
    print(f"Num ways blocked bottom up: {waysbu}")


if __name__ == '__main__':
    main()
