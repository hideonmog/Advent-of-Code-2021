with open('input.txt', 'r') as f:
    input = f.read()

# part 1

directions = [(line.split(' ')[0], int(line.split()[1])) for line in input.splitlines()]

position = depth = 0

for direction, n in directions:
    if direction == 'forward':
        position += n
    elif direction == 'up':
        depth -= n
    elif direction == 'down':
        depth += n
    else:
        None

print(f'The final horizontal position multiplied by final depth = {position*depth}')

# part 2

position = depth = aim = 0

for direction, n in directions:
    if direction == 'up':
        aim -= n
    elif direction == 'down':
        aim += n
    elif direction == 'forward':
        position += n
        depth += aim * n
    else:
        None

print(f'The new final horizontal position multiplied by final depth = {position*depth}')