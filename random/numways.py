

def nummoves(cost, a, b, y, z, allmoves):

    if a == y and b == z:
        return 0
    elif a > y or b > z:
        return -1
    elif allmoves[a][b]:
        return allmoves[a][b]
    else:
        moves = 2 + nummoves(cost, a+1, b, y, z, allmoves) + nummoves(cost, a, b+1, y, z, allmoves)
        allmoves[a][b] = moves
        return moves


def numways(cost, a, b, y, z, allways):

    if a == y and b == z:
        return 1
    elif a > y or b > z:
        return 0
    elif allways[a][b]:
        return allways[a][b]
    else:
        ways = numways(cost, a+1, b, y, z, allways) + numways(cost, a, b+1, y, z, allways)
        allways[a][b] = ways
        return ways


def numways_bottomup(cost, a, b, y, z, allwaysbu):

    allwaysbu[a][b] = 0

    for j in range(b+1, z+1):
        allwaysbu[a][j] = 1

    for i in range(a+1, y+1):
        allwaysbu[i][b] = 1

    for i in range(a+1, y+1):
        for j in range(b+1, z+1):
            allwaysbu[i][j] = allwaysbu[i][j-1] + allwaysbu[i-1][j]

    return allwaysbu[y][z]


def main():

    #cost = [
    #        [1, 8, 8, 1, 5],
    #        [4, 1, 1, 8, 1],
    #        [4, 2, 8, 8, 1],
    #        [1, 5, 8, 8, 1]
    #       ]

    cost = [
        [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]
    ]

    allmoves = [[None] * len(row) for row in cost]
    allways = [[None] * len(row) for row in cost]
    allwaysbu = [[None] * len(row) for row in cost]

    a = 0
    b = 0
    y = 1
    z = 2

    moves = nummoves(cost, a, b, y, z, allmoves)
    print(f"Num moves: {moves}")

    ways = numways(cost, a, b, y, z, allways)
    print(f"Num ways: {ways}")

    waysbu = numways_bottomup(cost, a, b, y, z, allwaysbu)
    print(f"Num ways bottom up: {waysbu}")


if __name__ == '__main__':
    main()
