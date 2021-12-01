from adventofcode import Puzzle, Part
import sys

class Part1(Part):

    def __init__(self):
        ...

    def solve(self, inputfile):
        count = 0
        with open(inputfile, "r") as f:
            previous_depth = 999999999999999
            for l in f.readlines():
                depth = int(l.rstrip('\n'))
                if depth > previous_depth:
                    count = count + 1
                previous_depth = depth
            
        return count


class Part2(Part):

    def __init__(self):
        ...

    def solve(self, inputfile):
        count = 0
        with open(inputfile, "r") as f:
            lines = f.read().split('\n')[:-1]
            previous_sum = 999999999999999
            for x, n in enumerate(lines[2:], start=2):
                a = int(lines[x - 2])
                b = int(lines[x - 1])
                c = int(lines[x - 0])
                if (a + b + c) > previous_sum:
                    count = count + 1
                previous_sum = a + b + c
            
        return count
