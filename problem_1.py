import math
def sqrt(number):
    if(number==0 or number==1):
        return number
    if number < 0:
        return math.nan
    i =1
    result = 1
    while(result<=number):
        i+=1
        result = i*i
    return i-1

    
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print("Pass: sqrt(-1) == math.nan" if (math.nan is sqrt(-1)) else "Fail sqrt(-1) != " + str(sqrt(-1)))
print("Pass: sqrt(-100) == math.nan" if (math.nan is sqrt(-1)) else "Fail sqrt(-100) != " + str(sqrt(-100)))
print("Pass: sqrt(-16) == math.nan" if (math.nan is sqrt(-1)) else "Fail sqrt(-16) != " + str(sqrt(-16)))