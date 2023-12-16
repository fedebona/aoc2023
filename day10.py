# Advent of Code 2023 Day 10

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


compatible_symbols = {
    "E": ["7", "-", "J", "S"], "N": ["|", "F", "7", "S"], "S": ["|", "L", "J", "S"], "W": ["-", "F", "L", "S"]
}

next_dir = {
    "N|": {"direction": "N", "p": Point(0, -1)},
    "NF": {"direction": "E", "p": Point(1, 0)},
    "N7": {"direction": "W", "p": Point(-1, 0)},
    "S|": {"direction": "S", "p": Point(0, 1)},
    "SL": {"direction": "E", "p": Point(1, 0)},
    "SJ": {"direction": "W", "p": Point(-1, 0)},
    "E-": {"direction": "E", "p": Point(1, 0)},
    "E7": {"direction": "S", "p": Point(0, 1)},
    "EJ": {"direction": "N", "p": Point(0, -1)},
    "W-": {"direction": "W", "p": Point(-1, 0)},
    "WF": {"direction": "S", "p": Point(0, 1)},
    "WL": {"direction": "N", "p": Point(0, -1)}
}


symbols = ["|",  "F", "L", "J", "7", "S", "-"]


def p(map):
    main_loop = set()
    sp = starting_point(map, "S")
    move = good_border(map, sp)
    #print(f'step {move["direction"]} {move["p"]}')
    p = move["p"]
    main_loop = main_loop.union({p, sp})
    iterations = 1
    while (True):
        if (p == sp):
            break
        move = next_dir[move["direction"] + map[p.y][p.x]]
        p = p.add(move["p"])
        #print(f'step {move["direction"]} {p}')
        main_loop = main_loop.union({p})
        iterations += 1
    #print(iterations)

    #Parte 2
    # prima mettere a 0 i vuoti che partono dai bordi e svuoto i tile che non sono parte del main loop
    clean_map(map, main_loop)
    clean_map(map, main_loop)


     # poi marco a I i tile interni, che hanno un numero dispari di tagli
    for y in range(len(map)):
        for x in range(len(map[y])):
            if(map[y][x] == "."):
                mark_empty_tile(map, Point(x, y))
    irradiate_found(map)
    return {"p1": iterations//2, "p2": count_symbols(map, "I")}

def mark_empty_tile(map, p):
    #East
    sublist= map[p.y][p.x:len(map[p.y])]
    cuts = sublist.count("L") - sublist.count("J") + sublist.count("S") + sublist.count("F") - sublist.count("7")  + sublist.count("|")
    if(cuts % 2 != 0):
        change_map_value(map, p, "I")
        return
    #West
    sublist= map[p.y][0:p.x]
    cuts = - sublist.count("L") + sublist.count("J") + sublist.count("S") - sublist.count("F") + sublist.count("7")  + sublist.count("|")
    if(cuts % 2 != 0):
        change_map_value(map, p, "I")  
        return
    #North
    sublist = [row[p.x] for row in map[0:p.y]]
    cuts = + sublist.count("L") - sublist.count("F") + sublist.count("S") + sublist.count("J") - sublist.count("7")  + sublist.count("-") 
    if(cuts % 2 != 0):
        change_map_value(map, p, "I")  
        return  
    #South
    sublist = [row[p.x] for row in map[p.y:len(map)]]
    cuts = - sublist.count("L") + sublist.count("F") + sublist.count("S") - sublist.count("J") + sublist.count("7") + sublist.count("-")
    if(cuts % 2 != 0):
        change_map_value(map, p, "I")  
        return

def irradiate_found(map):
    need_loop = True
    while( need_loop):
        need_loop = False
        for y in range(len(map)):
            for x in range(len(map[y])):
                if map[y][x] == "I":
                    borders = get_border(map, Point(x, y))
                    for b in borders:
                        if(map[b.y][b.x] == "."):
                            need_loop = True
                            change_map_value(map, b, "I")

def count_symbols(map, symbol):
    count = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == symbol:
                count += 1
    return count

def clean_map(map, main_loop):
    for y in range(len(map)):
        for x in range(len(map[y]) ):
            if (Point(x, y) not in main_loop and map[y][x] != "0"):
                change_map_value(map, Point(x, y), ".")
    #mark borders empty and inside with 0
    for y in range(len(map) ):
        if(map[y][0] in [".", "0"]):
            change_map_value(map, Point(0, y), "0")
            x = 1
            while(x<len(map)):
                if(map[y][x] in [".", "0"] and map[y][x-1] == "0"):
                    change_map_value(map, Point(x, y), "0")
                x += 1
        if(map[y][len(map[y])-1] in [".", "0"]):
            change_map_value(map, Point(len(map[y]) - 1, y), "0")
            x = len(map[y]) - 2
            while(x>=0 ):
                if(map[y][x] in [".", "0"] and map[y][x+1] == "0"):
                    change_map_value(map, Point(x, y), "0")
                x -= 1
    for x in range(len(map[0])):
        if(map[0][x] in [".", "0"]):
            change_map_value(map, Point(x, 0), "0")
            y = 1
            while(y<len(map) -1):
                if(map[y][x] in [".", "0"] and map[y-1][x] == "0"):
                    change_map_value(map, Point(x, y), "0")
                y += 1
        if(map[len(map) - 1][x] in [".", "0"]):
            change_map_value(map, Point(x, len(map) - 1), "0")
            y = len(map) - 2
            while(y>=0 ):
                if(map[y][x] in [".", "0"] and map[y+1][x] == "0"):
                    change_map_value(map, Point(x, y), "0")
                y -= 1

def change_map_value(map, p, value):
    s_list = list( map[p.y])
    s_list[p.x] = value
    map[p.y] = ''.join(s_list)

def good_border(map, p):
    if p.y > 0 and map[p.y-1][p.x] != ".":
        # towards N
        if map[p.y-1][p.x] in compatible_symbols["N"]:
            return {"direction": "N", "p": Point(p.x, p.y-1)}
    if p.y < len(map) - 1 and map[p.y+1][p.x] != ".":
        # towards S
        if map[p.y+1][p.x] in compatible_symbols["S"]:
            return {"direction": "S", "p": Point(p.x, p.y+1)}
    if p.x > 0 and map[p.y][p.x-1] != ".":
        # towards W
        if map[p.y][p.x-1] in compatible_symbols["W"]:
            return {"direction": "W", "p": Point(p.x-1, p.y)}
    if p.x < len(map[p.y]) - 1 and map[p.y][p.x+1] != ".":
        # towards E
        if map[p.y][p.x+1] in compatible_symbols["E"]:
            return {"direction": "E", "p": Point(p.x+1, p.y)}

def get_border(map, p):
    borders = set()
    if(p.y > 0):
        borders.add(Point(p.x, p.y-1))
    if(p.y < len(map) - 1):
        borders.add(Point(p.x, p.y+1))
    if(p.x > 0):
        borders.add(Point(p.x-1, p.y))
    if(p.x < len(map[p.y]) - 1):
        borders.add(Point(p.x+1, p.y))
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


f = open("resources\day10.txt", "r")
map = readallmap(f)
res = p(map)
print("Output: " + f"Part 1: {res['p1']}, Part 2: {res['p2' ]}")
f.close()
