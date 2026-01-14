from collections import Counter

def get_duplicates(list_obj):
    """
    Returns a list of all items that appear more than once. for one list.
    """
    counts = Counter(list_obj)
    return [item for item, count in counts.items() if count > 1]

# Example Usage:
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape', 'apple']
second_list = ['grape', 'kiwi', 'banana']

duplicates = get_duplicates(my_list)
# print(f"The duplicated items are: {duplicates}")

def check_duplicates_between_lists(list1, list2):
    """
    Checks if there are any duplicates between two lists.
    Returns True if duplicates exist, otherwise False.
    """
    set1 = set(list1)
    set2 = set(list2)
    return not set1.isdisjoint(set2) 

def combine_lists(list1, list2):
    """
    Combines two lists into one.
    """
    return list1 + list2   

def check_distinct_items_between(list1, list2):
    """
    Checks if two lists have all distinct items.
    Returns True if all items are distinct, otherwise False.
    """
    combined = combine_lists(list1, list2)
    return len(combined) == len(set(combined))

def duplicates_between_lists(listA, listB):
    """
    Returns a list of items that are duplicated between two lists.
    
    """
    counterA = Counter(listA)
    counterB = Counter(listB)
    
    common_counts = counterA & counterB
    return list(common_counts.elements())

distinct_items = check_distinct_items_between(my_list, second_list)
print(f"Do the two lists have all distinct items? {distinct_items}")
has_duplicates = check_duplicates_between_lists(my_list, second_list)   
print(f"Are there duplicates between the two lists? {has_duplicates}")
print(f"The duplicates between the two lists are: {duplicates_between_lists(my_list, second_list)}")
    
# is_there_duplicates = get_duplicates(combine_lists(my_list, second_list))
# print(f"The duplicated items between the two lists are: {is_there_duplicates}")

