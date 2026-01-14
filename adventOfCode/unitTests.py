# test_AdventOfCodeDayOne.py
import unittest
from AdventOfCodeDayOne import count_zeros_passed

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