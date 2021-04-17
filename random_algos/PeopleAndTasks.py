from RightMost import RightMostUnset
from collections import defaultdict
from pprint import pprint as print


class PeopleAndTasks:

    def __init__(self, cost):

        self.cost = cost
        self.N = len(self.cost)
        self.DP = None
        self.ALLMASK = (1 << self.N) - 1
        self.allocation = defaultdict()
        self.init_dp()

    def init_dp(self):

        self.DP = [[-1 for _ in range(self.N)] for _ in range(2 ** self.N)]

    def count_cost(self, mask, task):

        if mask == self.ALLMASK:
            return 0
        elif self.DP[mask][task] != -1:
            return self.DP[mask][task]
        else:
            #cost = min([self.count_cost(mask | (1 << i), task+1) + self.cost[i][task]
            #            for i in RightMostUnset(mask, self.N)])
            #self.DP[mask][task] = cost
            #return cost

            min_cost = float("Inf")
            index = -1
            for i in RightMostUnset(mask, self.N):
                cost = self.count_cost(mask | (1 << i), task+1) + self.cost[i][task]
                if cost < min_cost:
                    min_cost = cost
                    index = i
            self.allocation[index] = task
            self.DP[mask][task] = min_cost
            return min_cost


def main():

    cost = [
        [2, 3, 6, 10],
        [2, 1, 7, 1],
        [4, 1, 3,  5],
        [20, 20, 20, 20]
    ]

    peopleandtasks = PeopleAndTasks(cost)
    print(peopleandtasks.count_cost(0, 0))
    print(peopleandtasks.allocation)


if __name__ == '__main__':
    main()
