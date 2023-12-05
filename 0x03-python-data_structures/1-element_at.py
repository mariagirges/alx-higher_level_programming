#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
result = element_at(my_list, index)
if result is not None:
    print("Element at index {} is: {}".format(index, result))
else:
    print("Index out of range or negative.")
