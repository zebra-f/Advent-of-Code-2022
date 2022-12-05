from copy import deepcopy


with open("input1.txt") as f:
    lines = f.readlines()
    length = len(lines[0])
    stacks = [[] for _ in range(length//4)]
    for line in list(reversed(lines))[1:]:
        i = 1
        stacks_i = 0
        while i < length:
            if line[i].isalpha():
                stacks[stacks_i].append(line[i])
            i += 4
            stacks_i += 1

with open("input2.txt") as f:
    lines = f.readlines()
    procedures = []
    for line in lines:
        procedure = line.strip().split(" ")
        procedure = [int(procedure[i]) for i in (1, 3, 5)]
        procedures.append(procedure)

def part_one(procedures: list[list[int]], stacks: list[list[str]]) -> str:
    stacks = deepcopy(stacks)
    
    for procedure in procedures:
        move = procedure[0]
        from_ = procedure[1] - 1
        to = procedure[2] - 1
        for _ in range(move):
            crate = stacks[from_].pop()
            stacks[to].append(crate)

    messasge = ""
    for stack in stacks:
        if stack:
            messasge += stack[len(stack)-1]
    return messasge

def part_two(procedures: list[list[int]], stacks: list[list[str]]) -> str:
    stacks = deepcopy(stacks)
    
    for procedure in procedures:
        move = procedure[0]
        from_ = procedure[1] - 1
        to = procedure[2] - 1

        crates = stacks[from_][-move:]
        stacks[from_] = stacks[from_][:-move]
        stacks[to] = [*stacks[to], *crates]

    message = ""
    for stack in stacks:
        if stack:
            message += stack[len(stack)-1]
    return message




        


