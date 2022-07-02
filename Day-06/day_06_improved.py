from collections import Counter

with open('input.txt', 'r') as f:
    input = [int(i) for i in f.read().strip().split(',')]

def fish(days):
    states = Counter(input)
    for i in range(days):
        states2 = Counter({6: states[0], 8: states[0]})
        states2.update({k - 1: v for k, v in states.items() if k > 0})
        states = states2
    return sum(states.values())

print(f'part 1: {fish(80)}')
print(f'part 2: {fish(256)}')