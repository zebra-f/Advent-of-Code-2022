import string


with open("input.txt") as f:
    rucksacks = [rucksack[:-1] for rucksack in f.readlines()]

lowercase_priority = {letter: i + 1 for i, letter in enumerate(string.ascii_lowercase)}
upercase_priority = {letter: i + 27 for i, letter in enumerate(string.ascii_uppercase)}
priority = {**lowercase_priority, **upercase_priority}

def part_one(rucksacks: list[str]) -> int:
    count = 0
    for rucksack in rucksacks:
        first_compartment =  set(rucksack[:len(rucksack)//2])
        second_compartment = set(rucksack[len(rucksack)//2:])

        common_item = first_compartment.intersection(second_compartment).pop()
        count += priority[common_item]

    return count

def part_two(rucksacks: list[str]) -> int:
    count = 0
    for i in range(0, len(rucksacks), 3):
        rucksack_sets = []
        for j in range(i+1, i+3):
            rucksack = set(rucksacks[j])
            rucksack_sets.append(rucksack)
        
        common_item = set(rucksacks[i]).intersection(rucksack_sets[0], rucksack_sets[1]).pop()
        count += priority[common_item]

    return count
