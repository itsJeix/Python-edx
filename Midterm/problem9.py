def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList
    '''
    newlist = []
    for element in aList:
        if type(element) is list:
            newlist += (flatten(element))
        else:
            newlist.append(element)
    return newlist

