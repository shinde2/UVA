

def word_exists(grid, word, x, y, u, v):

    def word_gen():
        nonlocal x
        nonlocal y
        for _ in range(0, len(word)):
            yield grid[x][y]
            x += u
            y += v

    for char in word:
        if char != next(word_gen()):
            return False
    else:
        return True


def find_word(grid, words):

    found_words = dict()
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    for word in words:
        def r_loop():
            for r, row in enumerate(grid):
                def c_loop():
                    for c, columns in enumerate(row):
                        #validate(grid, len(word), r, c)
                        def dir_loop():
                            for u, v in directions:
                                if word_exists(grid, word, r, c, u, v):
                                    found_words.setdefault(word, (u, v))
                                    return True
                            else:
                                return None
                        if dir_loop():
                            return True
                if c_loop():
                    return True
        if r_loop():
            break

    for word in words:
        print(found_words.get(word))


def main():

    cases = list()

    with open("tests.txt") as f:
        lines = f.readlines()

    i = 2
    while i < len(lines):
        r, _ = map(int, lines[i].rstrip().split())
        grid = list()
        words = list()
        for _r in range(1, r+1):
            grid.append(list(lines[i+_r].rstrip()))
        n = int(lines[i+_r+1].rstrip())
        for _n in range(1, n+1):
            words.append(lines[i+_n].rstrip())
        cases.append([grid, words])
        i = i + r + 1 + n + 1 + 1

    print(cases)

    for case in cases:
        find_word(*case)


if __name__ == '__main__':
    main()
