# Advent of Code 2023 Day 11


# Class representing a point in the map
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} , {self.y}"

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def add(self, other):
        if other is None:
            return self
        return Point(self.x + other.x, self.y + other.y)
    
    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

def p(map):  
    map = expand_rows_map(map)
    map = expand_cols_map(map)  
    return {"p1": 0, "p2": 0}

def expand_rows_map(map):
    new_map = []
    for row in map:
        new_map.append(row)
        if row.count(".") == len(row):
            new_map.append("." * len(row))
    return new_map

def expand_cols_map(map):
    new_map = []
    width = len(map[0])
    for x in range(width):
        if([map[y][x] for y in range(width)].count(".") == width):
            for y in range(width):
                new_map.append((map[y][0::x] if x>0 else "" )+ "." + (map[y][x+1::width-1] if x<width-1 else ""))
    return new_map

def readallmap(f):
    map = []
    for line in f:
        map.append(line.strip())
    return map

f = open("resources\day11_test.txt", "r")
map = readallmap(f)
res = p(map)
print("Output: " + f"Part 1: {res['p1']}, Part 2: {res['p2' ]}")
f.close()
