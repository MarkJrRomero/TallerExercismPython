from math import sqrt
def score(x, y):
    dist = sqrt(x**2 + y**2)
    return 0 if dist > 10 else 1 if dist > 5 else 5 if dist > 1 else 10
