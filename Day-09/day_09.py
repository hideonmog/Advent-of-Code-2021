import numpy as np
with open('input.txt', 'r') as f:
    input = f.read().strip().splitlines()
    map = [[int(i) for i in list(line)] for line in input]

# part 1

rows = len(map) 
cols = len(map[0])

sol = 0 
minimas = []  # need to store minimas for part 2
for i in range(rows):
    for j in range(cols):
        lowest = True 
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x = i + d[0]
            y = j + d[1]

            if not ((0 <= x and x < rows) and (0 <= y and y < cols)):
                continue

            if map[x][y] <= map[i][j]:
                lowest = False
                break
        
        if lowest:
            sol +=  map[i][j] + 1
            minimas.append((i, j))

print(f'The solution to part 1 is: {sol}')

# part 2

basins = np.zeros((rows, cols), dtype = int) # map of 0s
id = 1 # id of basin, id = 0 is 9s
# depth first search 
for i, j in minimas:
    stack = [(i, j)]
    seen = set()
    while len(stack) > 0:
        i, j = stack.pop()

        if (i, j) in seen:
            continue

        seen.add((i, j))
        basins[i, j] = id

        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x = i + d[0]
            y = j + d[1]

            if not ((0 <= x and x < rows) and (0 <= y and y < cols)):
                continue

            if map[x][y] == 9:
                continue
            
            if map[x][y] > map[i][j]:
                stack.append((x, y))

    id += 1

sizes = [0] * id # initialize a count for each basin

for m in basins.flatten():
    sizes[m] += 1

sizes = sizes[1:] # ignnore first item because it is the 9s
sizes.sort()
top3  = sizes[-1] * sizes[-2] * sizes[-3]

print(f'The solution to part 2 is: {top3}')