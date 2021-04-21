# simpler way is to generate fibs once and count
# them for each query.
# below solution tries approximate method and
# answer is off by one for some tests


def NumFibs(a, b):

    if a == 0 and b == 0:
        return

    if a == b or a+1 == b:
        print("0")
        return

    if a == 0:
        prev = 0
        a = 1
    else:
        if a % 2 == 0:
            prev = a/2 - 1
        else:
            prev = (a+1)/2 - 1

    count = 0
    curr = prev + a

    while curr <= b:
        count += 1
        prev = a
        a = curr
        curr = prev + a

    print(count)


def main():

    with open("inputs.txt") as infile:
        lines = infile.readlines()

    for line in lines:
        NumFibs(*map(int, line.strip().split()))


if __name__ == '__main__':
    main()
