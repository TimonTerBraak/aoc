from adventofcode import Part, LineReader

class Part1(Part):

    def solve(self, inputfile) -> int:
        min_fuel = 99999999999
        with LineReader(inputfile).fields() as fields:
            total = len(fields)
            positions = list(map(int, fields))
            for t in range(max(positions) + 1):
                fuel = 0
                for p in positions:
                    fuel = fuel + abs(p - t)
                if fuel < min_fuel:
                    min_fuel = fuel
        return min_fuel


class Part2(Part):

    def solve(self, inputfile) -> int:
        min_fuel = 99999999999
        with LineReader(inputfile).fields() as fields:
            total = len(fields)
            positions = list(map(int, fields))
            for t in range(max(positions) + 1):
                fuel = 0
                for p in positions:
                    fuel = fuel + sum(range(abs(p - t) + 1))
                if fuel < min_fuel:
                    min_fuel = fuel
        return min_fuel
