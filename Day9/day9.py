with open('input.txt') as f:
    steps = f.readlines()
    steps = [step.strip().split(" ") for step in steps]

def head_positions_f(steps):
    steps_dict = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1)
    } 
    head_positions = [[0, 0]]
    head_position = [0, 0]
    for direction, step in steps:
        for i in range(int(step)):
            head_position[0] += steps_dict[direction][0]
            head_position[1] += steps_dict[direction][1]
            head_positions.append([*head_position])
    return head_positions

head_positions = head_positions_f(steps)

def visited_by_tail_f(tail_position: list, visited_by_tail: set) -> int:
    if tuple(tail_position) in visited_by_tail:
        return 0
    else:
        visited_by_tail.add(tuple(tail_position))
        return 1

def part_one(head_positions: list) -> int:
    visied_by_tail = {(0, 0)}
    visied_by_tail_counter = 1
    
    head_position = [0, 0]
    tail_position = [0, 0]
    tail_positions = [[0, 0]]
    
    for head_position in head_positions:
        if head_position == tail_position:
            continue
        
        directions =  ((0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, 1), (-1, -1), (1, -1))
        close = False
        for x, y in directions:
            current_tail_positon = [tail_position[0]+x, tail_position[1]+y]
            if current_tail_positon == head_position:
                close = True
                break
        if close:
            continue

        if abs(head_position[0] - tail_position[0]) == 2 and head_position[1] == tail_position[1]:
            if head_position[0] > tail_position[0]:
                tail_position[0] += 1
            else:
                tail_position[0] -= 1
        elif abs(head_position[1] - tail_position[1]) == 2 and head_position[0] == tail_position[0]:
            if head_position[1] > tail_position[1]:
                tail_position[1] += 1
            else:
                tail_position[1] -= 1
        else:
            directions =  ((2, 1), (1, 2), (2, -1), (1, -2), (-2, 1), (-1, 2), (-2, -1), (-1, -2), (2, 2), (2, -2), (-2, 2), (-2, -2))
            for x, y in directions:
                new_tail_positon = [tail_position[0]+x, tail_position[1]+y]
                if new_tail_positon == head_position:
                    if new_tail_positon[0] > tail_position[0]:
                        tail_position[0] += 1
                        if new_tail_positon[1] > tail_position[1]:
                            tail_position[1] += 1
                        else:
                            tail_position[1] -= 1
                    else:
                        tail_position[0] -= 1
                        if new_tail_positon[1] > tail_position[1]:
                            tail_position[1] += 1
                        else:
                            tail_position[1] -= 1
                    break
        
        tail_positions.append([*tail_position])
        visied_by_tail_counter += visited_by_tail_f(tail_position, visied_by_tail)
    
    return visied_by_tail_counter, tail_positions

def part_two(part_one_output, i, rope_length):
    visited_by_tail_counter = part_one_output[0]
    head_positions = part_one_output[1]
    if i == rope_length:
        return visited_by_tail_counter
    return part_two(part_one(head_positions), i+1, rope_length) + 0