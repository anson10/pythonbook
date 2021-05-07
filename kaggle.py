def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    index = 0
    new_list = []
    for num1 in L:
        for num2 in thresh:
            x = num1 > num2
            new_list.append(x)
    return new_list
    pass
L = [2,9,5,2]
thresh = [8,0,1,4]
elementwise_greater_than(L, thresh)