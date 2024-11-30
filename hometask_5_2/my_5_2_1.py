def my_range(stop: float, start: float = 0.0, step: float = 1.0):
    '''my_range - the function takes as input 3 variables: start, stop and step. Return list of steps(float)'''
    res = []
    while start < stop:
        res.append(start)
        start += step
    return res