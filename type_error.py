import zero_division
import random


def randomly_stringify_list_items(lst):
    length = len(lst)
    index = int(random.uniform(0, length))
    lst[index] = 'e'


val = 0

while val == 0:
    lst = zero_division.create_numbers()
    randomly_stringify_list_items(lst)
    val = zero_division.print_average(lst)
