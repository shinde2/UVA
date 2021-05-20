from pprint import pprint as print
from copy import deepcopy


num_ways = 0


def found(N, queen):

    return queen == N


def possible_positions(N, grid):

    possibilities = list()

    return possibilities


def nqueens(N, queen, grid, solutions):

    global num_ways
    if found(N, queen):
        num_ways += 1
    else:
        possibilities = possible_positions(N, grid)
        for x, y in possibilities:
            grid[x][y] = 1
            nqueens(N, queen+1, grid, solutions)
            grid[x][y] = 0


def main():

    N = 8
    queen = 0
    grid = [-1 for _ in range(N)]
    global num_ways

    num_ways = 0
    nqueens(N, queen, grid, [])
    print(num_ways)


if __name__ == '__main__':
    main()
