'''

There are 100 different types of caps each having a unique id from 1 to 100.
Also, there are ‘n’ persons each having a collection of a variable number of caps.
One day all of these persons decide to go in a party wearing a cap but to look,
unique they decided that none of them will wear the same type of cap.
So, count the total number of arrangements or ways such that none of them is wearing the same type of cap.

Constraints: 1 <= n <= 10 Example

'''

from pprint import pprint as print
from collections import defaultdict


class PeopleAndCaps:

    def __init__(self, nPeople):

        self.DP = None
        self.CAPS = defaultdict(list)
        self.ALLMASK = None
        self.nCaps = 100
        self.nPeople = nPeople

    def init_dp(self, caps):

        self.ALLMASK = (1 << self.nPeople) - 1

        self.DP = [[-1 for _ in range(self.nCaps+1)] for _ in range(2 ** self.nPeople)]

        for person, _caps in enumerate(caps):
            for cap in _caps:
                self.CAPS[cap].append(person)

    def CountWays(self, mask, cap):

        if mask == self.ALLMASK:
            return 1

        if cap > self.nCaps:
            return 0

        if self.DP[mask][cap] != -1:
            return self.DP[mask][cap]

        ways = self.CountWays(mask, cap+1)

        for person in self.CAPS[cap]:
            if not mask & (1 << person):
                ways += self.CountWays(mask | (1 << person), cap+1)

        self.DP[mask][cap] = ways

        return ways


def main():

    with open("peopleandcaps.txt") as f:
        lines = f.readlines()

    nPeople = len(lines)
    caps = [map(int, line.strip().split()) for line in lines]

    peoppleandcaps = PeopleAndCaps(nPeople)
    peoppleandcaps.init_dp(caps)
    ways = peoppleandcaps.CountWays(0, 1)

    print(ways)


if __name__ == '__main__':
    main()
