

def lands(n):

    c = (n * (n-1)) / 2


def main():

    with open("inputs.txt") as infile:
        lines = infile.readlines()

    for line in lines[1:]:
        lands(int(line.strip()))


if __name__ == '__main__':
    main()
