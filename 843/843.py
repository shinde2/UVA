

mapped = dict()


def word_matched(words, solution):

    return len(words) == len(solution)


def get_possibilities(words, solution, length):

    return [word for word in words if len(word) == length and word not in solution]


def backtrack(index, words, line, solution):

    global mapped

    if word_matched(words, solution):
        return
    else:
        index += 1
        possibilities = get_possibilities(words, solution, len(line[index]))
        for possibility in possibilities:
            temp = dict()
            for i, char in enumerate(possibility):
                if line[i] in mapped.keys() and line[i] != char:
                     break
                else:
                    temp.setdefault(line[i], char)
            else:
                mapped.update(temp)
                solution[index] = possibility


def decrypt(words, line):

    index = -1
    solution = [*] * len(line)

    backtrack(index, words, line, solution)

    return solution


def main():

    words = ["and", "dick", "jane", "puff", "spot", "yertle"]
    lines = [
        "bjvg xsb hxsn"
        #"bjvg xsb hxsn xsb qymm xsb rqat xsb pnetfn"
        #"xxxx yyy zzzz www yyyy aaa bbbb ccc dddddd"
    ]

    for line in lines:
        dec = decrypt(words, line.split())
        print(dec)


if __name__ == '__main__':
    main()
