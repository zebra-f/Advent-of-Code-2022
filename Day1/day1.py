with open("input.txt") as f:
    calories_list = [line[:-1] if line != "\n" else " " for line in f.readlines()]

def most_calories(calories_list: list[str]) -> int:
    current = 0
    maximum = 0
    for calories in calories_list:
        if calories == " ":
            maximum = max(current, maximum)
            current = 0
            continue
        current += int(calories) 

    return maximum