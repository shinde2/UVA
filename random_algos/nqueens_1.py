from pprint import pprint as print


num_ways = 0


def found(queen, grid):

    return queen == len(grid)


def possible_positions(queen, grid):

    possibilities = list()

    for c in range(1, len(grid)+1):
    for q in range(1, queen):
        if grid[q] == queen + (queen - q) or grid[q] == queen - (queen - q):

    return possibilities


def nqueens(queen, grid):

    global num_ways
    if found(queen, grid):
        num_ways += 1
    else:
        queen += 1
        possibilities = possible_positions(queen, grid)
        for possibility in possibilities:
            grid[queen] = possibility
            nqueens(queen, grid)


def main():

    N = 4
    queen = 0
    grid = [-1 for _ in range(N)]
    global num_ways

    num_ways = 0
    nqueens(queen, grid)
    print(num_ways)


if __name__ == '__main__':
    main()
