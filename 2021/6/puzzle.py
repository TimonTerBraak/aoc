from adventofcode import Part, LineReader

class Part1(Part):

    def solve(self, inputfile) -> int:
        with LineReader(inputfile).strings() as lines:
            lst = list(map(int,lines[0].split(',')))
            for d in range(80):
                born = list()
                for i,day in enumerate(lst):
                    if day == 0:
                        born.append(8)
                        lst[i] = 6
                    else:
                        lst[i] = lst[i] - 1
                lst = lst + born
            return len(lst)


class Part2(Part):

    def solve(self, inputfile) -> int:
        # initialize dictionary
        days = dict()
        for i in range(9):
            days[i] = 0

        # parse input
        with LineReader(inputfile).strings() as lines:
            lst = list(map(int,lines[0].split(',')))
            for l in lst:
                days[l] = days[l] + 1

        # calculate growth in constant memory and linear time        
        for d in range(256):
            new = days[0]
            for i in range(1,9):
                days[i-1] = days[i]
            days[6] = days[6] + new
            days[8] = new

        return sum(days.values())

