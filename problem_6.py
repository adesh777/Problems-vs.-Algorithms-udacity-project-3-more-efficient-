def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None
    minimum = maximum = ints[0]
    for i in ints[1:]:
        if i < minimum: 
            minimum = i 
        else: 
            if i > maximum: maximum = i
    return (minimum,maximum)
import random

l = [i for i in range(0, 10)] 
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
l = [i for i in range(300, 301)] 
random.shuffle(l)
print("Pass" if ((300, 300) == get_min_max(l)) else "Fail")
l = []
random.shuffle(l)
print("Pass" if (None == get_min_max(l)) else "Fail")
l = [i for i in range(-24, -1)] 
random.shuffle(l)
print("Pass" if ((-24, -2) == get_min_max(l)) else "Fail")