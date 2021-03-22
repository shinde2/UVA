

def set_current_winner(ballots):

    return [(0, ballot) for ballot in ballots]


def main():

    names = ["a", "b", "c"]

    ballots = [
        [1, 2, 3],
        [2, 1, 3],
        [2, 3, 1],
        [1, 2, 3],
        [3, 1, 2]
    ]

    indexed_ballots = set_current_winner(ballots)
    print(indexed_ballots)


if __name__ == '__main__':
    main()