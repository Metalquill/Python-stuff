# Day 3

my_numbers = ['987654321111111', '818181911112111', '234234234234278', '811111111111119']

# Part one
file_name = 'input3.txt'
with open(file_name, 'r') as openfile:
    content = openfile.read().strip()
lines = content.split('\n')

def max_joltage(bank):
    digits = [int(d) for d in bank]
    max_val = 0
    for i in range(len(digits)):
        for j in range(i+1, len(digits)):
            val = digits[i] * 10 + digits[j]
            if val > max_val:
                max_val = val
    return max_val

total_joltage = sum(max_joltage(bank) for bank in lines)
total_joltage_test = sum(max_joltage(bank) for bank in my_numbers)
print("Total output joltage:", total_joltage)
print("Total output joltage test:", total_joltage_test)


# read sequence and find the largest 12 digit number from the sequence of digits in each line
# Part two  

# largest_12_digit_number function now implements a greedy algorithm to select the 12 digits that form the largest possible 12-digit number
# from each sequence in input3.txt. It does this by iteratively choosing 
# the largest available digit at each step, ensuring there are enough remaining digits to complete the selection.

def largest_12_digit_number(bank):
    digits = [int(d) for d in bank]
    n = len(digits)
    k = 12
    result = []
    start = 0
    for i in range(k):
        # find max in start to n - (k - i)
        max_digit = -1
        chosen_pos = -1
        end_range = n - (k - i - 1)
        for j in range(start, end_range):
            if digits[j] > max_digit:
                max_digit = digits[j]
                chosen_pos = j
        result.append(str(max_digit))
        start = chosen_pos + 1
    return int(''.join(result))

total_joltage_part2 = sum(largest_12_digit_number(bank) for bank in lines)
total_joltage_test_part2 = sum(largest_12_digit_number(bank) for bank in my_numbers)
print("Total output joltage part 2:", total_joltage_part2)
print("Total output joltage test part 2:", total_joltage_test_part2)
