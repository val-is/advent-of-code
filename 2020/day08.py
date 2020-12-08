inputs = [str(i) for i in open('inputs/day8.txt', 'r').readlines()]

import re

instr = []
for i in inputs:
    t, val = i.split(" ")
    instr.append([t, int(val)])

def run_instrs_1(instrs):
    acc = 0
    pointer = 0
    done = []
    while True:
        if pointer in done:
            return acc
        done += [pointer]
        t, val = instrs[pointer]
        if t == "acc":
            acc += val
            pointer += 1
        elif t == "jmp":
            pointer += val
        elif t == "nop":
            pointer += 1


part1 = run_instrs_1(instr)
print(f"Part 1: {part1}")

import time
mTime = 0.1

def run_instrs_2(instrs):
    starttime = time.time()
    acc = 0
    pointer = 0
    while True:
        if pointer == len(instr):
            return acc
        t, val = instrs[pointer]
        if t == "acc":
            acc += val
            pointer += 1
        elif t == "jmp":
            pointer += val
        elif t == "nop":
            pointer += 1
        if time.time()-starttime > mTime:
            return None

instr_perms = []
for index in range(len(instr)):
    x = []
    for k, v in enumerate(instr):
        nv = v.copy()
        if index == k:
            if nv[0] == "jmp":
                nv[0] = "nop"
            elif nv[0] == "nop":
                nv[0] = "jmp"
        x.append(nv)
    instr_perms.append(x)

for instrs in instr_perms:
    x = run_instrs_2(instrs)
    if x != None:
        print(x)

part2 = 0
print(f"Part 2: {part2}")