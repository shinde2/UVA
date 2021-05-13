

num_ways = -1


def found(N, queen):

    return queen == N


def available(queen, grid, i, j):

    return grid[i][j] == 0 or (grid[i][j] == 1 and grid[i][j] > queen)


def traverse_direction(N, queen, grid, i, j, x, y):

    while 0 <= i < N and 0 <= j < N:
        if not available(queen, grid, i, j):
            return False
        i += x
        j += y

    return True


def diagonal(N, queen, grid, i, j):

    return traverse_direction(N, queen, grid, i, j, -1, -1) and \
           traverse_direction(N, queen, grid, i, j, 1, -1) and \
           traverse_direction(N, queen, grid, i, j, -1, 1) and \
           traverse_direction(N, queen, grid, i, j, 1, 1)


def column(N, queen, grid, i, j):

    return traverse_direction(N, queen, grid, i, j, -1, 0) and \
           traverse_direction(N, queen, grid, i, j, 1, 0)


def row(N, queen, grid, i, j):

    return traverse_direction(N, queen, grid, i, j, 0, 1) and \
           traverse_direction(N, queen, grid, i, j, 0, -1)


def place_queen(grid, x, y):

    grid[x][y] = 1


def possible_positions(N, queen, grid):

    possibilities = list()

    for i in range(N):
        for j in range(N):
            if row(N, queen, grid, i, j) and \
                    column(N, queen, grid, i, j) and \
                    diagonal(N, queen, grid, i, j):
                possibilities.append((i, j))

    return possibilities


def nqueens(N, queen, grid):

    global num_ways
    if found(N, queen):
        num_ways += 1
    else:
        for x, y in possible_positions(N, queen, grid):
            place_queen(grid, x, y)
            nqueens(N, queen+1, grid)


def main():

    N = 8
    queen = 0
    grid = [[0 for _ in range(N)] for _ in range(N)]
    global num_ways

    num_ways = 0
    nqueens(N, queen, grid)
    print(num_ways)


if __name__ == '__main__':
    main()
