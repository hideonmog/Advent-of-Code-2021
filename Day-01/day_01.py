with open('input.txt', 'r') as f:
    input = f.read()

nums = [int(line) for line in input.splitlines()]

count = sum(
    nums[i] > nums[i - 1]
    for i in range(1, len(nums))
)

print(count)