with open("input.txt") as f:
    pairs = [[line.strip().split(",")[0].split("-"), line.strip().split(",")[1].split("-")] for line in f]

def part_one(pairs):
    contains_other_counter = 0
    for first, second in pairs:
        first = [int(first[0]), int(first[1])]
        second = [int(second[0]), int(second[1])]
        
        if first[0] <= second[0] and first[1] >= second[1]:
            contains_other_counter += 1
        elif second[0] <= first[0] and second[1] >= first[1]:
            contains_other_counter += 1
    
    return contains_other_counter

def part_two(pairs):
    overlap_counter = 0
    for first, second in pairs:
        first = [int(first[0]), int(first[1])]
        second = [int(second[0]), int(second[1])]

        if second[0] <= first[0] <= second[1] or second[0] <= first[1] <= second[1]:
            overlap_counter += 1
        elif first[0] <= second[0] <= first[1] or first[0] <= second[1] <= first[1]:
            overlap_counter += 1

    return overlap_counter

