# Advent of Code 2023 Day 20
import re
import queue
from enum import Enum


class Pulse(Enum):
    HIGH = 1
    LOW = 2
    NONE = 0


class Module:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        if self.type == "%":
            self.status = "OFF"
        elif self.type == "&":
            self.status = {}

    def handle_pulse(self, pulse, origin):
        #print (f"{origin} -> {pulse} -> {self.name}")
        if (self.type == "%"):
            if pulse == Pulse.HIGH:
                return Pulse.NONE
            elif self.status == "OFF":
                self.status = "ON"
                return Pulse.HIGH
            else:
                self.status = "OFF"
                return Pulse.LOW
        elif (self.type == "&"):
            self.status[origin] = pulse
            return Pulse.HIGH if list( self.status.values()).count(Pulse.LOW) > 0 else Pulse.LOW
        elif self.type == "":
            return pulse

    def add_input(self, input_val):
        self.status[input_val] = Pulse.LOW


def P1(wf_list, module_list):

    pulse_counter = {Pulse.LOW: 0, Pulse.HIGH: 0}
    loops = 1
    push_button(wf_list, module_list, pulse_counter)
    while not is_initial_status(module_list) and loops < 1000:
        push_button(wf_list, module_list, pulse_counter)
        loops += 1

    #print(pulse_counter)    
    multiplier = 1 if loops == 1001 else (1000//loops) * (1000//loops)
    return pulse_counter[Pulse.HIGH] * pulse_counter[Pulse.LOW] * multiplier

def P2(wf_list, module_list):
    reset_status(module_list)
    pulse_counter = {Pulse.LOW: 0, Pulse.HIGH: 0}
    loops = 1
    res = push_button(wf_list, module_list, pulse_counter, True)
    while not is_initial_status(module_list):
        if res[Pulse.LOW] == 1 and res[Pulse.HIGH] == 0:
            break
        loops += 1
        res = push_button(wf_list, module_list, pulse_counter, True)

    print(loops)    
    return loops

def push_button(wf_list, module_list, pulse_counter, checkRx = False):
    #print("Pushing button on broadcaster")
    q = queue.Queue()
    count_rx_pulses = {Pulse.LOW: 0, Pulse.HIGH: 0}
    q.put({"module": "broadcaster", "pulse": Pulse.LOW, "origin": "broadcaster"})
    while not q.empty():
        current = q.get()
        #print(f"{current['origin']} -> {current['pulse']} -> {current['module']}")
        if checkRx and current["module"] == "rx" and current["pulse"] != Pulse.NONE:
            count_rx_pulses[current["pulse"]] += 1
        if current["pulse"] != Pulse.NONE:
            pulse_counter[current["pulse"]] += 1
        if current["module"] == "broadcaster" or current["module"] in wf_list.keys():
            result = module_list[current["module"]].handle_pulse(current["pulse"], current["origin"])
            if result == Pulse.NONE:
                continue
            for dest in wf_list[current["module"]]["dest"]:
                q.put({"module": dest, "pulse": result,"origin": current["module"]})
    if checkRx:
        return count_rx_pulses


def is_initial_status(module_list):
    for module in module_list.keys():
        if module_list[module].type == "&":
            if list(module_list[module].status.values()).count(Pulse.HIGH) > 0:
                return False
        elif module_list[module].type == "%":
            if module_list[module].status == "ON":
                return False
    return True

def reset_status(module_list):
    for module in module_list.keys():
        if module_list[module].type == "&":
            module_list[module].status = {}
        elif module_list[module].type == "%":
            module_list[module].status = "OFF"

f = open("resources\day20.txt", "r")
content = f.read()

wf_list = {}
module_list = {}
matches = re.findall('([\%\&])?(\w+?)\s->\s(.+)', content)
for m in matches:
    wf_list[m[1]] = {"dest": [i.strip()
                              for i in m[2].split(',')], "type": m[0]}
    if not m[1] in module_list:
        module_list[m[1]] = Module(m[1], m[0])

for wf in wf_list.keys():
    for dest in wf_list[wf]["dest"]:
        if dest in module_list.keys() and module_list[dest].type == "&":
            module_list[dest].add_input(wf)

print(f"P1: {P1(wf_list, module_list)} P2: {P2(wf_list, module_list)}")
f.close()
