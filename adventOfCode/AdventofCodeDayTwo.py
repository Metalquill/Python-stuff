# Day two
test_ranges = ['11-22',
    '95-115',
    '998-1012',
    '1188511880-1188511890',
    '222220-222224',
    '1698522-1698528',
    '446443-446449',
    '38593856-38593862',
    '565653-565659',
    '824824821-824824827',
    '2121212118-2121212124']


# Invalid Ids are made up of the same sequence of digits repeated e.g 55 is 5 twice and is an invalid id

def compare_intra_digits(number):
    """
    Compares the digits within a number to see if any two adjacent digits are the same.
    Returns True if any adjacent digits are the same, otherwise False.
    """
    num_str = str(number)
    length = len(num_str)
    for i in range(length - 1):
        if num_str[i] == num_str[i + 1]:
            return True
    return False

def get_first_digit_str(number):
    """
    Gets the first digit of an integer by converting it to a string.
    """
    # Convert the number to a string and remove the negative sign if present
    num_str = str(abs(number)) 
    # Access the first character (index 0) and convert it back to an integer
    first_digit = int(num_str[0])
    print("the number: ", first_digit)
    return first_digit


def is_invalid(number):
    """
    Checks if a number is invalid: composed of two identical halves.
    Returns True if invalid, False otherwise.
    """
    num_str = str(number)
    length = len(num_str)
    if length % 2 != 0:
        return False
    half = length // 2
    return num_str[:half] == num_str[half:]

def is_invalid_v2(number):
    """
    Checks if a number is invalid: made of some sequence of digits repeated at least twice.
    Returns True if invalid, False otherwise.
    """
    num_str = str(number)
    length = len(num_str)
    for d in range(1, length // 2 + 1):
        if length % d == 0:
            unit = num_str[:d]
            if unit * (length // d) == num_str:
                return True
    return False

fname = "advent-input-1.txt"
with open(fname, 'r') as openfile:
    content = openfile.read().strip()

ranges = content.split(',')

# Day two part one
# total_invalid = []
# for range_str in ranges:
#     parts = range_str.split('-')
#     start = int(parts[0])
#     end = int(parts[1])
#     invalid_in_range = []
#     for num in range(start, end + 1):
#         if is_invalid(num):
#             invalid_in_range.append(num)
#     total_invalid.extend(invalid_in_range)
#     print(f"Range {start}-{end}: invalid IDs: {invalid_in_range}")

# print(f"Total invalid IDs: {len(total_invalid)}")
# print(f"Sum of Invalid IDs: {sum(total_invalid)}")

# Day two part one test
# test_total_invalid = []
# for test_range_str in test_ranges:
#     parts = test_range_str.split('-')
#     start = int(parts[0])
#     end = int(parts[1])
#     invalid_in_range = []
#     for num in range(start, end + 1):
#         if is_invalid(num):
#             invalid_in_range.append(num)
#     test_total_invalid.extend(invalid_in_range)
#     print(f"Range {start}-{end}: invalid IDs: {invalid_in_range}")

# Day two part two test
# test_total_invalid_v2 = []  
# for test_range_str in test_ranges:
#     parts = test_range_str.split('-')
#     start = int(parts[0])
#     end = int(parts[1])
#     invalid_in_range_v2 = []
#     for num in range(start, end + 1):
#         if is_invalid_v2(num):
#             invalid_in_range_v2.append(num)
#     test_total_invalid_v2.extend(invalid_in_range_v2)
#     print(f"Range {start}-{end}: invalid IDs (v2): {invalid_in_range_v2}")
#     print(f"Sum of Invalid IDs: {sum(test_total_invalid_v2)}")
    
# Day two part two
total_invalid_v2 = []
total_invalid = []
for range_str in ranges:
    parts = range_str.split('-')
    start = int(parts[0])
    end = int(parts[1])
    invalid_in_range_v2 = []
    for num in range(start, end + 1):
        if is_invalid_v2(num):
            invalid_in_range_v2.append(num)
    total_invalid_v2.extend(invalid_in_range_v2)
    print(f"Range {start}-{end}: invalid IDs: {invalid_in_range_v2}")
    print(f"Sum of Invalid IDs: {sum(total_invalid_v2)}")
