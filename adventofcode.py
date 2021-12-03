#!/usr/bin/env python3
from typing import List, Tuple, Any
from dataclasses import dataclass
from contextlib import contextmanager
import importlib
import os
import sys
import time
import abc

class LineReader:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    @contextmanager
    def integers(self) -> List[int]:
        try:
            file = open(self.filename, 'r')
            yield [int(i) for i in file.read().split('\n')[:-1]]
        finally:
            file.close()

    @contextmanager
    def strings(self) -> List[str]:
        try:
            file = open(self.filename, 'r')
            yield file.read().split('\n')[:-1]
        finally:
            file.close()

    @contextmanager
    def moves(self) -> List[Tuple[str, int]]:
        try:
            file = open(self.filename, 'r')
            moves = file.read().split('\n')[:-1]
            pairs = [tuple(m.split(' ')) for m in moves]
            yield [(m, int(c)) for m, c in pairs]
        finally:
            file.close()


class Part:

    @abc.abstractmethod
    def solve(self, inputfile: str) -> Any:
        raise NotImplementedError


@dataclass
class Puzzle:

    year: int
    day: int
    part1: type
    part2: type

    def __init__(self, year: int, day: int) -> None:
        self.year = year
        self.day = day

        module = importlib.import_module(f'{year}.{day}.puzzle')
        self.part1 = getattr(module, 'Part1')
        self.part2 = getattr(module, 'Part2')

    def solve(self) -> None:
        print(f'Puzzle: {self.year}-{self.day}')
        ans = self.part1().solve(os.path.join(self.year, self.day, 'example1.txt'))
        print(f'Ex.  1: {ans}')
        ans = self.part1().solve(os.path.join(self.year, self.day, 'input1.txt'))
        print(f'Part 1: {ans}')
        ans = self.part2().solve(os.path.join(self.year, self.day, 'example2.txt'))
        print(f'Ex.  2: {ans}')
        ans = self.part2().solve(os.path.join(self.year, self.day, 'input2.txt'))
        print(f'Part 2: {ans}')


def main() -> None:
    if len(sys.argv) < 3:
        print(f'Usage: {sys.argv[0]} <year> <day>')
    else:
        start = time.time()
        puzzle = Puzzle(year=sys.argv[1], day=sys.argv[2])
        puzzle.solve()
        print(f'Timing: {time.time() - start} s')

if __name__ == "__main__":
    main()
