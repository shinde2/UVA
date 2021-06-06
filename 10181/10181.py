


def backtrack(puzzle, index, moves):




def solve(puzzle):

    for index, num in enumerate(puzzle):
        if num == 0:
            backtrack(puzzle, index, [])
            break


def main():

    with open("inputs.txt") as infile:
        lines = infile.readlines()

    puzzle = [-1]
    for j, i in enumerate(lines[1:], start=1):
        puzzle.extend(map(int, i.strip().split()))
        if j % 4 == 0:
            solve(puzzle)
            puzzle = [-1]


if __name__ == '__main__':
    main()
