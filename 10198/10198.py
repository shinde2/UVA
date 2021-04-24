

total = 0


def sum_reached(index, s, curr):

    S = sum(curr[:index+1])
    if S == s:
        global total
        total += 1
        return True
    elif S > s:
        return True
    else:
        return False


def counting(index, s, curr):

    if sum_reached(index, s, curr):
        return
    else:
        index += 1
        possibilities = [1, 1, 2, 3]

        for possibility in possibilities:
            try:
                curr[index] = possibility
            except:
                curr.append(possibility)
            counting(index, s, curr)


def main():

    index = -1
    global total

    counting(index, 3, [])

    print(total)


if __name__ == '__main__':
    main()
