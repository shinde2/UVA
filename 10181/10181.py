from copy import deepcopy


def solved(puzzle):

    solution = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                10, 11, 12, 13, 14, 15, 0]

    return puzzle == solution


def possibilities(curr, moves, index):

    poss = []

    if 0 <= curr + 4 <= 15 and moves[index] != "U":
        poss.append("D")
    if 0 <= curr + 1 <= 15 and moves[index] != "L":
        poss.append("R")
    if 0 <= curr - 1 <= 15 and moves[index] != "R":
        poss.append("L")
    if 0 <= curr - 4 <= 15 and moves[index] != "D":
        poss.append("U")

    return poss


def backtrack(puzzle, curr, moves, index):

    if index >= 50:
        return -1
    elif solved(puzzle):
        return index
    else:
        index += 1
        for possibility in possibilities(curr, moves, index-1):
            if possibility == "U":
                n = curr-4
            elif possibility == "D":
                n = curr+4
            elif possibility == "L":
                n = curr-1
            else:
                n = curr+1
            p = deepcopy(puzzle)
            t = p[n]
            p[n] = 0
            p[curr] = t
            moves.append(possibility)
            i = backtrack(p, n, moves, index)
            if i != -1:
                return i
        return i


def solve(puzzle):

    moves = ["X"]

    for index, num in enumerate(puzzle):
        if num == 0:
            i = backtrack(puzzle, index, moves, 0)
            break

    if i == -1:
        print("This puzzle is not solvable.")
    else:
        print("".join(moves[1:i+1]))


def main():

    with open("inputs.txt") as infile:
        lines = infile.readlines()

    puzzle = []
    for j, i in enumerate(lines[1:], start=1):
        puzzle.extend(map(int, i.strip().split()))
        if j % 4 == 0:
            solve(puzzle)
            puzzle = []


if __name__ == '__main__':
    main()
