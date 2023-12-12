# Advent of Code 2023 Day 11
from itertools import combinations

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

    def delta(self, other):
        #return range di x e range di y
        return {"dx":range(min(self.x, other.x), max(self.x, other.x)), "dy":range(min(self.y, other.y), max(self.y, other.y))}

empty_rows_weight = 1000000
empty_cols_weight = 1000000

def p1(map):  

    map = expand_rows_map(map)
    map = transpose_matrix(map)
    map = expand_rows_map(map)  
    map = transpose_matrix(map)

    #Replace # with sequence number
    sequence = 0
    galaxies = {}
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "#":
                sequence += 1
                map[y][x] = sequence
                galaxies[sequence] = Point(x, y)
    #couples
    elements = [i+1 for i in range(sequence)]
    couples = list(combinations(elements, 2))
    distances = []
    for c in couples:
        distances.append((galaxies[c[0]].distance(galaxies[c[1]])))
    #print (distances)
    return {"p1": sum(distances)}

#Part 2 risolve anche part 1 usando tabelle di weights
def p2(map):  
    weights = [[1]*len(map) for i in range(len(map[0]))]
    calculate_weights_map(map, weights, empty_rows_weight)
    map = transpose_matrix(map)
    weights = transpose_matrix(weights)
    calculate_weights_map(map, weights, empty_cols_weight)
    map = transpose_matrix(map)
    weights = transpose_matrix(weights)

    #Replace # with sequence number
    sequence = 0
    galaxies = {}
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "#":
                sequence += 1
                map[y][x] = sequence
                galaxies[sequence] = Point(x, y)
    #couples
    elements = [i+1 for i in range(sequence)]
    couples = list(combinations(elements, 2))
    distances = []
    for c in couples:
        distances.append((calculate_couple_distance(map, weights, c, galaxies)))
    #print (distances)
    return {"p2": sum(distances)}

def calculate_couple_distance(map, weights, couple, galaxies):
    distances = []
    #print (couple)
    delta = galaxies[couple[0]].delta(galaxies[couple[1]])
    for y in delta["dy"]:
        distances.append(weights[y][galaxies[couple[0]].x])
    for x in delta["dx"]:
        distances.append(weights[galaxies[couple[0]].y][x])
    #print (distances)
    return sum(distances)

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def reverse_transpose_matrix(matrix):
    return [(list(row)[::-1]) for row in zip(*matrix)]

def expand_rows_map(map):
    new_map = []
    for row in map:
        new_map.append(row)
        if row.count(".") == len(row):
            new_map.append(["."] * len(row))
    return new_map

def calculate_weights_map(map, weights, base_weight):
    for y in range(len(map)):
        if map[y].count(".") == len(map[y]):
            for x in range(len(map[y])):
                curr = weights[y][x]
                weights[y][x] *= base_weight

def readallmap(f):
    map = []
    for line in f:
        map.append(list(line.strip()))
    return map

f = open("resources\day11.txt", "r")
map = readallmap(f)
res1 = p1(map)
f.seek(0)
map = readallmap(f)
res2 = p2(map)

print("Output: " + f"Part 1: {res1['p1']}, Part 2: {res2['p2' ]}")
f.close()
