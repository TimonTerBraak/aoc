from adventofcode import Part, LineReader

class Part1(Part):

    def growrate(self, inputfile, days) -> int:
        with LineReader(inputfile).strings() as lines:
            lst = list(map(int,lines[0].split(',')))
            for d in range(days):
                born = list()
                for i,day in enumerate(lst):
                    if day == 0:
                        born.append(8)
                        lst[i] = 6
                    else:
                        lst[i] = lst[i] - 1
                lst = lst + born
                #print(f'After {d+1} day(s): {lst}')
            return len(lst)
        return 0

    def solve(self, inputfile) -> int:
        return self.growrate(inputfile, 80)


class Part2(Part1):

    def solve(self, inputfile):
        return self.growrate(inputfile, 256)
