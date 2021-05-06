# first solution is too slow for large integers

# second: find how many times given prime factor
#         appears in n!

def first():

    with open("inputs.txt") as i:
        lines = i.readlines()

    for line in lines:
        n, m = map(int, line.strip().split())

        f = n

        res = 1
        while f:
            if res == 0:
                break
            res *= f
            res %= m
            f -= 1

        if res == 0:
            print(f"{m} divides {n}!")
        else:
            print(f"{m} does not divide {n}!")


if __name__ == '__main__':
    first()
