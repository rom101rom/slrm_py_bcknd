'''my_range - the function takes as input 3 variables: start, stop and step.
Realised by generator'''

def my_range(stop: float, start: float = 0.0, step: float = 1.0):
    while start < stop:
        yield start
        start += step

#print(list(my_range(10, 5, 2))) - example of use