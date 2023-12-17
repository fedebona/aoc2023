# Advent of Code 2023 Day 16

def p1(map):
	return calculate_impact(map, Beam(0,0,"E"))

def p2(map):
	list_impacts = []
	for i in range(len(map)):
		list_impacts.append(calculate_impact(map, Beam(0,i,"E")))
		list_impacts.append(calculate_impact(map, Beam(len(map[0])-1,i,"W")))
	for j in range(len(map[0])):
		list_impacts.append(calculate_impact(map, Beam(j,0,"S")))
		list_impacts.append(calculate_impact(map, Beam(j,len(map)-1,"N")))
	print(list_impacts)
	return max(list_impacts)

def calculate_impact(map, initial_beam):
	beam_queue = set()
	beam_history = []
	beam_queue.add(initial_beam.__str__())
	weights = {}
	while len(beam_queue) > 0:
		beam = Beam.ToBeam(list(beam_queue)[0])
		move_beam(beam, map, beam_queue, weights, beam_history)
	return len(weights)

def move_beam(beam, map, beam_queue, weights, beam_history):
	orig_beam = beam.__str__()
	while True:		
		if(beam.p.x <0 or beam.p.y < 0 or beam.p.x >= len(map[0]) or beam.p.y >= len(map)):
			beam_queue.discard(orig_beam)
			return
		beam_history += [beam.__str__()]
		if(not beam.p.label() in weights):
			weights[beam.p.label()] = 1
		else:
			weights[beam.p.label()] += 1
		if beam.dir == "E":
			if map[beam.p.y][beam.p.x] == '\\':
				beam.dir = "S"
				beam.p.y += 1
			elif map[beam.p.y][beam.p.x] == '/':
				beam.dir = "N"
				beam.p.y -= 1
			elif map[beam.p.y][beam.p.x] == '|':
				if(beam.p.y - 1 >= 0):
					split_beam = Beam(beam.p.x, beam.p.y - 1, "N")
					if(not split_beam.__str__() in beam_history):
						beam_queue.add(split_beam.__str__())
				if(beam.p.y + 1 < len(map)):
					split_beam2 = Beam(beam.p.x, beam.p.y + 1, "S")
					if(not split_beam2.__str__() in beam_history):
						beam_queue.add(split_beam2.__str__())	
				beam_queue.discard(orig_beam)				
				return												
			elif beam.p.x == len(map[beam.p.y]) - 1:
				beam_queue.discard(orig_beam)
				return
			else:
				beam.p.x += 1
		elif beam.dir == "W":
			if map[beam.p.y][beam.p.x] == '\\':
				beam.dir = "N"
				beam.p.y -= 1
			elif map[beam.p.y][beam.p.x] == '/':
				beam.dir = "S"
				beam.p.y += 1
			elif map[beam.p.y][beam.p.x] == '|':
				if(beam.p.y - 1 >= 0):
					split_beam = Beam(beam.p.x, beam.p.y - 1, "N")
					if(not split_beam.__str__() in beam_history):
						beam_queue.add(split_beam.__str__())
				if(beam.p.y + 1 < len(map)):
					split_beam2 = Beam(beam.p.x, beam.p.y + 1, "S")
					if(not split_beam2.__str__() in beam_history):
						beam_queue.add(split_beam2.__str__())	
				beam_queue.discard(orig_beam)
				return
			elif beam.p.x == 0:
				beam_queue.discard(orig_beam)
				return
			else:
				beam.p.x -= 1

		elif beam.dir == "N":
			if map[beam.p.y][beam.p.x] == '\\':
				beam.dir = "W"
				beam.p.x -= 1
			elif map[beam.p.y][beam.p.x] == '/':
				beam.dir = "E"
				beam.p.x += 1
			elif map[beam.p.y][beam.p.x] == '-':
				if(beam.p.x + 1 < len(map[beam.p.y])):
					split_beam = Beam(beam.p.x + 1, beam.p.y, "E")
					if(not split_beam.__str__() in beam_history):
						beam_queue.add(split_beam.__str__())	
				if(beam.p.x - 1 >= 0):
					split_beam2 = Beam(beam.p.x - 1, beam.p.y, "W")
					if(not split_beam2.__str__() in beam_history):
						beam_queue.add(split_beam2.__str__())	
				beam_queue.discard(orig_beam)
				return
			elif beam.p.y == 0:
				beam_queue.discard(orig_beam)
				return
			else:
				beam.p.y -= 1
		elif beam.dir == "S":
			if map[beam.p.y][beam.p.x] == '\\':
				beam.dir = "E"
				beam.p.x += 1
			elif map[beam.p.y][beam.p.x] == '/':
				beam.dir = "W"
				beam.p.x -= 1
			elif map[beam.p.y][beam.p.x] == '-':
				if(beam.p.x + 1 < len(map[beam.p.y])):
					split_beam = Beam(beam.p.x + 1, beam.p.y, "E")
					if(not split_beam.__str__() in beam_history):
						beam_queue.add(split_beam.__str__())
				if(beam.p.x - 1 >= 0):
					split_beam2 = Beam(beam.p.x - 1, beam.p.y, "W")
					if(not split_beam2.__str__() in beam_history):
						beam_queue.add(split_beam2.__str__())	
				beam_queue.discard(orig_beam)
				return
			elif beam.p.y == len(map) - 1:
				beam_queue.discard(orig_beam)
				return
			else:
				beam.p.y += 1

def readallmap(f):
    map = []
    for line in f:
        map.append(line.strip())
    return map



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

class Beam:
	def __init__(self, x, y, dir):
		self.dir = dir
		self.p = Point(x, y)
	def __eq__(self, other):
		return (self.p, self.dir) == (other.p, other.dir)
	def __str__(self):
		return f"{self.p} , {self.dir}"
	def __hash__(self):	
		return hash(self.__str__())
	@staticmethod
	def ToBeam(string):
		parts = string.split(",")
		return Beam(int(parts[0]), int(parts[1]), parts[2].strip())


f = open("resources\day16.txt", "r")
map = readallmap(f)
f.close()
res1 = p1(map)
res2 = p2(map)
print("Day 3 Output: " + f"Part 1: {res1}, Part 2: {res2}")
