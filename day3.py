# Advent of Code 2023 Day 3

def day3(f):
    map = readallmap(f)
    border_finder = BorderFinder(len(map[0]), len(map)) #width, height. Assume rectangular map
    numbersInMap = []
    for y in range(len(map)):
        is_number_building = False 
        for x in range(len(map[y])):
            if(map[y][x].isdigit()):
                if(not(is_number_building)):
                    is_number_building = True
                    current_number = NumberInMap()
                current_number.digits.append(map[y][x])
                current_number.positions.append(Point(x,y))
                #print (map[i][j])
            else:
                if(is_number_building):
                    is_number_building = False
                    #print ("end number")
                    numbersInMap.append(current_number)
        if(is_number_building):
            is_number_building = False
            #print ("end number")
            numbersInMap.append(current_number)
    #print (numbersInMap)
    numbersOK= []   
    values = []
    valuesKO = []
    gears = []
    #print (numbersInMap[0].all_borders(border_finder))
    for n in numbersInMap:
        valid = False
        for p in n.all_borders(border_finder):
            if(is_gear(map, p)):
                #gear is a particular symbol, I calculate to find the companions
                valid = True
                numbersOK.append(n)
                values.append(n.value())
                gearCompanion = findGearCompanion(n, p, numbersInMap, border_finder)
                if(gearCompanion != None):
                    gears.append(n.value() * gearCompanion.value())
                    #print (f"Gear {n.value()} has companion {gearCompanion.value()}")
                break
            if(has_symbol(map, p)):
                valid = True
                numbersOK.append(n)
                values.append(n.value())
                break
        if(not(valid)):
            valuesKO.append(n.value())
    #print(valuesKO)
    #I assume that gears are only between two numbers. I found <n1,n2> and <n2,n1> so I divide by 2
    return {"part1": sum(values), "part2": int(sum(gears)/2)}

def has_symbol(map, p):
    return map[p.y][p.x] != "." and not(map[p.y][p.x].isdigit())

def is_gear(map, p):
    return map[p.y][p.x] == "*"

def findGearCompanion(n, gearPosition, numbersInMap, border_finder):
    for n2 in numbersInMap:
        if(n2 != n):
            for border_point in n2.all_borders(border_finder):
                if(border_point == gearPosition):
                    return n2                
    return None

def readallmap(f):
    map = []
    for line in f:
        map.append(line.strip())
    return map

#Utility class to find the borders of a point in the map
class BorderFinder:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def borders(self, p):
        result = set()
        if(p.y>0):
            if(p.x>0):
                result.add(Point(p.x-1, p.y-1)) #NW
            result.add(Point(p.x, p.y-1)) #N
            if(p.x<self.width-1):
                result.add(Point(p.x+1, p.y-1)) #NE
        if(p.x>0):
            result.add(Point(p.x-1, p.y)) #W
        if(p.x<self.width-1):
            result.add(Point(p.x+1, p.y)) #E
        if(p.y<self.height-1):
            if(p.x>0):
                result.add(Point(p.x-1, p.y+1)) #SW
            result.add(Point(p.x, p.y+1)) #S
            if(p.x<self.width-1):
                result.add(Point(p.x+1, p.y+1)) #SE
        return result

#Class representing a point in the map
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

#Class representing a number in the map, with all digits and relative positions
class NumberInMap:
    def __init__(self):
          self.digits = []
          self.positions = []  
    def value(self):
        return int("".join(self.digits))
    def __str__(self):
        return f"{self.digits} , {self.positions}"
    def __eq__(self, other):
        return other!= None and self.positions == other.positions
    def all_borders(self, border_finder):
        result = set()
        for p in self.positions:
            result = result.union(border_finder.borders(p))
        return result


f = open("resources\day3.txt", "r")
res = day3(f)
print("Day 3 Output: " + f"Part 1: {res['part1']}, Part 2: {res['part2']}")
f.close()