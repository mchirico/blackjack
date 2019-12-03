from itertools import cycle
import random


class Junk:
    def stuff(self):
        return "we stuff"


class Cards:
    deck = None
    cardPtr = None
    cardsDelt = -1

    def __init__(self):
        self.createCards()
        self.randomGen()

    def randomGen(self):
        random.seed = 42
        self.cardPtr = random.sample(range(52), 52)
        return self.cardPtr

    def createCards(self):
        suit = [s for s in "HCSD"]
        value = [v for v in "A23456789TJQK"]
        cards = []
        for s in suit:
            cards += list(zip(value, cycle(s)))
        self.cards = cards

    def dealCard(self):
        if self.cardsDelt > 52:
            return
        self.cardsDelt += 1
        return self.cards[self.cardPtr[self.cardsDelt]]


if __name__ == "__main__":
    cards = Cards()
    print(cards.dealCard())
    print(cards.dealCard())
    print(cards.dealCard())
