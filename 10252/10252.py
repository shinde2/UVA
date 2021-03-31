# tests passed

# current sloution is n2


def check(first, second):

    substring = list()

    for char in first:
        if char in second:
            substring.append(char)

    print(f"{''.join(substring)}")


def main():

    with open("tests.txt") as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        s1 = sorted(lines[i].rstrip())
        s2 = sorted(lines[i+1].rstrip())
        if len(s1) <= len(s2):
            check(s1, s2)
        else:
            check(s2, s1)
        i += 2


if __name__ == '__main__':
    main()
