IS_TRUE = True
IS_FALSE = False

def num_add(a, b):
    """Return (a + b)."""
    return a + b

def num_sub(a, b):
    """Return (a - b)."""
    return a - b

def num_mul(a, b):
    """Return (a * b)."""
    return a * b

def num_div(a, b):
    """Return (a / b)."""
    return a / b

def num_floor(a, b):
    """Return floor (a / b)."""
    return a // b

def num_rem(a, b):
    """Return remainder of (a / b)."""
    return a % b

PANCAKE_INGREDIENTS = {
    'flour' : 2,
    'eggs' : 4,
    'milk' : 200,
    'butter' : False,
    'salt' : 0.001
    }

def ingredient_exists(ingr, dict):
    """Check if an ingredient exists."""
    return ingr in dict.keys()

def fatten_pancakes(dict):
    """Return new recipe with added eggs and butter"""
    newdict = dict.copy()
    newdict['eggs'] = 6
    newdict ['butter'] = True
    return newdict

def add_sugar(dict):
    """Return new recipe with added sugar"""
    newdict = dict.copy()
    newdict['sugar'] = True
    return newdict

def remove_salt(dict):
    """Remove salt from the recipe"""
    newdict = dict.copy()
    if 'salt' in newdict:
        del newdict['salt']
    return newdict

FIBONACCI_NUMBERS = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

def add_fibonacci(lst):
    """Calculate the next Fibonacci number and add it to the returned list"""
    lst.append(lst[-1] + lst[-2])
    return lst

def fib_exists(lst, n):
    """Check if n exists in lst"""
    return n in lst

def which_fib(lst, n):
    """Return the position of n in lst counting from 1"""
    for i in range (0, len(lst)):
        if lst[i] == n:
            return i+1
    raise ValueError

