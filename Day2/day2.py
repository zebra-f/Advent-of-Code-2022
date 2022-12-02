with open("input.txt") as f:
    rounds = [line[:-1].split(" ") for line in f.readlines()]

def part_one(rounds):
    shape_points = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    # A rock, B paper, C scissors
    # X rock, Y paper, Z scissors
    # Win 6
    # Draw 3
    # Lose 0
    outcome_points = {
        ('A', 'X'): 3,
        ('A', 'Y'): 6,
        ('A', 'Z'): 0,
        
        ('B', 'X'): 0,
        ('B', 'Y'): 3,
        ('B', 'Z'): 6,
        
        ('C', 'X'): 6,
        ('C', 'Y'): 0,
        ('C', 'Z'): 3,
    }

    score = 0
    for opponent, your in rounds:
        score += outcome_points[(opponent, your)] + shape_points[your]

    return score

def part_two(rounds):
    # A rock, B paper, C scissors
    # X Lose, Y Draw, Z Win
    outcome_points = {
        ('A', 'X'): 0 + 3,
        ('A', 'Y'): 3 + 1,
        ('A', 'Z'): 6 + 2,
        
        ('B', 'X'): 0 + 1,
        ('B', 'Y'): 3 + 2,
        ('B', 'Z'): 6 + 3,
        
        ('C', 'X'): 0 + 2,
        ('C', 'Y'): 3 + 3,
        ('C', 'Z'): 6 + 1,
    }

    score = 0
    for opponent, outcome in rounds:
        score += outcome_points[(opponent, outcome)]
    
    return score
