# Advent of Code 2023 Day 15

def p1(map):
    count = [hash_char(row) for row in map]
    #print(count)
    return sum(count)


def p2(map):
    boxes = {}
    for item in map:
        # print(item)
        item = ''.join(item)
        if (item.count("=") > 0):
            label = item.split("=")[0]
            box_no = hash_char(label)
            if (box_no not in boxes):
                boxes[box_no] = {}
            boxes[box_no][label] = item.split("=")[1]
        elif (item.count("-") > 0):
            label = item.split("-")[0]
            box_no = hash_char(label)
            if (box_no not in boxes) or (label not in boxes[box_no]):
                continue
            boxes[box_no].pop(label)
    #print(boxes)
    count = []
    for box in boxes.keys():
        i = 1
        for label in boxes[box].keys():
            count += [int(boxes[box][label])*i*(box+1)]
            i += 1
    return sum(count)


def hash_char(row):
    curr = 0
    for c in row:
        curr = round(((curr + ord(c))*17) % 256)
    return curr


def readallmap(f):
    content = f.read()
    return [list(row) for row in content.split(',')]


f = open("resources\day15.txt", "r")
map = readallmap(f)
res1 = p1(map)
res2 = p2(map)

print("Output: " + f"Part 1: {res1}, Part 2: {res2}")
f.close()
