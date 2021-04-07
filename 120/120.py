

def _flip_1(pancake, count):

    if count:
        ps = count[0]
    else:
        ps = 0

    for index, cake in enumerate(pancake[ps:], start=ps):
        if index != cake:
            count.append(index)
            start = index
            end = len(pancake) - 1
            while start < end:
                t = pancake[start]
                pancake[start] = pancake[end]
                pancake[end] = t
                start += 1
                end -= 1
            return _flip_1(pancake, count)

    return count


def flip_1(pancake):

    for index, cake in enumerate(pancake, start=1):
        if index != cake:
            count = _flip_1(pancake, [])
            print(" ".join(pancake))
            print(" ".join(count))
            break
    else:
        print(" ".join(pancake))
        print("0")


def main():

    pancakes = list()

    with open("tests.txt") as f:
        lines = f.readlines()

    for line in lines:
        pancakes.append([int(c) for c in line.rstrip()[::-1]])

    for pancake in pancakes:
        flip_1(pancake)


if __name__ == '__main__':
    main()
