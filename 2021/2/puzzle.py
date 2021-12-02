from dataclasses import dataclass
from adventofcode import Puzzle, Part, LineReader
from submarine import Submarine

class Part1(Part, Submarine):

    def forward(self, dx: int):
        self.x = self.x + dx

    def down(self, d: int):
        self.z = self.z + d

    def up(self, d: int):
        self.z = self.z - d

    def solve(self, inputfile):
        with LineReader(inputfile).moves() as moves:
            for m, c in moves:
                self.move(m, c)
        return self.x * self.z


class Part2(Part1, Submarine):

    aim: int = 0

    def forward(self, dx: int):
        super().forward(dx)
        self.z = self.z + (self.aim * dx)

    def down(self, d: int):
        self.aim = self.aim + d

    def up(self, d: int):
        self.aim = self.aim - d


