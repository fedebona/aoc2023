# Advent of Code 2023 Day 21

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



def p(map, moves):

    sp = starting_point(map, "S")
    valid_points = set()
    valid_points.add(sp)

    moves_list = [sp]
    for i in range(0, moves):
        new_moves_list = []
        valid_points = set()
        for p in moves_list:
            borders = get_border(map, p)
            new_moves_list += borders
            valid_points = valid_points.union(borders)
        moves_list = new_moves_list

    # print ([(p.x, p.y) for p in valid_points])

    # for p in valid_points:
    #     change_map_value(map, p, "O")
    # print("\n".join(map))   

    #Parte 2
    # prima mettere a 0 i vuoti che partono dai bordi e svuoto i tile che non sono parte del main loop
 

    return {"p1": len(valid_points), "p2": 0}

def count_symbols(map, symbol):
    count = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == symbol:
                count += 1
    return count

def change_map_value(map, p, value):
    s_list = list( map[p.y])
    s_list[p.x] = value
    map[p.y] = ''.join(s_list)


def get_border(map, p):
    borders = []
    if(p.y > 0) and (map[p.y-1][p.x] != "#"):
        borders.append(Point(p.x, p.y-1))
    if(p.y < len(map) - 1) and (map[p.y+1][p.x] != "#"):
        borders.append(Point(p.x, p.y+1))
    if(p.x > 0) and (map[p.y][p.x-1] != "#"):
        borders.append(Point(p.x-1, p.y))
    if(p.x < len(map[p.y]) - 1) and (map[p.y][p.x+1] != "#"):
        borders.append(Point(p.x+1, p.y))
    return borders

def readallmap(f):
    map = []
    for line in f:
        map.append(line.strip())
    return map


def starting_point(map, symbol):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if (map[y][x] == symbol):
                return Point(x, y)
    return None


f = open("resources\day21.txt", "r")
map = readallmap(f)
res = p(map,64)
print("Output: " + f"Part 1: {res['p1']}, Part 2: {res['p2' ]}")
f.close()
