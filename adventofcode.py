#!/usr/bin/env python3

from dataclasses import dataclass
import importlib
import os
import sys

class Part:

    def solve(self, inputfile):
        ...

@dataclass
class Puzzle:

    year: int
    day: int
    part1: Part
    part2: Part

    def __init__(self, year: int, day: int):
        self.year = year
        self.day = day

        module = importlib.import_module(f'{year}.{day}.puzzle')
        part1 = getattr(module, 'Part1')
        self.part1 = part1()
        part2 = getattr(module, 'Part2')
        self.part2 = part2()

    def solve(self):
        print(f'Puzzle: {self.year}-{self.day}')
        ans = self.part1.solve(os.path.join(self.year, self.day, 'example1.txt'))
        print(f'Ex.  1: {ans}')
        ans = self.part1.solve(os.path.join(self.year, self.day, 'input1.txt'))
        print(f'Part 1: {ans}')
        ans = self.part2.solve(os.path.join(self.year, self.day, 'example2.txt'))
        print(f'Ex.  2: {ans}')
        ans = self.part2.solve(os.path.join(self.year, self.day, 'input2.txt'))
        print(f'Part 2: {ans}')


def main():
    if len (sys.argv) < 3:
        print(f'Usage: {sys.argv[0]} <year> <day>')
    else:
        puzzle = Puzzle(year=sys.argv[1], day=sys.argv[2])
        puzzle.solve()

if __name__ == "__main__":
    main()

