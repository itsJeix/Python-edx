def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    num = int(num)
    distance_to_num = num - abs(base**0)
    current_answer = ""
    for x in range(1, num):
        if abs(num - base**x) < distance_to_num:            
            current_answer = x
            distance_to_num = abs(num - base**x)
    if current_answer:
        return current_answer
    return 0
    




