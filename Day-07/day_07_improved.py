from statistics import median 

with open('input.txt', 'r') as f:
    input = [int(i) for i in f.read().strip().split(',')]
    
# part 1

def linearCost(i: int) -> int:
    return sum(abs(n - i) for n in input)

median = int(median(input))

print(f'part 1: {linearCost(median)}')

# part 2

def triangularCost(i: int) -> int:
    return sum((abs(n - i) * (abs(n - i) + 1)//2) for n in input)

minimum_value = min(triangularCost(i) for i in range(min(input), max(input)))

print(f'part 2: {minimum_value}')