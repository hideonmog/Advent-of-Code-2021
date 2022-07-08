import statistics
with open('input.txt', 'r') as f:
    input = f.read().strip().splitlines()

open = {'{': '}', '(': ')', '[': ']', '<': '>'}
close = {v: k for k, v in open.items()}

points = {')': 3, ']': 57, '}': 1197, '>': 25137}

def part1():
    score = 0
    for line in input:
        stack = []
        for i in line:
            if i in open:
                stack.append(i)
            elif i in close:
                if close[i] == stack[-1]:
                    stack.pop()
                else:
                    score += points[i]
                    break
    return score

print(f'The solution to part 1 is: {part1()}')

points2 = {')': 1, ']': 2, '}': 3, '>': 4}

def part2():
    scores = []
    for line in input:
        stack = []
        for i in line:
            if i in open:
                stack.append(i)
            elif i in close:
                if close[i] == stack[-1]:
                    stack.pop()
                else:
                    break

        else:
            score = 0
            for i in reversed(stack):
                score *= 5
                score += points2[open[i]]
            scores.append(score)

    return statistics.median(scores)

print(f'The solution to part 2 is: {part2()}')