#Advent of Code 2023 Day 7

import pandas as pd

card_ranks = {
    "A": 'Z',
    "K": 'Y',
    "Q": 'X',   
    "J": 'W',
    "T" : 'V'
    }  

card_ranks_p2 = {
    "A": 'Z',
    "K": 'Y',
    "Q": 'X',   
    "T" : 'V',
    "J": '0'
    }  


def value_hand(hands):
    values = []
    for hand in hands:
        dic = {}  
        for c in hand:        
            dic[c] = 1 if not dic.__contains__(c) else dic[c] +  1
        value = max(dic.values())
        if list(dic.values()).count(2) == 2:
            value = 2.5
        if list(dic.values()).count(2) == 1 and list(dic.values()).count(3) == 1:
            value = 3.5
        values += [value]
    return values

def value_hand_p2(hands):
    values = []
    for hand in hands:
        dic = {}  
        jokers = 0   
        value = 0       
        for c in hand: 
            if c == 'J':
                jokers += 1 
                continue
            dic[c] = 1 if not dic.__contains__(c) else dic[c] +  1
        if(jokers < 5):
            value = max(dic.values())
            if list(dic.values()).count(2) == 2:
                value = 2.5
            if list(dic.values()).count(2) == 1 and list(dic.values()).count(3) == 1:
                value = 3.5
        value += jokers
        values += [value]
    return values

def rank_hand(hands, card_rank_dict):
    ranks = []
    for hand in hands:
        rank = ""
        for c in hand:        
            rank += card_rank_dict[c] if card_rank_dict.__contains__(c) else c
        ranks += [rank]
    return ranks

# Experimented using pandas to sort and aggregate the data
def P1(f):

    #load data into a DataFrame object:
    df = pd.read_csv(f, names = ['hand', 'bet'], sep = " ")
    #print(df)
    df['rank'] = rank_hand(df['hand'], card_ranks)
    df['value'] = value_hand(df['hand'])

    df = df.sort_values(by=['value', 'rank'], ascending=True)
    df['row_num'] = df.reset_index().index + 1
    #print(df)
    return sum(df['bet']*df['row_num'])


def P2(f):
    f.seek(0)
    df = pd.read_csv(f, names = ['hand', 'bet'], sep = " ")
    #print(df)
    df['rank'] = rank_hand(df['hand'], card_ranks_p2)
    df['value'] = value_hand_p2(df['hand'])

    df = df.sort_values(by=['value', 'rank'], ascending=True)
    df['row_num'] = df.reset_index().index + 1
    #print(df)
    return sum(df['bet']*df['row_num'])


f = open("resources\day7.txt", "r")
print(f"Day 7 P1: {P1(f)} P2: {P2(f)}")
f.close()