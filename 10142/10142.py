# basic solution


def count_votes(indexed_ballots):

    candidate_count = dict()

    for ballot in indexed_ballots:
        try:
            candidate_count[ballot[1][ballot[0]]] += 1
        except:
            candidate_count[ballot[1][ballot[0]]] = 1

    return candidate_count


def is_winner(indexed_ballots):

    candidate_count = count_votes(indexed_ballots)

    for candidate, votes in candidate_count.items():
        if float(votes) > len(indexed_ballots)/2:
            return candidate

    return -1


def update_indices(indexed_ballots, losers):

    for loser in losers:
        for ballot in indexed_ballots:
            if ballot[1][ballot[0]] == loser:
                ballot[0] += 1


def get_losers(indexed_ballots):

    losers = list()
    min_votes = float("Inf")
    candidate_count = count_votes(indexed_ballots)

    for candidate, votes in candidate_count.items():
        if votes == min_votes:
            losers.append(candidate)
        elif votes < min_votes:
            del losers[:]
            losers.append(candidate)

    return losers


def set_current_winner(ballots):

    return [[0, ballot] for ballot in ballots]


def main():

    names = ["tie", "a", "b", "c"]

    ballots = [
        [1, 2, 3],
        [2, 1, 3],
        [2, 3, 1],
        [1, 2, 3]
        #[3, 1, 2]
    ]

    indexed_ballots = set_current_winner(ballots)

    winner = is_winner(indexed_ballots)

    while winner == -1:
        losers = get_losers(indexed_ballots)
        update_indices(indexed_ballots, losers)
        winner = is_winner(indexed_ballots)

    print(names[winner])


if __name__ == '__main__':
    main()
