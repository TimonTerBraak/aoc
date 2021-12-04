from typing import List,Set

class Card:

    numbers : List[List[int]]
    on_card : Set[int]
    bingo: bool

    def __init__(self, numbers : List[List[int]]):
        self.numbers = numbers
        self.on_card = set()
        self.bingo = False
        for row in self.numbers:
            for cell in row:
                self.on_card.add(cell)

    def check_bingo(self, x: int, y: int) -> bool:
        # check for horizontal bingo
        h_bingo = len(list(filter(lambda v: v > 0, self.numbers[y]))) == 0
        v_bingo = len(list(filter(lambda row: row[x] > 0, self.numbers))) == 0
        return h_bingo or v_bingo

    def play(self, number) -> bool:
        if not number in self.on_card:
            return False

        for y, row in enumerate(self.numbers):
            for x, val in enumerate(row):
                if val == number:
                    self.numbers[y][x] = -number
                    bingo = self.check_bingo(x, y)
                    if bingo:
                        self.bingo = True
                    return bingo
