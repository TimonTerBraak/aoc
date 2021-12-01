from adventofcode import Puzzle, Part

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
        return ""
