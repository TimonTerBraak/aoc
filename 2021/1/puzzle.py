from adventofcode import Part, LineReader
import sys

class Part1(Part):

    def solve(self, inputfile):
        with LineReader(inputfile).integers() as lines:
            pairs = zip(lines, lines[1:])
            return sum([1 if i < j else 0 for i, j in pairs])


class Part2(Part):

    def solve(self, inputfile):
        count = 0
        with LineReader(inputfile).integers() as lines:
            quads = zip(lines, lines[1:], lines[2:], lines[3:])
            return sum([1 if (b + c + d) > (a + b + c) else 0 for a, b, c, d in quads])


