# Advent of Code 2023 Day 17

import heapq


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
	def label(self):
		return f"{self.x},{self.y}"

def p1(map):
	return 0

def p2(map):
	return dijkstra(map)

symbols = ['>', '<', '^', 'v']

def readallmap(f):
    map = []
    for line in f:
        map.append(line.strip())
    return map

def dijkstra(map):
	distances = {}
	visited_points = set()
	
	queue = [(0, Point(0,0))]
	while queue:
		current_distance, current_point = heapq.heappop(queue)
		if Point(0,0).label in visited_points:
			continue
		visited_points.add(current_point.label)
		if not current_point.label in distances:
			distances[current_point.label] = 1000000
		if current_distance > distances[current_point.label]:
			continue
		neighbors = next_node(map, current_point)
		for neighbor in neighbors:
			distance = current_distance + map[neighbor.y][neighbor.x]
			if distance < distances[neighbor]:
				distances[neighbor.label] = distance
				heapq.heappush(queue, (distance, neighbor))
	return distances[Point(len(map) - 1, len(map[len(map) - 1]) - 1).label]



def next_node(map, p):
	next_node = []
	# Check if we can go up
	if(p.y == len(map) - 1) and p.x == len(map[p.y]) - 1:
		return next_node
	if(map[p.y][p.x] == '>'):
		# Check if we can go left
		if(p.y - 1 >= 0):
			next_node.append(Point(p.x, p.y - 1))
		# Check if we can go right
		if(p.y + 1 < len(map)):
			next_node.append(Point(p.x, p.y + 1))
		# Check if we can go straight
		if(p.x + 1 < len(map[p.y])):
			if(not streak_of_symbols(map, p, '>', "E")):
				next_node.append(Point(p.x + 1, p.y))
	elif(map[p.y][p.x] == '<'):
		# Check if we can go right
		if(p.y - 1 >= 0):
			next_node.append(Point(p.x, p.y - 1))
		# Check if we can go left
		if(p.y + 1 < len(map)):
			next_node.append(Point(p.x, p.y + 1))
		# Check if we can go straight
		if(p.x - 1 >= 0):
			if(not streak_of_symbols(map, p, '<', "W")):
				next_node.append(Point(p.x - 1, p.y))
	elif(map[p.y][p.x] == '^'):
		# Check if we can go left
		if(p.x - 1 >= 0):
			next_node.append(Point(p.x - 1, p.y))
		# Check if we can go right
		if(p.x + 1 < len(map[p.y])):
			next_node.append(Point(p.x + 1, p.y))
		# Check if we can go straight
		if(p.y - 1 >= 0):
			if(not streak_of_symbols(map, p, '^', "N")):
				next_node.append(Point(p.x, p.y - 1))
	elif(map[p.y][p.x] == 'v'):
		# Check if we can go left
		if(p.x - 1 >= 0):
			next_node.append(Point(p.x - 1, p.y))
		# Check if we can go right
		if(p.x + 1 < len(map[p.y])):
			next_node.append(Point(p.x + 1, p.y))
		# Check if we can go straight
		if(p.y + 1 < len(map)):
			if(not streak_of_symbols(map, p, 'v', "S")):
				next_node.append(Point(p.x, p.y + 1))
	return next_node

def streak_of_symbols(map, curr_p, symbol, dir):
	p = curr_p.copy()
	if(map[p.y][p.x] != symbol):
		return False
	for i in range(1,3):
		if(dir == 'W'):
			curr_p.x -= i
		elif(dir == 'E'):
			curr_p.x += i
		elif(dir == 'N'):
			curr_p.y -= i
		elif(dir == 'S'):
			curr_p.y += i
		if(p.x < 0) or (p.y < 0) or (p.x >= len(map[0])) or (p.y >= len(map)):
			return False
		if(map[p.y][p.x] != symbol):
			return False
	return True



f = open("resources\day17_test.txt", "r")
map = readallmap(f)
f.close()
res1 = p1(map)
res2 = p2(map)
print("Day 3 Output: " + f"Part 1: {res1}, Part 2: {res2}")
