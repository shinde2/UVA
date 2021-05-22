from pprint import pprint as print


num_ways = 0


def found(queen, grid):

    return queen == len(grid)


def possible_positions(queen, grid):

    possibilities = list()
    N = len(grid)
    high = N * N
    low = 0 if queen == 0 else (int(grid[queen-1] / N) + 1) * N

    for n in range(low, high):
        for q in range(0, queen):
            if q % N == n % N:
                break
        else:
            possibilities.append(n)

    for q in range(0, queen):
        n = grid[q]
        while n < N * N:
            if n in possibilities:
                possibilities.remove(n)
            n += 3
        n = grid[q]
        while n < N * N:
            if n in possibilities:
                possibilities.remove(n)
            n += 5
        n = grid[q]
        while n >= 0:
            if n in possibilities:
                possibilities.remove(n)
            n -= 5
        n = grid[q]
        while n >= 0:
            if n in possibilities:
                possibilities.remove(n)
            n -= 3

    return possibilities


def nqueens(queen, grid):

    global num_ways
    if found(queen, grid):
        num_ways += 1
    else:
        possibilities = possible_positions(queen, grid)
        #print(queen)
        #print(possibilities)
        for possibility in possibilities:
            grid[queen] = possibility
            nqueens(queen+1, grid)


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
