from adventofcode import Part, LineReader
from typing import Tuple

class Part1(Part):

    def diagnose(self, lines) -> Tuple[str, str]:
        cols = list()
        for line in lines:
            for c in range(len(line)):
                try:
                    cols[c] = cols[c] + int(line[c])
                except IndexError:
                    cols.append(int(line[c]))

        half = len(lines)/2
        gamma = ''.join(['1' if c >= half else '0' for c in cols])
        epsilon = ''.join(['1' if c < half else '0' for c in cols])

        return gamma, epsilon

    def solve(self, inputfile) -> int:
        with LineReader(inputfile).strings() as lines:
            gamma, epsilon = self.diagnose(lines)
            return int(gamma, 2) * int(epsilon, 2)


class Part2(Part1):

    def solve(self, inputfile) -> int:
        with LineReader(inputfile).strings() as lines:
            oxygen_generator = lines
            c02_scrubber = lines

            pos = 0
            while len(oxygen_generator) > 1:
                gamma, _ = self.diagnose(oxygen_generator)
                oxygen_generator = list(filter(lambda l: l[pos] == gamma[pos], oxygen_generator))
                pos = pos + 1

            pos = 0
            while len(c02_scrubber) > 1:
                _, epsilon = self.diagnose(c02_scrubber)
                c02_scrubber = list(filter(lambda l: l[pos] == epsilon[pos], c02_scrubber))
                pos = pos + 1

            return int(oxygen_generator[0], 2) * int(c02_scrubber[0], 2)
