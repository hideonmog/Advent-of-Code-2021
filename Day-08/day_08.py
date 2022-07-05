with open('input.txt', 'r') as f:
    input = f.read().strip()

# part 1 

count = 0
for line in input.splitlines():
    _, output = line.split(' | ')
    parts = output.split()
    for part in parts:
        if len(part) in {2, 3, 4, 7}:
            count += 1
        else:
            None

print(f'The solution to part 1 is: {count}')