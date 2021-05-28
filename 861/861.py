from pprint import pprint as print


num_ways = 0


def found(queen, k):

    return queen == k - 1


def possible_positions(queen, grid, n):

    possibilities = list()

    for _n in range(grid[queen-1]+1, n * n):
        conflicting = set()
        row = int(_n/n)
        col = _n % n
        for r in range(row):
            c = col + (row - r)
            if 0 <= c < n:
                conflicting.add(r * n + c)
            c = col - (row - r)
            if 0 <= c < n:
                conflicting.add(r * n + c)
        if not (set(grid[:queen]) & conflicting):
            possibilities.append(_n)

    return possibilities


def nqueens(queen, grid, k, n):

    global num_ways
    if found(queen, k):
        num_ways += 1
    else:
        queen += 1
        possibilities = possible_positions(queen, grid, n)
        for possibility in possibilities:
            grid[queen] = possibility
            nqueens(queen, grid, k, n)


def main():

    n = 8
    k = 6
    queen = -1
    grid = [-1 for _ in range(k)]
    global num_ways

    num_ways = 0
    nqueens(queen, grid, k, n)
    print(num_ways)


if __name__ == '__main__':
    main()
