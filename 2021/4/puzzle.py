from adventofcode import Part, LineReader
from bingo import Card
from typing import List, Set

class Part1(Part):

    cards: List[Card]
    numbers: List[int]

    def parse(self, inputfile):
        self.cards = list()

        with LineReader(inputfile).strings() as lines:
            self.numbers = list(map(int,lines[0].split(',')))

            for l in range(2, len(lines),6):
                card = [list(map(int, l.split())) for l in lines[l:l+5]]
                self.cards.append(Card(card))
 
    def score(self, card: Card, n: int) -> int:
        return sum([sum(filter(lambda x: x > 0, row)) for row in card.numbers]) * n

    def solve(self, inputfile):
        self.parse(inputfile)
        for n in self.numbers:
            for c in self.cards:
                # check for bingo on this card
                if c.play(n):
                    return self.score(c, n)

        return "?"


class Part2(Part1):

    def solve(self, inputfile):
        self.parse(inputfile)

        no_bingo = set()
        for i, _ in enumerate(self.cards):
            no_bingo.add(i)

        for n in self.numbers:
            for i in no_bingo.copy():
                c = self.cards[i]
                # check for bingo on this card
                if not c.bingo and c.play(n):
                    if len(no_bingo) == 1:
                        return self.score(c, n)
                    no_bingo.remove(i)

        return "?"
