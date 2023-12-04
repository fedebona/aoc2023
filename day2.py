# Advent of Code 2023 Day 2

bags_limit = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def day2_1(f):
    gamesOK = []
    gameId = 0
    for line in f:
        gameId = gameId + 1
        game = analyze_game(line)
        if validate_game(bags_limit, game):
            gamesOK.append(gameId)
    #print (gamesOK)
    return sum(gamesOK)  #calculate

def analyze_game(line):
    set_list= line.split(": ")[1].split("; ")
    game = []
    for set_line in set_list:
        color_lines = set_line.split(", ")
        set = {}
        for color_line in color_lines:
            set[color_line.split(" ")[1].strip()] = int(color_line.split(" ")[0]) 
        game.append(set)    
    return game

def validate_game(bags_limit, game):
    for set in game:
        for key in bags_limit:
            if(key in set):                
                if bags_limit[key] < set[key]:
                    #TODO: check limits better
                    return False
    return True

def day2_2(f):
    powers = []
    gameId = 0
    for line in f:
        gameId = gameId + 1
        game = analyze_game(line)
        powers.append(calculate_power_game(game))
    #print(powers)
    return sum(powers)  #calculate

def calculate_power_game(game):
    min_colors = { "red": 0, "green": 0, "blue": 0 }
    for set in game:
        for key in set:
            if set[key] > min_colors[key]:
                min_colors[key] = set[key]
    return min_colors["red"]*min_colors["green"]*min_colors["blue"]

f = open("resources\day2.txt", "r")
print("Result 2.1: " + str(day2_1(f)))
f.close()

f = open("resources\day2.txt", "r")
print("Result 2.2: " + str(day2_2(f)))
f.close()
