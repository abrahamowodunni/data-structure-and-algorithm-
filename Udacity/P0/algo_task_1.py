def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # base case
    if number <= 1:
        return number 

    # updating mid 
    start,end = 0,number
    while start <= end:
        mid = (start + end)//2
        multi_mid = mid * mid

        if multi_mid == number:
            return mid
        elif multi_mid <= number:
            start += 1
            result = mid

        else:
            end = mid - 1
    return result

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")