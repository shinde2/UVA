
def exchanged(trip):

    n = len(trip)
    money = 0

    average_cost = sum(trip)/float(n)
    #average_cost = round(average_cost, 2)

    for cost in trip:
        if cost < average_cost:
            money += average_cost - cost

    return f"${round(money, 2)}"


def main():

    #trip = [15.00, 15.01, 3.00, 3.01]
    #money = exchanged(trip)
    #print(money)

    trips = list()

    with open("tests.txt") as f:
        line = f.readline().rstrip()
        while line != "0":
            num = int(line)
            temp = list()
            while num:
                temp.append(float(f.readline().rstrip()))
                num -= 1
            trips.append(temp)
            line = f.readline().rstrip()

    for trip in trips:
        print(exchanged(trip))


if __name__ == "__main__":
    main()
