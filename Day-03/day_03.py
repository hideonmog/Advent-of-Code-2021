with open('input.txt', 'r') as f:
    input = f.read().splitlines()

# part 1

counts = [0] * len(input[0])

for line in input:
    for index, bit in enumerate(line):
        if bit == '1':
            counts[index] += 1
            
gamma_rate = 0
epsilon = 0

for i in range(len(input[0])):
    gamma_rate <<= 1
    epsilon <<= 1
    if counts[i] > len(input)/2:
        gamma_rate += 1
    else:
        epsilon += 1

print(f'The power consumption of the submarine is: {gamma_rate*epsilon}')
