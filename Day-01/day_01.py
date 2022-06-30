with open('input.txt', 'r') as f:
    input = f.read()

# part 1

nums = [int(line) for line in input.splitlines()]

count = sum(
    nums[i] > nums[i - 1]
    for i in range(1, len(nums))
)

print(f'Count for part 1: {count}')

# part 2

count = sum(
    nums[i] > nums[i - 3]
    for i in range(3, len(nums))
)

print(f'Count for part 1: {count}')