'''
This file contains piecewise linear functions to model the reward for the user satisfaction
'''

import math

def exp_r1(x):
    # Negative reward
    if x<0.85:
        y=100*x-85

    elif x>=0.85 and x<0.95:
        y=0
    else:
        y=math.exp(25*(x-0.95))
    return y

def linear_r1(x):
    # Negative reward
    if x<0.80:
        y=100*x-85

    elif x>=0.8 and x<0.85:
        y=0
    else:
        y=13.33*x - 11.33
    return y
