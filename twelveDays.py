# 12 days of Christmas
# Total number of items 364
the_answer = input("Would you like to play the 12 days of Christmas \nor know a specific days gifts for the 12 days of Christmas?\ntype 'play' to play the song or 'know' to select gifts for a certain day: ").strip()
print(" ")
if the_answer == 'play' or the_answer == 'Play':
    print("The twelve days of Christmas, first published by Angus of Newcastle in the 'Mirth Without Mischief'.")
    print(" ")
the_twelve_days = {
    1:("a partridge in a pear tree.", 1, "first"),
    2:("two turtle doves ", 2, "second"),
    3:("three french hens, ", 3, "third"),
    4:("four colly birds, ", 4, "forth"),
    5:("five gold rings, ", 5, "fifth"),
    6:("six geese a-laying, ", 6, "sixth"),
    7:("seven swans a-swimming, ", 7, "seventh"),
    8:("eight maids a-milking, ", 8,  "eighth"),
    9:("nine ladies dancing, ", 9, "ninth"),
    10:("ten lords a-leaping, ", 10, "tenth"),
    11:("eleven pipers piping, ", 11, "eleventh"),
    12:("twelve drummers drumming, ", 12, "twelfth"),
}

counts_addition = {
    1:(1), # 1
    2:(1 + 2 + 1), # 4
    3:(1 + 2 + 3 + 3 + 1), # 10
    4:(1 + 2 + 3 + 4 + 6 + 3 + 1), # 20
    5:(1 + 2 + 3 + 4 + 5 + 10 + 6 + 3 + 1), # 35 
    6:(1 + 2 + 3 + 4 + 5 + 6 + 15 + 10 + 6 + 3 + 1), # 56 
    7:(1 + 2 + 3 + 4 + 5 + 6 + 7 + 21 + 15 + 10 + 6 + 3 + 1), # 84
    8:(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 28 + 21 + 15 + 10 + 6 + 3 + 1), # 120
    9:(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 36 + 28 + 21 + 15 + 10 + 6 + 3 + 1), # 165
    10:(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 45 + 36 + 28 + 21 + 15 + 10 + 6 + 3 + 1), # 220
    11:(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 55 + 45 + 36 + 28 + 21 + 15 + 10 + 6 + 3 + 1),  # 286
    12:(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 66 + 55 + 45 + 36 + 28 + 21 + 15 + 10 + 6 + 3 + 1), # 364
}

count = 0
day_array = []
lyric_array = []

def count_days():
    """
    outputs the correct day based on the count of the while loop
    """
    for num, days in the_twelve_days.items():
        num_days = days[2]
        # day_number = num[0]
        day_array.append((num_days))
    if count == count:
        return day_array[count -1]
    
def sequence_one():
    """ displays sequence one """
    
    if count > 1 :
        return "\n" + "and " + lyric_array[count -count]
    else:
        return lyric_array[count -count]

def sequence_two():
    """ displays sequence two """
    
    return lyric_array[count -1]
    
def sequence_three():
    """
    displays sequence three
    """
    repeated_sequence = sequence_two()
    return str(repeated_sequence) + "\n" + lyric_array[count -2]

def sequence_four():
    """ displays sequence four """
    
    repeated_sequence = sequence_three()
    return str(repeated_sequence) + "\n" + lyric_array[count -3]

def sequence_five():
    """ displays sequence five """
    
    repeated_sequence = sequence_four()
    return str(repeated_sequence) + "\n" + lyric_array[count -4]

def sequence_six():
    """ displays sequence six """
    
    repeated_sequence = sequence_five()
    return str(repeated_sequence) + "\n" + lyric_array[count -5]

def sequence_seven():
    """ displays sequence seven """
    
    repeated_sequence = sequence_six()
    return str(repeated_sequence) + "\n" + lyric_array[count -6]

def sequence_eight():
    """ displays sequence eight """
    
    repeated_sequence = sequence_seven()
    return str(repeated_sequence) + "\n" + lyric_array[count -7]

def sequence_nine():
    """ displays sequence nine """
    
    repeated_sequence = sequence_eight()
    return str(repeated_sequence) + "\n" + lyric_array[count -8]

def sequence_ten():
    """ displays sequence ten """
    
    repeated_sequence = sequence_nine()
    return str(repeated_sequence) + "\n" + lyric_array[count -9]

def sequence_eleven():
    """ displays sequence eleven """
    
    repeated_sequence = sequence_ten()
    return str(repeated_sequence) + "\n" + lyric_array[count -10]

def sequence_twelve():
    """ displays sequence twelve """
    
    repeated_sequence = sequence_eleven()
    return str(repeated_sequence) + "\n" + lyric_array[count -11]

def count_phrase():
    """
    outputs the correct phrase based on the count of the while loop
    """
    for num, days in the_twelve_days.items():
        lyric = days[0]
        day_num = days[1]
        # day_number = num[0]
        lyric_array.append((lyric))
    # if count == count:
    #     return lyric_array[count -1]
    first_sequence = sequence_one()
    day_one_to_twelve = [1,2,3,4,5,6,7,8,9,10,11,12]
    if count == 1:
        return lyric_array[count - 1]
    elif count == 2:
        sequence = sequence_two()
        return str(sequence) + first_sequence 
    elif count == 3:
        sequence = sequence_three()
        return str(sequence) + first_sequence
    elif count == 4:
        sequence = sequence_four()
        return str(sequence) + first_sequence
    elif count == 5:
        sequence = sequence_five()
        return str(sequence) + first_sequence
    elif count == 6:
        sequence = sequence_six()
        return str(sequence) + first_sequence
    elif count == 7:
        sequence = sequence_seven()
        return str(sequence) + first_sequence
    elif count == 8:
        sequence = sequence_eight()
        return str(sequence) + first_sequence
    elif count == 9:
        sequence = sequence_nine()
        return str(sequence) + first_sequence
    elif count == 10:
        sequence = sequence_ten()
        return str(sequence) + first_sequence
    elif count == 11:
        sequence = sequence_eleven()
        return str(sequence) + first_sequence
    elif count == 12:
        sequence = sequence_twelve()
        return str(sequence) + first_sequence

if the_answer == 'play' or the_answer == 'Play':
    while count < 12:
        count += 1
        reoccuring_song = f"On the {count_days()} day of Christmas my true love sent to me,\n{count_phrase()} \nTotal item count = {counts_addition[count]}\n"
        print(reoccuring_song)     

# have two arrays, one array counts the total of each day and the second array holds the count of the previous days total
# the counts are then added together at each iteration 

# recursive algorith for counting gifts
def gift_count():
    """ 
    calculates the total gift amount for the 12 days of christmas
    """
    new_count = 0
    this_count = 0
    while this_count < 13:
        this_count += 1
        new_count + 1
        
    return new_count


sentences = [
    'A Partridge in a Pear Tree',
    'Two Turtle Doves',
    'Three French Hens',
    'four colly birds',
    'five gold rings',
    'six geese a-laying',
    'seven swans a-swimming',
    'eight maids a-milking',
    'nine ladies dancing',
    'ten lords a-leaping',
    'eleven pipers piping',
    'twelve drummers drumming'
]
if the_answer == 'know' or the_answer == 'Know':
    days = [ 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelth' ]

    day = int(input('What day of Christmas is it? '))

    print("On the {} day of Christmas my true love gave to me:".format(days[day - 1]))

    for sentence in list(reversed(sentences))[-day:]:
        print(sentence)

#!/usr/bin/env python3
"""Twelve Days of Christmas"""

# import argparse
# import sys


# # --------------------------------------------------
# def get_args():
#     """Get command-line arguments"""

#     parser = argparse.ArgumentParser(
#         description='Twelve Days of Christmas',
#         formatter_class=argparse.ArgumentDefaultsHelpFormatter)

#     parser.add_argument('-n',
#                         '--num',
#                         help='Number of days to sing',
#                         metavar='days',
#                         type=int,
#                         default=12)

#     parser.add_argument('-o',
#                         '--outfile',
#                         help='Outfile',
#                         metavar='FILE',
#                         type=argparse.FileType('wt'),
#                         default=sys.stdout)

#     args = parser.parse_args()

#     if args.num not in range(1, 13):
#         parser.error(f'--num "{args.num}" must be between 1 and 12')

#     return args


# # --------------------------------------------------
# def main():
#     """Make a jazz noise here"""

#     args = get_args()
#     verses = map(verse, range(1, args.num + 1))
#     print('\n\n'.join(verses), file=args.outfile)


# # --------------------------------------------------
# def verse(day):
#     """Create a verse"""

#     ordinal = [
#         'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
#         'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'
#     ]

#     gifts = [
#         'A partridge in a pear tree.',
#         'Two turtle doves,',
#         'Three French hens,',
#         'Four calling birds,',
#         'Five gold rings,',
#         'Six geese a laying,',
#         'Seven swans a swimming,',
#         'Eight maids a milking,',
#         'Nine ladies dancing,',
#         'Ten lords a leaping,',
#         'Eleven pipers piping,',
#         'Twelve drummers drumming,',
#     ]

#     lines = [
#         f'On the {ordinal[day - 1]} day of Christmas,',
#         'My true love gave to me,'
#     ]

#     lines.extend(reversed(gifts[:day]))

#     if day > 1:
#         lines[-1] = 'And ' + lines[-1].lower()

#     return '\n'.join(lines)


# # --------------------------------------------------
# def test_verse():
#     """Test verse"""

#     assert verse(1) == '\n'.join([
#         'On the first day of Christmas,', 'My true love gave to me,',
#         'A partridge in a pear tree.'
#     ])

#     assert verse(2) == '\n'.join([
#         'On the second day of Christmas,', 'My true love gave to me,',
#         'Two turtle doves,', 'And a partridge in a pear tree.'
#     ])


# # --------------------------------------------------
# if __name__ == '__main__':
#     main()