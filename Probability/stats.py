import numpy as np
import math

def multiplication(n1,n2):
    '''
    Multiplication rule
    n1 is number of posibilities of event 1
    n2 is number of posibilities of event 2
    '''
    return n1*n2 

def permutations(n,k):
    '''
    Permutation rule
    Number of permutations k taken from a set of n elements
    Distinct multiplication rule
    
    (n)
    | | = n!/((n-k)!)
    (k)
    '''
    return math.factorial(n)/math.factorial(n-k)

def combinations(n,k):
    '''
    Combinations are without replacement
    (n)
    | | = n!/(k!(n-k)!)
    (k)
    '''
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))