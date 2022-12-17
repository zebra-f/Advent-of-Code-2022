with open('input.txt') as f:
    program = f.readlines()
    program = [instruction.strip().split(" ") for instruction in program]

def part_one(program):
    x = 1
    singal_strength = 0
    
    cycle = 1
    important_cycle = 20
    multiplicator = 1
    
    addx = None
    for instruction in program:
        if len(instruction) == 2:
            addx = int(instruction[1])
            cycle += 1
        else:
            cycle += 1
        
        while True:
            if cycle == important_cycle * multiplicator:
                singal_strength +=  x * (important_cycle * multiplicator)
                multiplicator += 2
            if addx:
                cycle += 1
                x += addx
                addx = None
                continue
            break
    
    return singal_strength
