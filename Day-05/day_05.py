from collections import Counter

with open('input.txt', 'r') as f:
    input = f.read().splitlines()

def hydrothermalvents(diagonals=False):
    allpoints = []
    for line in input:
        firstpos, secondpos = line.split('->')
        x1, y1 = tuple(map(int, firstpos.split(',')))
        x2, y2 = tuple(map(int, secondpos.split(',')))

        # consider horizontal and vertical lines only     
        if x1 == x2 or y1 == y2:
            # calculate points each line goes through and append to list 
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    allpoints.append((x, y))

        # diagonals
        elif diagonals:
            xdir = 1 if x1 < x2 else -1
            ydir = 1 if y1 < y2 else -1
            y = y1  
            for x in range(x1, x2 + xdir, xdir): 
                allpoints.append((x, y))
                # y is only moving up or down 1 so we don't need to loop over y, just add an increment everytime we change x 
                y += ydir 
            
    return len([point for point in Counter(allpoints).values() if point > 1])

print(f'The solution to part 1 is: {hydrothermalvents()}')
print(f'The solution to part 2 is: {hydrothermalvents(diagonals=True)}')