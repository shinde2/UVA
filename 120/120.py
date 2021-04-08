
def reverse(current, start, end):

    while start < end:
        t = current[start]
        current[start] = current[end]
        current[end] = t
        start += 1
        end -= 1


def done(current):

    for i, j in enumerate(current):
        if len(current)-i != j:
            return False
    return True


def flip(current, seq, index):

    if done(current):
        seq.append(0)
        return
    else:
        largest = index
        for i, elm in enumerate(current[index:], start=index):
            if len(current) - i != elm and elm >= current[largest]:
                largest = i

        if largest != len(current)-1:
            seq.append(largest+1)
            reverse(current, largest, len(current)-1)

        seq.append(index+1)
        reverse(current, index, len(current)-1)
        index += 1

        flip(current, seq, index)


def main():

    pancakes = list()

    with open("tests.txt") as f:
        lines = f.readlines()

    for line in lines:
        pancakes.append([int(c) for c in line.rstrip().split(" ")[::-1]])

    for pancake in pancakes:
        seq = list()
        print(" ".join(map(str, pancake[::-1])))
        flip(pancake, seq, 0)
        print(" ".join(map(str, seq)))


if __name__ == '__main__':
    main()
