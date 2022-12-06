with open("input.txt") as f:
    signal = f.readline()

def part_one(signal: str) -> int:
    left = 0
    right = 0
    marker = set()
    while len(marker) < 4 and right < len(signal):
        while signal[right] in marker:
            marker.remove(signal[left])
            left += 1

        marker.add(signal[right])
        if len(marker) == 4:
            return right + 1
        right += 1
    
    return 0

def part_two(signal: str) -> int:
    left = 0
    right = 0
    marker = set()
    while len(marker) < 14 and right < len(signal):
        while signal[right] in marker:
            marker.remove(signal[left])
            left += 1

        marker.add(signal[right])
        if len(marker) == 14:
            return right + 1
        right += 1
    
    return 0

        


        



