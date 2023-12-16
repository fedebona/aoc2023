# Advent of Code 2023 Day 13

def p1(maps):

    current = []
    for i in range(len(maps)):
        #print(maps[i])
        if (i % 2 == 0):
            current.append(find_simmetry(transpose_matrix(maps[i]), True))
        else:
            current.append(find_simmetry(maps[i]) * 100)

    print(current)

    return sum(current)


def find_simmetry(map, reverse=False):
    p = 1
    found = []
    sim_len = []
    while(True):
    # Replace # with sequence number
        for y in range(p, (len(map))):
            if (map[y] == map[y-1]):
                p = y
                break
        count = 0
        if p == len(map):
            break        
        while (map[p+count] == map[p-1-count]):
            count += 1
            if (p+count == len(map) or p-1-count == -1):
                break
        if (count != 0):
            found += [p]
            sim_len += [count]
            break
        p += 1
    if(len(found) > 1):
        print(f"Found more than one simmetry {found} {sim_len}")
    return 0 if len(found) ==0 else (max(found))


def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def reverse_transpose_matrix(matrix):
    return [list(row)[::-1] for row in zip(*matrix)]

def readallmap(f):
    content = f.read()
    maps = content.split('\n\n')
    return [list(map.split('\n')) for map in maps]


f = open("resources\day13.txt", "r")
map = readallmap(f)
res1 = p1(map)

print("Output: " + f"Part 1: {res1}, Part 2: {0}")
f.close()
