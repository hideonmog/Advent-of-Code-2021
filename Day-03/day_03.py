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

# part 2

input2 = input.copy()
index = 0
while len(input2) !=1:
    one = 0
    zero = 0
    ones = []
    zeros = []
    for line in input2:
        if line[index] == '0':
            zero += 1
            zeros.append(line)
        else:
            one += 1
            ones.append(line)
    if zero > one:
        input2 = zeros
    else:
        input2 = ones
    index += 1

oxygen = int(''.join(input2), 2)

input2 = input.copy()
index = 0
while len(input2) !=1:
    one = 0
    zero = 0
    ones = []
    zeros = []
    for line in input2:
        if line[index] == '0':
            zero += 1
            zeros.append(line)
        else:
            one += 1
            ones.append(line)
    if zero > one:
        input2 = ones
    else:
        input2 = zeros
    index += 1

co2 = int("".join(input2), 2)

print(f'The life support rating of the submarine is: {oxygen*co2}')