from pprint import pprint as print
from math import ceil


num_ways = 0


def found(queen, k):

    return queen == k - 1


def possible_positions(queen, grid, n):

    N = n * n
    possibilities = list()

    for c in range(grid[queen-1]+1, N):
        probable = set()
        k = c
        while k >= 0:
            k1 = k - (n-1)
            if int(k/n) - int(k1/n) == 1:
                probable.add(k1)
                k = k1
            else:
                break
        k = c
        while k >= 0:
            k1 = k - (n+1)
            if int(k/n) != int(k1/n):
                probable.add(k1)
                k = k1
            else:
                break
        if not (set(grid[:queen]) & probable):
            possibilities.append(c)

    return possibilities


def nqueens(queen, grid, k, n):

    global num_ways
    if found(queen, k):
        num_ways += 1
    else:
        queen += 1
        possibilities = possible_positions(queen, grid, n)
        #print("----------")
        #print(num_ways)
        #print(grid)
        #print(queen)
        #print(possibilities)
        for possibility in possibilities:
            grid[queen] = possibility
            nqueens(queen, grid, k, n)


def main():

    n = 3
    k = 2
    queen = -1
    grid = [-1 for _ in range(k)]
    global num_ways

    num_ways = 0
    nqueens(queen, grid, k, n)
    print(num_ways)


if __name__ == '__main__':
    main()
