import random

def create_numbers():
    lst = []
    for n in range(int(random.uniform(0, 9))):
        lst.append(int(random.uniform(0, 9)))
    return lst

def avg(lst):
    some = 0
    for n in range(len(lst)):
        some = some + lst[n]
    average = float(some) / float(len(lst))
    return average

def print_average(lst):
    try:
        print(f"The average of the random list is{avg(lst)}")
    except ZeroDivisionError as ZD:
        print(ZD)
        return ZD
    except TypeError as TE:
        print(TE)
        return TE
    else:
        return 0

val = 0

while val == 0:
    lst = create_numbers()
    val = print_average(lst)