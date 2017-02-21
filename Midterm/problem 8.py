def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here
    redo = 1
    while redo:
        redo = 0
        for i in L:
            if not g(f(int(i))):
                L.remove(i)
                redo = 1                
    if L:
        return max(x for x in L)
    return -1

