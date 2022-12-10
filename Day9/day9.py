with open('input.txt') as f:
    steps = f.readlines()
    steps = [step.strip().split(" ") for step in steps]

def visited_by_tail_f(tail_position: list, visited_by_tail: set) -> int:
    if tuple(tail_position) in visited_by_tail:
        return 0
    else:
        visited_by_tail.add(tuple(tail_position))
        return 1

def part_one(steps: list) -> int:
    visied_by_tail = {(0, 0)}
    visied_by_tail_counter = 1
    head_position = [0, 0]
    tail_position = [0, 0]
    steps_dict = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }
    
    for direction, step in steps:
        for i in range(int(step)):
            head_position[0] += steps_dict[direction][0]
            head_position[1] += steps_dict[direction][1]
            
            if head_position == tail_position:
                continue
            
            directions =  ((0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, 1), (-1, -1), (1, -1))
            close = False
            for x, y in directions:
                current_tail_positon = [*tail_position]
                current_tail_positon[0] += x
                current_tail_positon[1] += y
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
                directions =  ((2, 1), (1, 2), (2, -1), (1, -2), (-2, 1), (-1, 2), (-2, -1), (-1, -2))
                for x, y in directions:
                    new_tail_positon = [*tail_position]
                    new_tail_positon[0] += x
                    new_tail_positon[1] += y
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

            visied_by_tail_counter += visited_by_tail_f(tail_position, visied_by_tail)
            
    return visied_by_tail_counter
