from math import floor


def gcd(a, b):

    if a < b:
        return gcd(b, a)

    if b == 0:
        return a, 1, 0

    _a = b
    _b = a - (floor(a/b) * b)  # a % b

    g, _x, _y = gcd(_a, _b)

    x = _y
    y = _x - (floor(a/b)*_y)

    return g, x, y


def main():

    a = 34398
    b = 2132

    g, x, y = gcd(a, b)

    print(g, x, y)


if __name__ == '__main__':
    main()
