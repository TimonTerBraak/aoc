from adventofcode import Puzzle, Part, LineReader

class Part1(Part):

    def solve(self, inputfile):
        x = 0
        d = 0
        with LineReader(inputfile).moves() as moves:
            for m, c in moves:
                if m == "forward":
                    x = x + c
                elif m == "down":
                    d = d + c
                elif m == "up":
                    d = d - c
        return x * d


class Part2(Part):

    def solve(self, inputfile):
        x = 0
        d = 0
        a = 0
        with LineReader(inputfile).moves() as moves:
            for m, c in moves:
                if m == "forward":
                    x = x + c
                    d = d + (a * c)
                elif m == "down":
                    a = a + c
                elif m == "up":
                    a = a - c
        return x * d
