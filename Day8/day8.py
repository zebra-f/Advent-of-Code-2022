with open('input.txt') as f:
    grid = [list(line.strip()) for line in f.readlines()]
    grid = [[int(grid[i][j]) for j in range(len(grid[i]))] for i in range(len(grid))]

def border_indices(grid: list[list]) -> set[tuple]:
    indicies = set()
    for i in range(len(grid[0])):
        indicies.add((0, i))
        indicies.add((len(grid) - 1, i))
    for i in range(len(grid)):
        indicies.add((i, 0))
        indicies.add((i, len(grid) - 1))
    return indicies

def part_one(grid: list[list]) -> int:
    visible_counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in border_indices(grid):
                visible_counter += 1
                continue
            current = grid[i][j]
            
            visible = True
            top = i - 1
            while top >= 0 and visible:
                if grid[top][j] >= current:
                    visible = False
                top -= 1
            if visible:
                visible_counter += 1
                continue

            visible = True
            bottom = i + 1
            while bottom < len(grid) and visible:
                if grid[bottom][j] >= current:
                     visible = False
                bottom += 1
            if visible:
                visible_counter += 1
                continue

            visible = True
            left = j - 1
            while left >= 0 and visible:
                if grid[i][left] >= current:
                    visible = False
                left -= 1
            if visible:
                visible_counter += 1
                continue

            visible = True
            right = j + 1
            while right < len(grid[0]) and visible:
                if grid[i][right] >= current:
                    visible = False
                right += 1
            if visible:
                visible_counter += 1
                continue
    
    return visible_counter

def part_two(grind: list[list]) -> int:
    max_viewing_distance = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            viewing_distances = []
            current = grid[i][j]
            
            viewing_distance = 0
            top = i - 1
            while top >= 0:
                viewing_distance += 1
                if grid[top][j] >= current:
                    break
                top -= 1
            viewing_distances.append(viewing_distance)

            viewing_distance = 0
            bottom = i + 1
            while bottom < len(grid):
                viewing_distance += 1
                if grid[bottom][j] >= current:
                     break
                bottom += 1
            viewing_distances.append(viewing_distance)

            viewing_distance = 0
            left = j - 1
            while left >= 0:
                viewing_distance += 1
                if grid[i][left] >= current:
                    break
                left -= 1
            viewing_distances.append(viewing_distance)

            viewing_distance = 0
            right = j + 1
            while right < len(grid[0]):
                viewing_distance += 1
                if grid[i][right] >= current:
                    break
                right += 1
            viewing_distances.append(viewing_distance)

            scenic_score = viewing_distances[0]
            for distance in viewing_distances[1:]:
                scenic_score *= distance
            
            max_viewing_distance = max(max_viewing_distance, scenic_score)
    
    return max_viewing_distance
