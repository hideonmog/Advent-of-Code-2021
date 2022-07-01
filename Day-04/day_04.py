from turtle import left


with open('input.txt', 'r') as f:
    nums, *boards = f.read().strip().split('\n\n')

nums = [int(x) for x in nums.split(',')]
boards = [[[int(i) for i in j.split()] for j in board.split('\n')] for board in boards]

# print numbers and all boards
# print(nums)
# for board in boards:
#     for j in board:
#         print(j)
    
#     print('\n')

# place an 'x' if a number in the board is called
def mark(number, board):
    for j in board:
        for i in range(0, len(j)):
            if j[i] == number:
                j[i] = 'x'

# sum numbers in board
def sum(board):
    sum = 0
    for j in board:
        for num in j:
            if num != 'x':
                sum += num
    return sum 

# detect win 
def detect_win(board):
    win = False
    for j in board:
        win = all(item in ['x'] for item in j)

        if win:
            return win

    for i in range(0, len(j)):
        win = all(item in ['x'] for item in [j[i] for j in board])

        if win:
            return win

# part1: find the first board that wins and calculate score
def part1():
    for num in nums:
        for board in boards:
            mark(num, board)
            if detect_win(board):
                return sum(board) * num

print(f'The solution to part 1 is: {part1()}')

# part2: find the last board that wins and calculate the score

def part2():
    boards2 = boards.copy()
    nums2 = nums.copy()

    last = False
    while not last:
        for num in nums2:
            for board in boards2:
                mark(num, board)

            index = 0
            while index < len(boards2):
                if detect_win(boards2[index]):
                    if len(boards2) != 1:
                        boards2.pop(index)
                    else: 
                        last = True
                        return sum(boards2[index]) * num
                else:
                    index += 1
    
print(f'The solution to part 2 is: {part2()}')