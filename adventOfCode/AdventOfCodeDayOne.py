# Advent of Code day 2
safe_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
                61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

# test_rotations = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']  # Not used, commented out

position = 50
count_o_zeros = 0
fname = "advent-input.txt"
openfile = open(fname, 'r')
lines = openfile.readlines()

def count_zeros_passed(pos, direction, dist):
    count = 0
    for k in range(1, dist):
        if direction == 'R':
            p = (pos + k) % 100
        elif direction == 'L':
            p = (pos - k) % 100
        if p == 0:
            count += 1
    return count

for index, line in enumerate(lines):
    line = line.strip()
    lines[index] = line
    direction = line[0]
    distance = int(line[1:])
    print('Direction: ', direction, 'line: ', line, 'Distance: ', distance)
    
    # Count zeros passed during this move (excluding final position)
    zeros_passed = count_zeros_passed(position, direction, distance)
    count_o_zeros += zeros_passed
    print('Zeros passed during move: ', zeros_passed)
    
    
    # Update position
    if direction == 'L':
        position -= distance
    elif direction == 'R':
        position += distance
    
    # Wrap around
    position %= 100
    print('New position: ', position)
    
    # Count if ends on 0
    if position == 0:
        count_o_zeros += 1
        print('Ended on 0, total count now: ', count_o_zeros)

openfile.close()

print('Total count of zeros: ', count_o_zeros)
import unittest
# from AdventOfCodeDayOne import count_zeros_passed

class TestAdventOfCodeDayOne(unittest.TestCase):
    
    def test_count_zeros_passed_right_small(self):
        # From 50, R 10: positions during: 51 to 59, none 0
        self.assertEqual(count_zeros_passed(50, 'R', 10), 0)
    
    def test_count_zeros_passed_left_small(self):
        # From 50, L 10: positions during: 49 to 41, none 0
        self.assertEqual(count_zeros_passed(50, 'L', 10), 0)
    
    def test_count_zeros_passed_right_wrap(self):
        # From 99, R 5: during: 0,1,2,3 (k=1 to4), 0 is passed
        self.assertEqual(count_zeros_passed(99, 'R', 5), 1)
    
    def test_count_zeros_passed_left_wrap(self):
        # From 1, L 5: during: 0,99,98,97 (k=1 to4), 0 is passed
        self.assertEqual(count_zeros_passed(1, 'L', 5), 1)
    
    def test_count_zeros_passed_no_zero(self):
        # From 10, R 20: during: 11 to 29, none 0
        self.assertEqual(count_zeros_passed(10, 'R', 20), 0)
    
    def test_full_example_simulation(self):
        # Simulate the full test_rotations starting from 50
        test_rotations = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
        position = 50
        count_o_zeros = 0
        for move in test_rotations:
            direction = move[0]
            distance = int(move[1:])
            zeros_passed = count_zeros_passed(position, direction, distance)
            if direction == 'L':
                position -= distance
            elif direction == 'R':
                position += distance
            position %= 100
            count_o_zeros += zeros_passed
            if position == 0:
                count_o_zeros += 1
        self.assertEqual(count_o_zeros, 6)

if __name__ == '__main__':
    unittest.main()