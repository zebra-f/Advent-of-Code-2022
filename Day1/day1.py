with open("input.txt") as f:
    calories_list = [line[:-1] if line != "\n" else " " for line in f.readlines()]

def part_one(calories_list: list[str]) -> int:
    current = 0
    maximum = 0
    for calories in calories_list:
        if calories == " ":
            maximum = max(current, maximum)
            current = 0
            continue
        current += int(calories) 

    return maximum

def part_two_1(calories_list: list[str]) -> int:

    current = 0
    maximum = [0 for i in range(3)]
    
    for calories in calories_list:
        if calories == " ":
            maximum.append(current)
            i = len(maximum) - 1
            while i > 0 and maximum[i] > maximum[i-1]:
                maximum[i], maximum[i-1] = maximum[i-1], maximum[i]
                i -= 1
            maximum.pop()
            current = 0
            continue
        current += int(calories) 
    
    return sum(maximum)

def part_two_2(calories_list: list[str]) -> int:

    current = 0
    calories_sum_list = []

    for calories in calories_list:
        if calories == " ":
            calories_sum_list.append(current)
            current = 0
            continue
        current += int(calories)
    
    return sum(sorted(calories_sum_list, reverse=True)[:3])
