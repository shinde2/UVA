from dataclasses import dataclass

MAXDIGITS = 10


@dataclass
class BigNum:

    digits = list()
    sign = "+"
    lastdigit = MAXDIGITS - 1


def main():

    num = BigNum()
    print(num)


if __name__ == '__main__':
    main()
