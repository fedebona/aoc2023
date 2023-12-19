# Advent of Code 2023 Day 18

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

	def label(self):
		return f"{self.x},{self.y}"


def p1(map):
	dest_map = init_map()
	# dest_map = extend_map(dest_map)
	current_position = Point(500, 500)
	top_right = Point(500, 500)
	bottom_left = Point(500, 500)
	for line in map:
		direction = line.split(" ")[0]
		amount = int(line.split(" ")[1])
		for i in range(amount):
			dest_map[current_position.y][current_position.x] = "#"
			if current_position.x > top_right.x:
				top_right.x = current_position.x
			if current_position.y > top_right.y:
				top_right.y = current_position.y
			if current_position.x < bottom_left.x:
				bottom_left.x = current_position.x
			if current_position.y < bottom_left.y:
				bottom_left.y = current_position.y
			if direction == "R":
				current_position.x += 1
			elif direction == "L":
				current_position.x -= 1
			elif direction == "U":
				current_position.y -= 1
			elif direction == "D":
				current_position.y += 1

	with open('resources\output_18.txt', 'w') as f:
		f.write(f"Top right: {top_right}, Bottom left: {bottom_left}\n")

	with open('resources\output_18_filled.txt', 'w') as f:
		f.write(f"Top right: {top_right}, Bottom left: {bottom_left}\n")

	dest_map_dump = [item.copy() for item in dest_map]

	print(f"Top right: {top_right}, Bottom left: {bottom_left}")
	# fill map
	count = 0
	for y in range(bottom_left.y-1, top_right.y+1):
		with open('resources\output_18.txt', 'a') as f:
			f.write(''.join(dest_map[y][bottom_left.x-1:top_right.x+1]) + "\n")
		cuts = 0
		sequence = False
		start_bend = [False, False]
		prev_bend = [False, False]
		for x in range(bottom_left.x-1, top_right.x+1):
			if dest_map[y][x] == "." and (count_cuts(dest_map, Point(x, y), top_right.x+1) == 0 or count_cuts_reverse(dest_map, Point(x, y), bottom_left.x-1) == 0):
				continue
			if dest_map[y][x] == "." and (count_cuts(dest_map, Point(x, y), top_right.x+1) % 2 != 0
                                 or count_cuts_reverse(dest_map, Point(x, y), bottom_left.x-1) % 2 != 0):
				dest_map_dump[y][x] = "#"
				count += 1
			elif dest_map[y][x] == "#":
				dest_map_dump[y][x] = "#"
				count += 1
			# prev_bend[0] = (dest_map[y-1][x-1] == "#")
			# prev_bend[1] = (dest_map[y+1][x-1] == "#")
			# if(dest_map[y][x+1:top_right.x+1].count("#")==0):
			# 	break
			# if dest_map[y][x] == "#":
			# 	if not sequence:
			# 		sequence = True
			# 		cuts += 1
			# 		start_bend[0] = (dest_map[y-1][x] == "#")
			# 		start_bend[1] = (dest_map[y+1][x] == "#")
			# 	count += 1
			# elif dest_map[y][x] == "." and sequence and start_bend == prev_bend and start_bend[0] != start_bend[1]:
			# 	cuts -= 1
			# 	sequence = False
			# elif dest_map[y][x] == "." and cuts % 2 != 0:
			# 	dest_map[y][x] = "#"
			# 	count += 1
			# 	sequence = False
			# else:
			# 	sequence = False
		with open('resources\output_18_filled.txt', 'a') as f:
			f.write(''.join(dest_map_dump[y][bottom_left.x-1:top_right.x+1]) + "\n")

	return count


def p2(map):
	return 0


def count_cuts(dest_map, point, x_limit):
	count = 0
	countbend = 0
	shape = {}
	shape["TT"] = 0
	shape["TF"] = 0
	shape["FT"] = 0
	shape["FF"] = 0
	for x in range(point.x+1, x_limit+1):
		if dest_map[point.y][x] == "#":
			k1 = "T" if (dest_map[point.y-1][x] == "#") else "F"
			k2 = "T" if (dest_map[point.y+1][x] == "#") else "F"
			shape[k1+k2] += 1
	return shape["TT"] + min(shape["TF"] , shape["FT"]) % 2


def count_cuts_reverse(dest_map, point, x_limit):
	count = 0

	countbend = 0
	shape = {}
	shape["TT"] = 0
	shape["TF"] = 0
	shape["FT"] = 0
	shape["FF"] = 0
	for x in range(x_limit, point.x):
		if dest_map[point.y][x] == "#":
			k1 = "T" if (dest_map[point.y-1][x] == "#") else "F"
			k2 = "T" if (dest_map[point.y+1][x] == "#") else "F"
			shape[k1+k2] += 1
	return shape["TT"] + min(shape["TF"] , shape["FT"]) % 2


def readallmap(f):
    map = []
    for line in f:
        map.append(line.strip())
    return map


def init_map():
	return [list('.' * 1000) for _ in range(1000)]


def extend_map(map):
	for item in map:
		item.extend(list('.' * 100))
	map += [list('.' * (len(map)+100)) for _ in range(100)]
	return map


f = open("resources\day18.txt", "r")

map = readallmap(f)

f.close()
res1 = p1(map)
res2 = p2(map)
print("Day 3 Output: " + f"Part 1: {res1}, Part 2: {res2}")
