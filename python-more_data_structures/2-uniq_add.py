#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)  # Convert the list to a set to remove duplicates
    total = 0
    for num in unique:
        total += num
    return total
