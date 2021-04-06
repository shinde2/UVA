

def mincostpath(cost, a, b, y, z, mincost):

    if a == y and b == z:
        return cost[y][z]
    elif a > y or b > z:
        return float("Inf")
    elif mincost[a][b]:
        return mincost[a][b]
    else:

        _min = cost[a][b] + min(mincostpath(cost, a+1, b, y, z, mincost),
                                   mincostpath(cost, a+1, b+1, y, z, mincost),
                                   mincostpath(cost, a, b+1, y, z, mincost))
        mincost[a][b] = _min
        return _min


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

    mincost = [[None] * len(row) for row in cost]

    a = 1
    b = 0
    y = 2
    z = 2
    cost = mincostpath(cost, a, b, y, z, mincost)

    print(cost)


if __name__ == '__main__':
    main()
