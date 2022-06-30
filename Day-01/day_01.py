with open('input.txt', 'r') as f:
    input = f.read()

nums = [int(line) for line in input.splitlines()]

count = 0
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        count += 1

print(count)