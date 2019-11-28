"""solution of tasks"""
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

def ingredient_exists(ingr, diction):
    """Check if an ingredient exists."""
    return ingr in diction.keys()

def fatten_pancakes(diction):
    """Return new recipe with added eggs and butter"""
    newdict = diction.copy()
    newdict['eggs'] = 6
    newdict['butter'] = True
    return newdict

def add_sugar(diction):
    """Return new recipe with added sugar"""
    newdict = diction.copy()
    newdict['sugar'] = True
    return newdict

def remove_salt(diction):
    """Remove salt from the recipe"""
    newdict = diction.copy()
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
    for i, val in enumerate(lst, 1):
        if val == n:
            return i
    raise ValueError
