# Advent of Code 2023 Day 19
import re
from functools import reduce
import operator


def P1(wf_list, ranks):
    listRank = [extract_rank(m) for m in re.findall('{(\S+)\}', ranks)]

    for m in matches:
        rules = m[1].split(',')
        wf_list[m[0]] = rules

    satisfied_ranks = []

    for rank in listRank:
        res = evaluate_wf(rank, wf_list, "in")
        if res:
            satisfied_ranks.append(sum(rank.values()))

    # print(satisfied_ranks)
    return sum(satisfied_ranks)


def P2(wf_list):
    for m in matches:
        rules = m[1].split(',')
        wf_list[m[0]] = rules

    res = visit_all_wf(wf_list, "crn")
    return res


def evaluate_wf(rank, wf_list, wf_name):
    rules = wf_list[wf_name]
    for rule in rules:
        r = extract_rule(rule)
        condition_satisfied = False
        if r["condition"][1] == "<" and rank[r["condition"][0]] < r["condition"][2]:
            condition_satisfied = True
            # satisfied_ranks.append(r["condition"][2])
        elif r["condition"][1] == ">" and rank[r["condition"][0]] > r["condition"][2]:
            condition_satisfied = True
        elif r["condition"][1] == "True":
            condition_satisfied = True

        if condition_satisfied:
            if r["destination"] == "R":
                return False
            elif r["destination"] == "A":
                return True
            else:
                return evaluate_wf(rank, wf_list, r["destination"])

#TODO: keep a dictionary of each variables for conditions, and restrict the range of allowed values navigating the tree
def visit_all_wf(wf_list, wf_name):
    print(f'current wf: {wf_name}')
    rules = wf_list[wf_name]
    result = 0
    previous_rules = []
    while len(rules) > 0:
        rule = rules.pop(0)
        r = extract_rule(rule)
        print(f'rule {r["condition"]} -> {r["destination"]}')
        if r["destination"] == "A":
            #it is an "ELSE" rule
            if (r["condition"][1] == "True"):
                result += reduce(
                    operator.mul, [calculate_rank_range(pr, False) for pr in previous_rules], 1) * 4000^(4-len(previous_rules))
            else:
                result += calculate_rank_range(r, True) 
            print(f'dest OK: {wf_name} range {result}')
        elif r["destination"] == "R":
            result += 0
            print(f'dest KO: {wf_name} range {result}')
        else:
            if len(previous_rules) > 0:
                if not r["condition"][1] == "True":
                    print(
                        f'range P {calculate_rank_range(r, True)} * {[calculate_rank_range(pr, False) for pr in previous_rules] } * { r["destination"]}')
                    result += calculate_rank_range(r, True) * reduce(operator.mul, [calculate_rank_range(
                        r, False) in previous_rules], 1) * visit_all_wf(wf_list, r["destination"])
                else:
                    print(
                        f'range N {[calculate_rank_range(pr, False) for pr in previous_rules] } * 4000^({4-len(previous_rules)}) * { r["destination"]}')
                    result += reduce(operator.mul, [calculate_rank_range(
                        pr, False) for pr in previous_rules], 1) * 4000^(4-len(previous_rules)) * visit_all_wf(wf_list, r["destination"])
            else:
                print(
                    f'range P {calculate_rank_range(r, True)} * { r["destination"]}')
                result += calculate_rank_range(r, True) * \
                    visit_all_wf(wf_list, r["destination"])
        previous_rules.append(r)
    print(f'result for: {wf_name} = {result}')
    return result


def extract_rank(rank):
    res = {}
    for item in rank.split(','):
        res[item.split("=")[0]] = int(item.split("=")[1])
    return res


def extract_rule(rule):
    if rule.count(":") == 0:
        return {"condition": ["", "True", 0], "destination": rule}
    m = re.findall('(\w+)([<|>|=])(\d+)', rule.split(":")[0])
    return {"condition": [m[0][0], m[0][1], int(m[0][2])], "destination": rule.split(":")[1]}


def calculate_rank_range(r, ok):
    if r["condition"][1] == "<":
        if ok:
            return r["condition"][2] - 1
        else:
            return 4000 - r["condition"][2]
    elif r["condition"][1] == ">":
        if ok:
            return 4000 - r["condition"][2] + 1
        else:
            return r["condition"][2]


f = open("resources\day19_test.txt", "r")
content = f.read()
maps = content.split('\n\n')
worflows = maps[0]
ranks = maps[1]
wf_list = {}
matches = re.findall('(\S+?)\{(\S+)\}', worflows)
for m in matches:
    rules = m[1].split(',')
    wf_list[m[0]] = rules

print(f"P1: {P1(wf_list, ranks)} P2: {P2(wf_list)}")
f.close()
