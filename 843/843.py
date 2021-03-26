

def word_matched(index, word, words):

    return word if len(word) == index+1 and "".join(word) in words else False


def get_possibilities(index, word, chars, mapped):

    if index < len(word):
        if word[index] in mapped.keys():
            word[index] = mapped.get(word[index])
            return list()
        else:
            return list(set(chars)-set(mapped.values()))
    else:
        return list()


def backtrack(index, word, chars, mapped, demapped, words):

    if word_matched(index, word, words):
        return word
    else:
        index += 1
        possibilities = get_possibilities(index, word, chars, mapped)
        for possibility in possibilities:
            mapped.setdefault(word[index], possibility)
            demapped.setdefault(possibility, word[index])
            word[index] = possibility
            found = backtrack(index, word, chars, mapped, demapped, words)
            if found:
                return found
            else:
                k = demapped.get(possibility)
                word[index] = k
                del demapped[possibility]
                del mapped[k]


def _back(lines, index, chars, mapped, demapped, words):

    for line in lines:
        for word in line.split():
            w = backtrack(index, list(word), chars, mapped, demapped, words)
            print(w)


def decrypt(words, lines):

    chars = list()
    mapped = dict()
    demapped = dict()
    index = -1

    for word in words:
        for char in word:
            if char not in chars:
                chars.append(char)

    _back(lines, index, chars, mapped, demapped, words)


def main():

    #words = ["and", "dick", "jane", "puff", "spot", "yertle"]
    words = ["dick"]
    lines = [
        "bjvg"
        #"bjvg xsb hxsn xsb qymm xsb rqat xsb pnetfn"
        #"xxxx yyy zzzz www yyyy aaa bbbb ccc dddddd"
    ]

    decrypt(words, lines)


if __name__ == '__main__':
    main()