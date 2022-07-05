with open('input.txt', 'r') as f:
    input = f.read().strip().splitlines()
    map = [[int(i) for i in list(line)] for line in input]

# part 1

rows = len(map) 
cols = len(map[0])

sol = 0 

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

print(f'The solution to part 1 is: {sol}')