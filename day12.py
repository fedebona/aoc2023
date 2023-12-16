# Advent of Code 2023 Day 12
import itertools


def p(file):
    matches_p1 = []
    matches_p2 = []
    for line in file:
        checklist  = [int(i) for i in line.split(" ")[1].split(",")]
        row = list(line.split(" ")[0])
        extended_row = []
        extended_checklist = []
        for i in range(5):
            extended_row += row + (['?'] if i<4 else []) 
            extended_checklist += checklist
        matches_p1.append(calculate_row(row, checklist))

        matches_p2.append(calculate_row(extended_row, extended_checklist))
    #print(matches_p1)

    return {"part1": sum(matches_p1), "part2": sum(matches_p2)}

def calculate_row(original_row, checklist):
    matches = 0  
    # matches_extended = 0  
    for comb in itertools.product(['#', '.'], repeat=original_row.count('?')):
        row = original_row.copy()
        #print (f"new comb: {comb} - {row} ")
        i = 0
        subs = row.count('?')
        for j in range(len(row)):
            if row[j] == '?':
                row[j] = comb[i]
                i += 1
        #print (f"row after ? substitutions: {comb} - {row} ")
        resulting_checklist = [len(item) for item in ''.join(row).strip('.').split('.') if len(item) > 0]
        #print(f" calculated checklist: {resulting_checklist} to verify against {checklist}")
        #print("----")
        if(resulting_checklist) == checklist:
            matches += 1
            # if(comb[0] == '.') or (comb[-1] == 0) or (comb.count("#") == 0) :
            #     matches_extended += 1
    #print(matches)
    #return {"matches": matches, "matches_extended": matches_extended}
    return matches


f = open("resources\day12.txt", "r")
res = p(f)
f.close()

print("Output: " + f"Part 1: {res['part1']}, Part 2: {res['part2']}")
