
def validate(grid, lenght, x, y):

    r = len(grid)
    c = len(grid[0])

    #directions = [
    #    (-1, 0), (1, 0), (0, -1), (0, 1),
    #    (-1, -1), (-1, 1), (1, -1), (1, 1)
    #]

    directions = list()

    if x-lenght >= 0:
        directions.append((-1, 0))
    if x+lenght < r:
        directions.append((1, 0))
    if y+lenght < c:
        directions.append((0, 1))
    if y-lenght >= 0:
        directions.append((0, -1))

    if (0, -1) in directions and (-1, 0) in directions:
        directions.append((-1, -1))
    if (0, 1) in directions and (-1, 0) in directions:
        directions.append((-1, 1))
    if (1, 0) in directions and (0, -1) in directions:
        directions.append((1, -1))
    if (0, 1) in directions and (1, 0) in directions:
        directions.append((1, 1))

    return directions


def word_exists(grid, word, x, y, u, v):

    def word_gen():
        nonlocal x
        nonlocal y
        s = ""
        for _ in range(0, len(word)):
            s += grid[x][y]
            x += u
            y += v
        return s

    si = iter(word_gen())
    for char in word:
        if char.lower() != next(si).lower():
            return False
    else:
        return True


def check_grid_point(grid, word, r, c):



def find_word(grid, words):

    found_words = dict()

    for word in words:
        def r_loop():
            for r, row in enumerate(grid):
                def c_loop():
                    for c, columns in enumerate(row):
                        directions = validate(grid, len(word), r, c)
                        if directions:
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
        n = int(lines[i+r+1].rstrip())
        for _n in range(1, n+1):
            words.append(lines[i+r+1+_n].rstrip())
        cases.append([grid, words])
        i = i + r + 1 + n + 1 + 1

    for case in cases:
        find_word(*case)


if __name__ == '__main__':
    main()
