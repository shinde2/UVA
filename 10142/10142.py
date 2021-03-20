
def count_votes(ballots):

    votes = dict()

    for ballot in ballots:
        try:
            votes[ballot[0]] += 1
        except:
            votes[ballot[0]] = 1

    return votes


def vote(names, ballots):

    index_to_name = dict()

    for index, name in enumerate(names):
        index_to_name.setdefault(index+1, name)

    votes = count_votes(ballots)


def main():

    names = ["a", "b", "c"]

    ballots = [
        [1, 2, 3],
        [2, 1, 3],
        [2, 3, 1],
        [1, 2, 3],
        [3, 1, 2]
    ]

    vote(names, ballots)


if __name__ == '__main__':
    main()