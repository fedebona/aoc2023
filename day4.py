# Advent of Code 2023 Day 4
import re

def day4(file, total_cards):
    wins = []
    card_copies = {}
    currentCard = 1
    for line in file:
        all_numbers = line.split(":")[1].split(" | ")
        winning_numbers = card_set(all_numbers[0])
        my_numbers = card_set(all_numbers[1])
        #print(my_numbers)
        matches = len(my_numbers.intersection(winning_numbers))
        if(matches > 0):
            #print(f"Found {matches} matches")
            val = 2**(matches-1)
            wins.append(val)    #part 1
            add_copy(card_copies, matches, currentCard, total_cards) #part 2
        currentCard = currentCard + 1
    #print(wins)     
    #print(card_copies)  
    part2 = sum(card_copies.values()) + total_cards
    return {"part1": sum(wins), "part2": part2}

def card_set(stripe):
    return set(re.findall('\d+', stripe))

def add_copy(card_copies, matching_numbers, currentCard, total_cards):
    if(card_copies.keys().__contains__(currentCard)):
        copies_to_add = card_copies[currentCard] + 1
    else:
        copies_to_add = 1
    for i in range(matching_numbers):
        target_card = currentCard + i + 1
        if(target_card > total_cards):
            break
        if(not(card_copies.keys().__contains__(target_card))):
            card_copies[target_card] = copies_to_add
        else:
            card_copies[target_card] += copies_to_add

def number_of_cards(file):
    lines = 0
    for line in file:
        lines +=1
    return lines

f = open("resources\day4.txt", "r")
total_cards = number_of_cards(f)
f.close()

f = open("resources\day4.txt", "r")
res = day4(f, total_cards)
f.close()

print("Day 4 Output: " + f"Part 1: {res['part1']}, Part 2: {res['part2']}")
