

def solved(puzzle):

    solution = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                10, 11, 12, 13, 14, 15, 0]

    return puzzle == solution


def possibilities(puzzle, curr, moves, index):

    poss = []

    if 0 <= int(curr / 4) + 1 <= 3 and moves[index] != "U" and puzzle[curr+4] <= curr+1:
        poss.append("D")
    if 0 <= (curr % 4) + 1 <= 3 and moves[index] != "L" and puzzle[curr+1] <= curr+1:
        poss.append("R")
    if 0 <= (curr % 4) - 1 <= 3 and moves[index] != "R" and puzzle[curr-1] >= curr+1:
        poss.append("L")
    if 0 <= int(curr / 4) - 1 <= 3 and moves[index] != "D" and puzzle[curr-4] >= curr+1:
        poss.append("U")

    return poss


def backtrack(puzzle, curr, moves, index):

    if index >= 50:
        return -1
    elif solved(puzzle):
        return index
    else:
        index += 1
        for possibility in possibilities(puzzle, curr, moves, index-1):
            if possibility == "U":
                nxt = curr-4
            elif possibility == "D":
                nxt = curr+4
            elif possibility == "L":
                nxt = curr-1
            else:
                nxt = curr+1
            temp = puzzle[nxt]
            puzzle[nxt] = puzzle[curr]
            puzzle[curr] = temp
            moves.append(possibility)
            i = backtrack(puzzle, nxt, moves, index)
            temp = puzzle[nxt]
            puzzle[nxt] = puzzle[curr]
            puzzle[curr] = temp
            if i != -1:
                return i
        return -1


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
