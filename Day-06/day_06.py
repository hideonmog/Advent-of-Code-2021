from collections import defaultdict 

with open('input.txt', 'r') as f:
    input = [int(i) for i in f.read().strip().split(',')]

def part1():
    allFish = input.copy()
    days = 80
    while days > 0:
        for fish in range(len(allFish)):
            if allFish[fish] == 0:
                allFish[fish] = 7
                allFish.append(9)
        for fish in range(len(allFish)):
            allFish[fish] -= 1

        days -= 1
    return len(allFish)

print(f'The solution to part 1 is: {part1()}')

def part2(days):
    allFish = input.copy()
    fishdict = {}
    for fish in allFish:
        if fish not in fishdict:
            fishdict[fish] = 0
        fishdict[fish] += 1

    for day in range(days):
        updated_fishdict = defaultdict(int) # use defaultdict to avoid key error 
        for fish, count in fishdict.items():
            if fish == 0:
                updated_fishdict[6] += count
                updated_fishdict[8] += count
            else: 
                updated_fishdict[fish - 1] += count

            fishdict = updated_fishdict

    return sum(fishdict.values())

print(f'The solution to part 2 is: {part2(256)}')