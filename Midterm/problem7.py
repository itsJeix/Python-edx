def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    common_dict = {}
    uncommon_dict = {}
    for key in d1:
        if key in d2:
            common_dict[key] = f(d1[key], d2[key])
        else:
            uncommon_dict[key] = d1[key]
    for key in d2:
        if key not in common_dict:
            uncommon_dict[key] = d2[key]       
    return (common_dict, uncommon_dict)



