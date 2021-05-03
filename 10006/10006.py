# a^n mod n


def main():

    a = 4
    n = 12
    N = 12

    res = a
    while N-1:
        res = res * a
        res = res % n
        N -= 1

    print(res)


if __name__ == '__main__':
    main()
