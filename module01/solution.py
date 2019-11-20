def f_c(X):
    '''
    f_c (x)

    Keyword arguments:
    X -- an argument

    Returns: constant 4
    '''

    return 4

def f_x(x, a, b):
    '''
    f_x(x,a,b)

    Keyword arguments:
    x, a, b -- numbers

    Returns: a * x + b
    '''

    return a * x + b

def sum(x):
    s = 0
    for i in range (1,4):
        s += f_x(x, i, i)
    return s
