# Print and None (continued)

"""
>>> print(None, print(1, 2)) #? - from Fall 2018 Midterm 1
1 2
None None
"""

def noisy(x):
    """
    >>> noisy(5)
    NOISY 5
    6
    >>> noisy(5) + 1
    NOISY 5
    7
    >>> noisy(noisy(2) + noisy(3)) #?
    NOISY 2
    NOISY 3
    NOISY 7
    8
    """
    print('NOISY', x)
    return x + 1

# H example
def h2(x):
    print(f(x))
    return f(x)

def h3(x):
    y = f(x)
    print(y)
    return y

def f(z):
    # print('HOWDY')
    return z + 2
"""
>>> h2(2)
4
4
>>> h3(2)
4
4
>>> CTRL+D, add print call
>>> h2(2)
HOWDY
4
HOWDY
4
>>> h3(2)
HOWDY
4
4
>>> # why? explain it to your neighbor
>>> # environment diagram difference: 2 local frames vs 1
>>> # https://pythontutor.com/cp/composingprograms.html#code=def%20h2%28x%29%3A%0A%20%20%20%20print%28f%28x%29%29%0A%20%20%20%20return%20f%28x%29%0A%0Adef%20h3%28x%29%3A%0A%20%20%20%20y%20%3D%20f%28x%29%0A%20%20%20%20print%28y%29%0A%20%20%20%20return%20y%0A%0Adef%20f%28z%29%3A%0A%20%20%20%20print%28%22HOWDY%22%29%0A%20%20%20%20return%20z%20%2B%202%0A%0Ax%20%3D%20h2%282%29%0A%23%20x%20%3D%20h3%282%29&cumulative=true&mode=edit&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D 

>>> # now, let's change f
>>> f = print
>>> h2(2) #?
2
None
2
>>> h3(2) #?
2
None
"""

# Conditionals slide

# Running a file in non-interactive mode
def triple(x):
    return x * 3
triple(3)
print(triple(3))

# Return ends a function call
def triple(x):
    print(x * 4)
    return x * 3
"""
>>> triple(3) + 1
12
10
"""

def triple(x):
    return x * 3
    print(x * 4)
"""
triple(3) + 1
10
"""

def triple(x):
    if x == 4:
        return 13
    return x * 3
"""
>>> triple(5)
15
>>> triple(4)
13
"""

# While loops slide

# Prime factorization
"""
>>> # how to check for divisibility?
>>> n = 12
>>> d = 5
>>> n / d
2.4
>>> d = 4
>>> n / d
3.0
>>> n // d
3
>>> n % d
0
>>> d = 5
>>> n % d
2
"""


def prime_factors(n):
    """Print the prime factors of positive integer n
       in non-decreasing order.

    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(11)
    11
    >>> prime_factors(12)
    2
    2
    3
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallest_factor(n)
        print(k)
        n = n // k

def smallest_factor(n):
    """Return the smallest factor of n greater than 1.
    
    >>> smallest_factor(8)
    2
    >>> smallest_factor(4)
    2
    >>> smallest_factor(2)
    2
    >>> smallest_factor(13)
    13
    """
    k = 2
    while n % k != 0:
        k = k + 1
    return k

# Max Digit

def max_digit(n):
    """Given a positive integer N, return its max digit.
    
    >>> max_digit(12345)
    5
    >>> max_digit(816)
    8
    >>> max_digit(0)
    0
    """
    # Repeat this in a loop until there are no digits left:
    #   Look at the last digit
    #   If it's larger than our biggest digit so far, update our biggest digit so far
    #   Remove the last digit
    # Return the biggest digit we've seen so far
 
    best_digit = 0
    while n != 0:
        last_digit = n % 10
        if last_digit > best_digit:
            best_digit = last_digit
        n = n // 10
    return best_digit
