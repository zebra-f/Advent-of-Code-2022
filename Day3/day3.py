import string


with open("input.txt") as f:
    rucksacks = [rucksack[:-1] for rucksack in f.readlines()]

lowercase_priority = {letter: i + 1 for i, letter in enumerate(string.ascii_lowercase)}
upercase_priority = {letter: i + 27 for i, letter in enumerate(string.ascii_uppercase)}
priority = {**lowercase_priority, **upercase_priority}

def part_one(rucksacks):
    count = 0
    for rucksack in rucksacks:
        first_compartment =  set(rucksack[:len(rucksack)//2])
        second_compartment = set(rucksack[len(rucksack)//2:])

        common_item = first_compartment.intersection(second_compartment).pop()
        count += priority[common_item]

    return count
