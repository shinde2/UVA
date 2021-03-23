

def is_jolly(numbers):

    if len(numbers) == 1:
        print("Jolly")
    else:
        i = 0
        j = True
        while i < len(numbers)-1:
            if abs(numbers[i+1]-numbers[i]) not in range(0, len(numbers)):
                j = False
                break
            i += 1
        if j:
            print("Jolly")
        else:
            print("Not jolly")


def main():

    #numbers = [
    #    [1, 4, 2, 3],
    #    [1, 4, 2, -1, 6]
    #]

    numbers = list()

    with open("tests.txt") as f:
        lines = f.readlines()

    for line in lines:
        l = list(map(int, line.rstrip().split()))
        numbers.append(l[1:])

    for number in numbers:
        is_jolly(number)


if __name__ == '__main__':
    main()