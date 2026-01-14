# Advent of code day 1
safe_numbers = [0, 1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
                41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,
                61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,
                81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]

# For the test example
test_rotations = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
# create function for moving left or right (if L)
test_position = 50
test_count_o_zeros = 0 

def count_zeros_passed(pos, direction, dist):
    count = 0
    for k in range(1, dist):  # During the move, k=1 to dist-1 (exclude start)
        if direction == 'R':
            p = (pos + k) % 100
        elif direction == 'L':
            p = (pos - k) % 100
        if p == 0:
            count += 1
    return count

for thing in enumerate(test_rotations):
    test_direction = thing[1][0]
    test_distance = int(thing[1][1:])
    print('Direction: ', test_direction, 'thing: ', thing, 'Distance: ', test_distance)
    
    # Update position and if position is equal to zero add 1 to count_o_zeros
    # if position gets to zero and goes below zero we need to wrap around the safe_numbers list
    zeros_passed = count_zeros_passed(test_position, test_direction, test_distance)
    test_count_o_zeros += zeros_passed
    print('Zeros passed during move: ', zeros_passed)
    if test_direction == 'L':
        test_position -= test_distance
    elif test_direction == 'R':
        test_position += test_distance
    
    # Wrap around using modulo
    test_position %= 100
    print('New position: ', test_position)
    
    if test_position == 0:
         test_count_o_zeros += 1
    
    # if test_direction == 'L':
    #     test_position -= test_distance
    #     if test_position < 0:
    #         test_position = test_position + len(safe_numbers)
    #     print('New position (left): ', test_position)
    #     if test_position == 0:
    #         test_count_o_zeros += 1
    # elif test_direction == 'R':
    #     test_position += test_distance
    #     if test_position >= len(safe_numbers):
    #         test_position = test_position - len(safe_numbers)
    #     print('New position (right): ', test_position)
    #     if test_position == 0:
    #         test_count_o_zeros += 1


print('count of zeros in the test example: ', test_count_o_zeros)

# Day one working code
position = 50 
count_o_zeros = 0
fname = "advent-input.txt"
openfile = open(fname, 'r')
lines = openfile.readlines()

for index, line in enumerate(lines):
    line = line.strip()
    lines[index] = line
    direction = line[0]
    distance = int(line[1:])
    print('Direction: ', direction, 'line: ', line, 'Distance: ', distance)
    
    if direction == 'L':
        position -= distance
    elif direction == 'R':
        position += distance
    
    # Wrap around using modulo
    position %= 100
    print('New position: ', position)
    
    if position == 0:
        count_o_zeros += 1

openfile.close()


# print('lines:   ', lines)
print('count of zeros: ', count_o_zeros)