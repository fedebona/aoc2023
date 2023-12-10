#Advent of Code 2023 Day 8
import pandas as pd

def P1(df, recipe, currentPosition, iterations):
    #print (f"it {currentPosition} - {recipe} - {iterations}")    
    for c in recipe:
        iterations += 1
        df2=df[df["current"] == currentPosition] 
        if df2[c].item() == 'ZZZ':
            return { 'iterations': iterations, 'finalPosition': df2[c].item()}            
        else:
            currentPosition = df2[c].item()   
        #print (f"after turn {c} - {currentPosition}")              
    return P1(df, recipe, currentPosition, iterations)

def P2(df, recipe, position_list, iterations):
    while True:
        for c in recipe:
            iterations += 1
            found = 0
            for i in range(0, len(position_list)):
                next = df.query(f'current == "{position_list[i]}"')[c].values.tolist()[0]
                if next[2] == 'Z':
                    found += 1
                position_list[i] = next           
            if found==len(position_list):
                return { 'iterations': iterations}            

f = open("resources\day8.txt", "r")
 #load data into a DataFrame object:
df = pd.read_csv(f, names=['data'], skiprows=2, sep=";")   #define a fake separator to avoid the split by comma
#print (df)
df[['current', 'L', 'R']] = df['data'].str.extract(r'([A-Z]{3})\s=\s\(([A-Z]{3})\,\s([A-Z]{3})\)', expand=True)

f.seek(0)
recipe = f.readline().strip()
#print (recipe)
#print (df)

#p1 = P1(df, recipe, 'AAA', 0)['iterations']

starting_list = df.query('current.str.endswith("A")')['current'].values.tolist()

p2 = P2(df, recipe, starting_list, 0)['iterations']

print(f"Day 7 P1: {p1} P2: {p2}")
f.close()