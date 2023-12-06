# Advent of Code 2023 Day 5
import re

def day5(file):
    rowNumber = 0
    sectionNumber = 0
    newSection = False
    sections = {}
    for line in file:
        rowNumber +=1
        if(rowNumber == 1):
            seeds_list = list_numbers(line.split(":")[1])
            continue
        if(line=="\n"):
            newSection = True
            continue
        if(newSection):
            sections[sectionNumber] = { "label": line, "ranges" : {} }
            sectionNumber += 1
            newSection = False
            continue
        values = list_numbers(line)
        sections[sectionNumber - 1]["ranges"][values[1]] = { "dest": values[0], "len": values[2] }
    #print (sections)
    locations_p1 = []
    for seed in seeds_list:
        locations_p1.append(get_location(sections, seed))
    #print(seeds_list)
    #print(locations)   

    #Part 2
    #separate even and odd seed list
    base_seeds = seeds_list[::2]
    range_seeds = seeds_list[1::2]
    locations_p2 = []

    #StraightAlgorithm: for each seed, calculate the location. 
    # #Then, for each seed, calculate the location + 1, location + 2, etc. until the range is reached
    # Unfeasible because of performance issues (ranges too big )
    # for idx, x in enumerate(base_seeds):
    #     for i in range(range_seeds[idx]):
    #        locations_p2.append(get_location(sections, x + i))

    #Optimized algorithm: calculate the location for initial seed and all limits between initial seed and range
    for idx, initial_seed in enumerate(base_seeds):
        
        values_to_calculate = [Interval(initial_seed, initial_seed + range_seeds[idx]-1)]
        for section in sections:
            #print(f"Range input for section {sections[section]['label']}")
            #for a in values_to_calculate:
            #    print(a)
            next_values = []
            while(len(values_to_calculate) > 0):
                interval = values_to_calculate.pop(0)
                breaks = [seed for seed in get_section_limits(sections[section]) if seed > interval.start and seed < interval.end]
                list_intervals = create_intervals(sorted(breaks + [interval.start , interval.end]))
                next_values += [get_next_interval( value, sections[section]) for value in list_intervals]

            #print(f"end of section {sections[section]['label']}")
            values_to_calculate = next_values

        #print("End of all sections")
        #for a in values_to_calculate:
        #    print(a)
        locations_p2.append(min([value.start for value in values_to_calculate if value.start>0]))
    #print(locations_p2)  

    return {"part1": min(locations_p1), "part2": min(locations_p2)}

#Gets the location for a seed, flowing through all sections in almanac
def get_location(sections,  seed):
    res = seed
        #print(f"Seed: {seed}")
    for section in sections:            
        res = get_next(res, sections[section]["ranges"])
            #print(f"next: {res} for section {sections[section]['label']}")
    return res

def create_intervals(the_list):
    calc =  [Interval(the_list[i], the_list[i+1] - 1) for i in range(len(the_list)-1)]
    calc[len(calc)-1].end += 1
    return calc

def get_next_interval(interval, section):
    a  = get_next(interval.start, section["ranges"])
    b = get_next(interval.end, section["ranges"])
    return Interval(a if a<=b else b, b if a<=b else a)

def get_section_limits(section):
    limits = set(section["ranges"].keys())#.union(set([upper_limit + section["ranges"][upper_limit]["len"] -1 for upper_limit in section["ranges"].keys()]))
    return sorted(list(limits)) 

#Gets all numbers in a string
def list_numbers(stripe):
    return [int(x) for x in re.findall('\d+', stripe)]  #list comprehension to convert to int all elements in the list

#gets corresponding value for next section
def get_next(value, ranges):    
    for src in sorted(ranges.keys()):
        if(value >= src and value < src + ranges[src]["len"]):
            return value - src + ranges[src]["dest"]
    return value
        
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __str__(self):
        return f"[{self.start},{self.end}]"
    def shift(self, value):
        self.start += value
        self.end += value

f = open("resources\day5.txt", "r")
res = day5(f)
f.close()

print("Day 5 Output: " + f"Part 1: {res['part1']}, Part 2: {res['part2']}")
