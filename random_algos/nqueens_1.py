from pprint import pprint as print


num_ways = 0


def found(queen, grid):

    return queen == len(grid) - 1


def possible_positions(queen, grid):

    possibilities = list()

    for c in range(1, len(grid)):
        conflict = False

        for q in range(1, queen):
            if grid[q] == c + (queen - q) or grid[q] == c - (queen - q):
                conflict = True
        for q in range(1, queen):
            if grid[q] == c:
                conflict = True
        if not conflict:
            possibilities.append(c)

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

    N = 10
    queen = 0
    grid = [-1 for _ in range(N+1)]
    global num_ways

    num_ways = 0
    nqueens(queen, grid)
    print(num_ways)


if __name__ == '__main__':
    main()
