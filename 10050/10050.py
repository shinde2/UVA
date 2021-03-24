from math import ceil


def hartal(params):

    lost = 0
    days = params[0]

    weeks = [[0]*6 for _ in range(int(ceil(days/7))+1)]

    for party in params[1:]:
        i = party
        while i <= days:
            d = i % 7
            w = int(ceil(i/7))
            if d != 6 and d != 7:
                weeks[w][d] = 1
            i += party

    for week in weeks[1:]:
        for day in week[1:]:
            if day == 1:
                lost += 1

    print(lost)


def main():

    params = [100, 12, 15, 25, 40]

    hartal(params)


if __name__ == '__main__':
    main()
