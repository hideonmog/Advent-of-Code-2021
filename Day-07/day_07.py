from statistics import median 

with open('input.txt', 'r') as f:
    input = [int(i) for i in f.read().strip().split(',')]

def part1():
    med = int(median(input))
    fuel = 0
    for pos in input:
        fuel += abs(pos - med)
    return fuel

print(f'The solution to part 1 is: {part1()}')

def fuelCost(steps): # triangular numbers
    return (steps * (steps + 1)//2)

def part2():
    max_pos = max(input)
    min_pos = min(input)
    minfuel = 1 << 100 # huge number
    for pos in range(min_pos, max_pos):
        fuel = 0
        for crab in input:
            fuel += fuelCost(abs(crab - pos))

        minfuel = min(minfuel, fuel) # keep least amount of fuel saved 

    return minfuel

print(f'The solution to part 2 is: {part2()}')