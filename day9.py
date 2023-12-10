#Advent of Code 2023 Day 9

def P(f):
    all_next_values = []
    all_previuos_values = []
    for line in f:
        sequence = [int(x) for x in line.strip().split(" ")]
        all_next_values.append(sum(extrapolate_sequence(sequence)))
        all_previuos_values.append(sum(extrapolate_sequence(sequence[::-1])))    
    return {"p1": sum(all_next_values), "p2":sum(all_previuos_values)}

#produces the list of last element of each extapolation of the sequence. In the end the sum of values of this list is next value of initial sequence
def extrapolate_sequence(sequence):
    #print(sequence)
    if(len(sequence) == 1):
        return sequence
    #if all elements are the same
    if(len(set(sequence))==1):
        return [sequence[-1]]
    return extrapolate_sequence([(sequence[i] - sequence[i-1])  for i in range(1, len(sequence))])  + [sequence[-1]]

f = open("resources\day9.txt", "r")
print(f"Day 7 P1: {P(f)['p1']} P2: {P(f)['p2']}")
f.close()

