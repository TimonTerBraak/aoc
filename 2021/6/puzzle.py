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
        days = dict.fromkeys([0,1,2,3,4,5,6,7,8], 0)

        # parse input
        with LineReader(inputfile).strings() as lines:
            lst = list(map(int,lines[0].split(',')))
            for l in lst:
                days[l] = days[l] + 1

        # calculate growth in constant memory and linear time        
        for _ in range(256):
            new = days[0]
            for day, count in days.items():
                if day > 0:
                    days[day - 1] = days[day]
            days[6] = days[6] + new
            days[8] = new

        return sum(days.values())

