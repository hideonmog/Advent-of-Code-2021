with open('input.txt', 'r') as f:
    input = f.read().splitlines()

# part 1

counts = [0] * len(input[0])

for line in input:
    for index, bit in enumerate(line):
        if bit == '1':
            counts[index] += 1
            
gamma_rate = []
epsilon = []

for i in range(len(input[0])):
    if counts[i] > len(input)/2:
        gamma_rate.append('1')
        epsilon.append('0')
    else:
        gamma_rate.append('0')
        epsilon.append('1')

gamma_rate = int(''.join(gamma_rate), 2)
epsilon = int(''.join(epsilon), 2)

print(f'The power consumption of the submarine is: {gamma_rate*epsilon}')