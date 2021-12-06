from adventofcode import Part, LineReader
from parse import parse

class Part1(Part):

    def solve(self, inputfile):
        with LineReader(inputfile).strings() as lines:
            segments = []
            for line in lines:
                segments.append(list(map(int, parse('{},{} -> {},{}', line))))

            m = [[0 for i in range(1000)] for j in range(1000)]
            for x0,y0,x1,y1 in segments:
                if x0 == x1:
                    if y1 < y0:
                        y0, y1 = y1, y0

                    for y in range(y0, y1 + 1):
                        m[y][x0] = m[y][x0] + 1

                if y0 == y1:
                    if x1 < x0:
                        x0, x1 = x1, x0
                    for x in range(x0, x1 + 1):
                        m[y0][x] = m[y0][x] + 1
                    #print(f'({x0},{y0}) -> ({x1},{y1})')

            count = 0
            for row in m:
                for cell in row:
                    if cell >= 2:
                        count = count + 1
            return count

        return ""


class Part2(Part):

    def solve(self, inputfile):
        with LineReader(inputfile).strings() as lines:
            segments = []
            for line in lines:
                segments.append(list(map(int, parse('{},{} -> {},{}', line))))

            m = [[0 for i in range(1000)] for j in range(1000)]
            for x0,y0,x1,y1 in segments:
                if x0 == x1:
                    if y1 < y0:
                        y0, y1 = y1, y0
                    for y in range(y0, y1 + 1):
                        m[y][x0] = m[y][x0] + 1
                elif y0 == y1:
                    if x1 < x0:
                        x0, x1 = x1, x0
                    for x in range(x0, x1 + 1):
                        m[y0][x] = m[y0][x] + 1
                else:
                    if y1 < y0:
                        y0, y1 = y1, y0
                        x0, x1 = x1, x0
                    x = x0
                    for y in range(y0, y1 + 1):
                        m[y][x] = m[y][x] + 1
                        if x0 < x1:
                            x = x + 1
                        else:
                            x = x - 1
            count = 0
            for row in m:
                for cell in row:
                    if cell >= 2:
                        count = count + 1
            return count

        return ""
