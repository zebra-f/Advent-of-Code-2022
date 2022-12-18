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

def part_two(program):  
    
    def increment_cycle(rows, cycle, x, addx=None):
        cycle += 1
        if cycle - 1 in (x - 1, x, x + 1):
            rows[cycle-1] = '#'
        if cycle in (40, 80, 120, 160, 200, 240):
            x += 40
        if addx:
            x += addx
        return cycle, x

    rows = ['.' for _ in range(240)]

    # sprite position
    x = 1
    cycle = 0
    addx = None
    for instruction in program:
        if len(instruction) == 2:
            addx = int(instruction[1])
        
        cycle, x = increment_cycle(rows, cycle, x)
        
        if addx:
            cycle, x = increment_cycle(rows, cycle, x, addx)
            addx = None

    left = 0
    right = 40
    for _ in range(6):
        print("".join(rows[left:right]))
        left += 40
        right += 40
    
    return rows
