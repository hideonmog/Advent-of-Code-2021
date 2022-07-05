with open('input.txt', 'r') as f:
    data = f.read().strip().splitlines()

# part 1 

def part1():
    count = 0
    for line in data:
        _, output = line.split(' | ')
        parts = output.split()
        for part in parts:
            if len(part) in {2, 3, 4, 7}:
                count += 1

    print(f'The solution to part 1 is: {count}')

part1()

# part 2

def part2():
    inputs = [line.split(' | ')[0].strip().split() for line in data]
    outputs = [line.split(' | ')[1].strip().split() for line in data]
    totalCount = 0

    for i in range(len(data)):
        map = {}
        # known digits 1, 4, 7 , 8
        for digit in inputs[i]:
            if len(digit) ==  2:
                map[1] = digit
            elif len(digit) == 4:
                map[4] = digit
            elif len(digit) == 3:
                map[7] = digit
            elif len(digit) == 7:
                map[8] = digit
        # unknown digits
        for digit in inputs[i]:
            # for 0, 6, 9 which all have length 6
            if len(digit) == 6:
                # 4 is part of 9
                if set(map[4]).issubset(set(digit)):
                    map[9] = digit
                # 1 is part of 0
                elif set(map[1]).issubset(set(digit)):
                    map[0] = digit
                # 6 has to be whatever is left
                else:
                    map[6] = digit
        for digit in inputs[i]:
            # for 2, 3, 5 which all have lengths of 5
            if len(digit) == 5:
                # 5 is part of 6
                if set(digit).issubset(set(map[6])):
                    map[5] = digit
                # 1 is part of 3
                elif set(map[1]).issubset(set(digit)):
                    map[3] = digit
                # 2 has to be whatever is left
                else:
                    map[2] = digit

        number = []
        for digit in outputs[i]:
            for key, value in map.items():
                if set(digit) == set(value):
                    number.append(str(key))

        number = int(''.join(number))
        totalCount += number

    return totalCount


print(f'The solution to part 2 is: {part2()}')