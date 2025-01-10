import re

my_arr = []
count = 0
second_count = 0  
sentences = [
    'a Partridge in a Pear Tree.',
    'two Turtle Doves',
    'three French Hens',
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

days = [ 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelth' ]
# creates a list of lists which I use to append the various verse sequences into
number_of_seq = [[] for x in range(12)]
while count < 12:
    count += 1
    for words in sentences[0:count]:
        # adds the 'and' to the first verse after the first verse has been appended 
        if count > 1:
            number_of_seq[count -1].append((words))
            number_of_seq[count -1][0] = "and a Partridge in a Pear tree."
        else:
            number_of_seq[count -1].append((words))
       
while second_count < 12:
    second_count += 1
    # Removes the brackets from the strings and reverses the output to be consisent with the rhyme
    new_seq = re.sub(r'[\[\]]', '', str(number_of_seq[second_count -1][::-1]))
    # Removes single quotes from the output
    removed_apos = new_seq.replace('\'', '') 
    print(f"On the {days[second_count - 1]} day of Christmas my true love gave to me: \n{removed_apos}\n")
    