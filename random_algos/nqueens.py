from pprint import pprint as print


num_ways = -1


def found(N, queen):

    return queen == N


def traverse_direction(N, grid, i, j, x, y):

    while 0 <= i < N and 0 <= j < N:
        if grid[i][j] == 1:
            return False
        i += x
        j += y

    return True


def diagonal(N, grid, i, j):

    return traverse_direction(N, grid, i, j, -1, -1) and \
           traverse_direction(N, grid, i, j, 1, -1) and \
           traverse_direction(N, grid, i, j, -1, 1) and \
           traverse_direction(N, grid, i, j, 1, 1)


def column(N, grid, i, j):

    return traverse_direction(N, grid, i, j, -1, 0) and \
           traverse_direction(N, grid, i, j, 1, 0)


def row(N, grid, i, j):

    return traverse_direction(N, grid, i, j, 0, 1) and \
           traverse_direction(N, grid, i, j, 0, -1)


def possible_positions(N, grid):

    possibilities = list()

    for i in range(N):
        for j in range(N):
            if row(N, grid, i, j) and \
                    column(N, grid, i, j) and \
                    diagonal(N, grid, i, j):
                possibilities.append((i, j))

    return possibilities


def nqueens(N, queen, grid, solutions):

    global num_ways
    if found(N, queen):
        current = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 1]
        for solution in solutions:
            if solution == current:
                break
        else:
            solutions.append(current)
            num_ways += 1
    else:
        possibilities = possible_positions(N, grid)
        for x, y in possibilities:
            grid[x][y] = 1
            nqueens(N, queen+1, grid, solutions)
            grid[x][y] = 0


def main():

    N = 5
    queen = 0
    grid = [[0 for _ in range(N)] for _ in range(N)]
    global num_ways

    num_ways = 0
    nqueens(N, queen, grid, [])
    print(num_ways)


if __name__ == '__main__':
    main()
