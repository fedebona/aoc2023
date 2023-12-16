# Advent of Code 2023 Day 14

def p1(map):

    map = transpose_matrix(map)
    for row in map:
        for i in range(len(row)):
            if(row[i]=='O'):
                if i== 0:
                    continue
                back = i
                moved = False
                rock = False
                while back > 0 :
                    back -= 1
                    if(row[back] == '.'):
                        moved=True
                        row[i] = '.'
                    else:
                        rock = True
                        break
                if moved:
                    row[back+1 if rock else 0] = 'O'
    map = transpose_matrix(map)
    #print(map)
    count = []
    for i in range(len(map)):
        count += [map[i].count('O')*(len(map[i]) - i )]
    #print(count)
    return sum(count)


def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def readallmap(f):
    content = f.read()
    return [list(row) for row in content.split('\n')]
    

f = open("resources\day14.txt", "r")
map = readallmap(f)
res1 = p1(map)

print("Output: " + f"Part 1: {res1}, Part 2: {0}")
f.close()
