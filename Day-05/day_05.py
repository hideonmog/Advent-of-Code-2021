from collections import Counter

with open('input.txt', 'r') as f:
    input = f.read().splitlines()

def part1():
    allpoints = []
    for line in input:
        firstpos, secondpos = line.split('->')
        x1, y1 = tuple(map(int, firstpos.split(',')))
        x2, y2 = tuple(map(int, secondpos.split(',')))

        if x1 == x2 or y1 == y2:
            # calculate points each line goes through and append to list 
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    allpoints.append((x, y))

    return len([point for point in Counter(allpoints).values() if point > 1])

print(f'The solution to part 1 is: {part1()}')