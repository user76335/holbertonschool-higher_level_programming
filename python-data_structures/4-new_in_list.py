#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Return a copy if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()

    # Copy the original list
    new_list = my_list.copy()

    # Modify only the copy
    new_list[idx] = element

    return new_list


