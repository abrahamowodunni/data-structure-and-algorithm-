def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
       ints(list): list of integers containing one or more integers
    """
    
    if len(ints) <= 1:
       return ints[0],ints[0]
    min = max = ints[0]
    for num in ints:
        if num < min:
            min = num
        elif num > max:
            max = num
    return min,max
            

### Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
