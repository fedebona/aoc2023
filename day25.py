# Advent of Code 2023 Day 25
from itertools import combinations

def p1(graph):
	map = graph["adjacentlist"]
	node1 = list(map.keys())[0]
	arks = graph["arks"]
	#print(len(map))
	for tuple in combinations(arks, 3):
		# for n in map:
		# 	for e in map[n]:
		m1 = copymap(map)
		for n, e in tuple:
			m1[n].remove(e)
			m1[e].remove(n)
		v = visit_graph(m1, node1)
		if len(v) != len(map):
			#print(tuple, len(v) )			
			return len(v) * (len(map) - len(v))
	#v = visit_graph(map, "nvd")
	#print (v)
	#print(len(v))
	return 0

def p2(map):	
	return 0

def copymap(map):
	m = {}
	for k in map:
		m[k] = map[k].copy()
	return m

def readallmap(f):
	map = {}
	arks = []
	for line in f:
		origin = line.strip().split(": ")[0]
		dest = line.strip().split(": ")[1].split(" ")
		if origin in map:
			map[origin] = map[origin].union(set(dest))
		else:
			map[origin] = set(dest)
		for d in dest:
			if d in map:
				map[d] = map[d].union(set([origin]))
			else:
				map[d] = set([origin])
			arks.append((origin, d))
	return {"adjacentlist":map, "arks":arks}

def visit_graph(map, start):
	visited = set()
	queue = [start]
	while queue:
		node = queue.pop(0)
		if node not in visited:
			visited.add(node)
			queue.extend(map[node] - visited)
	return visited

f = open("resources\day25.txt", "r")
map = readallmap(f)
f.close()
res1 = p1(map)
res2 = p2(map)
print("Output: " + f"Part 1: {res1}, Part 2: {res2}")
