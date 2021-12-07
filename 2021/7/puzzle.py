from adventofcode import Part, LineReader

class Part1(Part):

    def fuel(self, a: int, b: int) -> int:
        return abs(a - b)

    def solve(self, inputfile) -> int:
        min_fuel = 99999999999
        with LineReader(inputfile).fields() as fields:
            total = len(fields)
            positions = list(map(int, fields))
            for t in range(max(positions) + 1):
                fuel = 0
                for p in positions:
                    fuel = fuel + self.fuel(p, t)
                if fuel < min_fuel:
                    min_fuel = fuel
        return min_fuel


class Part2(Part1):

    def fuel(self, a: int, b: int) -> int:
        return sum(range(abs(a - b) + 1))
