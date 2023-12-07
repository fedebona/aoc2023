#Advent of Code 2023 Day 6

from functools import reduce
import operator

def day6_1(f):
    time, duration = f.read().split("\n")
    time = time.split(":")[1]
    time = [int(x) for x in time.split()]
    duration = duration.split(":")[1]
    duration = [int(x) for x in duration.split()]
    wins = []
    for r, _ in enumerate(time):
        wins += [(len([d for d in calculate_distance(time[r]) if d > duration[r]]))]
    return reduce(operator.mul, wins, 1)

def day6_2(f):
    f.seek(0)
    time, duration = f.read().split("\n")
    time = time.split(":")[1]
    time = int(time.replace(" ", ""))
    duration = duration.split(":")[1]
    duration = int(duration.replace(" ", ""))   
    return len([d for d in calculate_distance(time) if d > duration])

def calculate_distance(t):
    return [(t-i)*i for i in range(0, t)]

f = open("resources\day6.txt", "r")
print(f"Day 6 P1: {day6_1(f)} P2: {day6_2(f)}")
f.close()