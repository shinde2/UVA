

def get_char_dict(words):

    char_dict = dict()

    for word in words:
        for char in word:
            char_dict.setdefault(char, None)

    return char_dict


def decrypt(words, lines):

    char_dict = get_char_dict(words)





def main():

    words = ["and", "dick", "jane", "puff", "spot", "yertle"]
    lines = [
        "bjvg xsb hxsn xsb qymm xsb rqat xsb pnetfn",
        "xxxx yyy zzzz www yyyy aaa bbbb ccc dddddd"
    ]

    decrypted = decrypt(words, lines)


if __name__ == '__main__':
    main()