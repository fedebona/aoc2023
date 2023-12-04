# Advent of Code 2023 Day 1
import re

digit_dictionary = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,       
    "nine": 9
}

def day1_1(f):
    calibration_array = []
    for x in f:
        #print(x)
        m = re.findall('\d', x)
        #print(m[0])
        #print(m[len(m)-1])
        calibration_value_str = m[0] + m[len(m)-1]  # combine the first and last string
        calibration_array.append(int(calibration_value_str))
    return sum(calibration_array)

def day1_2(f):
    calibration_array = []
    for x in f:
        #print(x)
        m = re.findall('\d|one|two|three|four|five|six|seven|eight|nine', x)
        first = get_digit(m[0])
        #Regex to find all digits getting only the last one that matches in case of chained digits.
        #e.g. oneight will return eight in this second regex and one in the first regex
        m = re.findall('\d|one(?!ight)|two(?!ne)|three(?!ight)|four|five(?!ight)|six|seven(?!ine)|eight(?!hree|wo)|nine(?!ight)', x)
        last = get_digit(m[len(m)-1])
        calibration_value_str =first + last  # combine the first and last string
        #print(calibration_value_str)
        calibration_array.append(int(calibration_value_str))
    #print(calibration_array)
    return sum(calibration_array)

def get_digit(thedigit):
    value = digit_dictionary.get(thedigit) or thedigit
    return str(value)

f = open("resources\day1.txt", "r")
print("Calibration Total: " + str(day1_1(f)))
f.close()

f = open("resources\day1.txt", "r")
print("Calibration Total: " + str(day1_2(f)))
f.close()
