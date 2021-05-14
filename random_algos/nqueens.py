from pprint import pprint as print
from copy import deepcopy


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


def traverse_mark(N, grid, i, j, x, y):

    i += x
    j += y
    while 0 <= i < N and 0 <= j < N:
        grid[i][j] = 1
        i += x
        j += y


def diagonal(N, grid, i, j):

    t = traverse_direction(N, grid, i, j, -1, -1) and \
        traverse_direction(N, grid, i, j, 1, 1)
    b = traverse_direction(N, grid, i, j, 1, -1) and \
        traverse_direction(N, grid, i, j, -1, 1)

    if not t:
        traverse_mark(N, grid, i, j, -1, -1)
        traverse_mark(N, grid, i, j, 1, 1)

    if not b:
        traverse_mark(N, grid, i, j, 1, -1)
        traverse_mark(N, grid, i, j, -1, 1)

    return t and b


def column(N, grid, i, j):

    u = traverse_direction(N, grid, i, j, -1, 0)
    d = traverse_direction(N, grid, i, j, 1, 0)

    if not u or not d:
        traverse_mark(N, grid, i, j, -1, 0)
        traverse_mark(N, grid, i, j, 1, 0)

    return u and d


def row(N, grid, i, j):

    r = traverse_direction(N, grid, i, j, 0, 1)
    l = traverse_direction(N, grid, i, j, 0, -1)

    if not r or not l:
        traverse_mark(N, grid, i, j, 0, 1)
        traverse_mark(N, grid, i, j, 0, -1)

    return r and l


def possible_positions(N, grid):

    possibilities = list()
    grid_new = deepcopy(grid)

    for i in range(N):
        for j in range(N):
            if grid_new[i][j] == 0:
                if row(N, grid_new, i, j) and \
                        column(N, grid_new, i, j) and \
                        diagonal(N, grid_new, i, j):
                    possibilities.append((i, j))
                #else:
                #    grid_new[i][j] = 1
    print(grid_new)
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
        print(queen)
        print(grid)
        print(possibilities)
        print("----------------")
        for x, y in possibilities:
            grid[x][y] = 1
            nqueens(N, queen+1, grid, solutions)
            grid[x][y] = 0


def main():

    N = 4
    queen = 0
    grid = [[0 for _ in range(N)] for _ in range(N)]
    global num_ways

    num_ways = 0
    nqueens(N, queen, grid, [])
    print(num_ways)


if __name__ == '__main__':
    main()
