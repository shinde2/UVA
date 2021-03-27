from collections import OrderedDict
from copy import deepcopy


def game(cards, shuffles):

    for shuffle in shuffles:
        temp = deepcopy(cards)
        for i, c in enumerate(shuffle[1:]):
           cards[i+1] = temp.get(c)

    print(cards)


def main():

    def get_cards():
       for i in range(1, 6):
           yield i

    cards = OrderedDict((k, k) for k in get_cards())
    print(cards)

    shuffles = [
        [0, 2, 1, 3, 4, 5],
        [0, 5, 1, 2, 3, 4]
    ]

    game(cards, shuffles)


if __name__ == '__main__':
    main()
