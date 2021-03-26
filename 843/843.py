

mapped = dict()


def word_matched(index, line):

    return index == len(line)-1


def get_possibilities(words, solution, line, index):

    global mapped
    possibilities = list()

    for word in words:
        if len(word) == len(line[index]):
            for i, char in enumerate(word):
                if line[index][i] in mapped.keys() and mapped.get(line[index][i]) != char:
                    break
            else:
                possibilities.append(word)

    return possibilities


def backtrack(index, words, line, solution):

    global mapped

    if word_matched(index, line):
        return 0
    else:
        index += 1
        possibilities = get_possibilities(words, solution, line, index)
        for possibility in possibilities:
            temp = list()
            for i, char in enumerate(possibility):
                if line[index][i] not in mapped.keys():
                    mapped.setdefault(line[index][i], char)
                    temp.append(line[index][i])
            solution[index] = possibility
            ret = backtrack(index, words, line, solution)
            if ret == 0:
                return ret
            else:
                for k in temp:
                    del mapped[k]
        return -1


def decrypt(words, line):

    index = -1
    solution = ["*"] * len(line)

    backtrack(index, words, line, solution)

    return solution


def main():

    words = ["and", "dick", "jane", "puff", "spot", "yertle"]
    lines = [
        "bjvg xsb hxsn xsb qymm xsb rqat xsb pnetfn",
        "xxxx yyy zzzz www yyyy aaa bbbb ccc dddddd"
    ]

    for line in lines:
        dec = decrypt(words, line.split())
        print(dec)


if __name__ == '__main__':
    main()
