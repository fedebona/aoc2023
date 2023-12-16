# Advent of Code 2023 Day 8
import pandas as pd
import math


def lcm_list(lst):
    lcm = lst[0]
    for i in lst[1:]:
        lcm = abs(lcm*i) // math.gcd(lcm, i)
    return lcm


def P1(df, recipe, currentPosition, iterations, finalPositionFull=True):
    # print (f"it {currentPosition} - {recipe} - {iterations}")
    while True:        
        for c in recipe:
            iterations += 1
            next = df.query(f'current == "{currentPosition}"')[c].values.tolist()[0]
            if (finalPositionFull and next == 'ZZZ') or (not finalPositionFull and next[2] == 'Z'):
                return {'iterations': iterations, 'finalPosition': next}
            else:
                currentPosition = next
            # print (f"after turn {c} - {currentPosition}")


def P2(df, recipe, position_list):
    lista = [P1(df, recipe, p, 0, False)['iterations'] for p in position_list]
    mcm = lcm_list(lista)
    return {'iterations': mcm}


f = open("resources\day8.txt", "r")
# load data into a DataFrame object:
# define a fake separator to avoid the split by comma
df = pd.read_csv(f, names=['data'], skiprows=2, sep=";")
# print (df)
df[['current', 'L', 'R']] = df['data'].str.extract(
    r'([A-Z]{3})\s=\s\(([A-Z]{3})\,\s([A-Z]{3})\)', expand=True)

f.seek(0)
recipe = f.readline().strip()
# print (recipe)
# print (df)

p1 = P1(df, recipe, 'AAA', 0)['iterations']
print("P1 done")

starting_list = df.query('current.str.endswith("A")')[
    'current'].values.tolist()

p2 = P2(df, recipe, starting_list)['iterations']

print(f"Day 7 P1: {p1} P2: {p2}")
f.close()
