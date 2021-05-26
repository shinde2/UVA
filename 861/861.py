from pprint import pprint as print
from math import ceil


num_ways = 0


def found(queen, grid):

    return queen == len(grid) - 1


def possible_positions(queen, grid, n):

    N = n * n
    possibilities = list()

    for c in range(grid[queen-1]+1, N+1):
        probable = set()
        k = c
        while k >= 1:
            k1 = k - (n-1)
            if ceil(k/n) - ceil(k1/n) == 1:
                probable.add(k)
                k = k1
            else:
                break
        k = c
        while k >= 1:
            k1 = k - (n+1)
            if ceil(k/n) != ceil(k1/n):
                probable.add(k)
                k = k1
            else:
                break
        if not (set(grid[1:queen]) & probable):
            possibilities.append(c)

    return possibilities


def nqueens(queen, grid, N):

    global num_ways
    if found(queen, grid):
        num_ways += 1
    else:
        queen += 1
        possibilities = possible_positions(queen, grid, N)
        print(queen)
        print(possibilities)
        for possibility in possibilities:
            grid[queen] = possibility
            nqueens(queen, grid, N)


def main():

    n = 3
    k = 2
    queen = 0
    grid = [0 for _ in range(k+1)]
    global num_ways

    num_ways = 0
    nqueens(queen, grid, n)
    print(num_ways)


if __name__ == '__main__':
    main()
