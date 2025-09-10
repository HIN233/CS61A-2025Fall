# Assignment

def ex1():
    """
    >>> max(2, 10)
    10
    >>> pow(2, 10)
    1024
    >>> f(2, 10)
    Error
    >>> f = pow
    >>> f(2, 10)
    1024
    >>> f
    Function: pow
    >>> pow
    Function: pow
    >>> # Two names for the same thing

    >>> # Test your understsanding
    >>> pow(2, 10)
    1024
    >>> max = pow
    >>> pow(2, 10) #?
    1024
    
    >>> pow = max
    >>> pow(2, 10) #?
    1024

    >>> max
    Function: pow

    >>> CTRL+D
    >>> pow
    Function: pow
    >>> max
    Function: max
    >>> max = pow
    >>> max
    Function: pow
    >>> pow
    Function: pow
    >>> max = pow
    >>> pow = max
    >>> pow
    Function: pow
    >>> max
    Function: pow

    >>> # Video example
    >>> CTRL+D
    >>> max
    Function: max
    >>> min
    Function: min
    >>> h = max
    >>> h
    Function: max
    >>> max = min
    >>> max
    Function: min
    >>> h
    Function max
    >>> h(2, 10)
    10
    >>> max(2, 10)
    2

    >>> # Common use-case
    >>> original_print = print
    >>> print = max
    >>> print(2, 3)
    >>> original_print
    Function: print
    >>> original_print(2, 3)
    2 3

    >>> # Calling functions you've defined yourself
    >>> CTRL+D
    >>> def f(x):
    ...     return x + 1
    ...
    >>> f(3)
    4
    >>> # REPEAT ABOVE IN FILE AND START IN INTERACTIVE MODE - VIM + VS CODE
    """

def ex2():
    """
    >>> # DEFINE IN A FILE:
    >>> def g(y):
    ...     x = 2 * y
    ...     return x + 1
    ...
    >>> x
    NameError
    >>> g

    Function: g
    >>> x = 2
    >>> g(x)
    5
    >>> x
    2
    >>> y
    NameError

    >>> # CLEAR
    >>> x = 2
    >>> g(3 * x) + 3 #?
    16
    >>> x
    2
    >>> y = 3
    >>> g(y)
    7
    >>> y
    3
    >>> # TO PYTHON TUTOR
    """

# https://pythontutor.com/cp/composingprograms.html#code=def%20g%28y%29%3A%0A%20%20%20%20x%20%3D%202%20*%20y%0A%20%20%20%20return%20x%20%2B%201%0A%20%20%20%20%0Ax%20%3D%202%0Aprint%28g%28x%29%29%0Aprint%28g%283%20*%20x%29%20%2B%203%29%0A&cumulative=true&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D
# SLIGHT MODIFICATION: https://pythontutor.com/cp/composingprograms.html#code=x%20%3D%202%0A%0Adef%20g%28y%29%3A%0A%20%20%20%20return%20x%20%2B%201%0A%20%20%20%20%0Aprint%28g%28x%29%29%0Aprint%28g%283%20*%20x%29%20%2B%203%29&cumulative=true&mode=edit&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D

# Name conflicts

from operator import mul

def square(square):
    return mul(square, square)
square(3) #?

# https://pythontutor.com/cp/composingprograms.html#code=from%20operator%20import%20mul%0Adef%20square%28square%29%3A%0A%20%20%20%20return%20mul%28square,%20square%29%0Aprint%28square%283%29%29&cumulative=true&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D
# SLIGHT MODIFICATION: https://pythontutor.com/cp/composingprograms.html#code=from%20operator%20import%20mul%0Adef%20square%28square%29%3A%0A%20%20%20%20return%20mul%28square,%20square%29%0Aprint%28square%28square%283%29%29%29&cumulative=true&mode=edit&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D

# Multiple Assignment

def diff(x, y):
    """
    >>> def diff(x, y):
    ...     x, y = y, x
    ...     return y - x
    
    >>> x, y = 6, 1
    >>> x, y = y, x-y
    >>> diff(y, x)
    4
    """
    x, y = y, x
    return y - x
    
# https://pythontutor.com/cp/composingprograms.html#code=def%20diff%28x,%20y%29%3A%0A%20%20%20%20x,%20y%20%3D%20y,%20x%0A%20%20%20%20return%20y%20-%20x%0A%20%20%20%20%0Ax,%20y%20%3D%206,%201%0Ax,%20y%20%3D%20y,%20x-y%0Aprint%28diff%28y,%20x%29%29&cumulative=true&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D

# Print and None
def print_ex():
    """
    >>> # IN A FILE, RUN WITH `python3 ex.py`:
    >>> def triple(x):
    ...     return x * 3
    ...
    triple(3)
    print(triple(3))
    >>> # IN INTERACTIVE MODE
    >>> triple(3)
    9
    >>> triple(3) + 1
    10
    >>> def triple(x):
    ...     print(x * 3)
    ...
    >>> triple(3)
    9
    >>> triple(6)
    18
    >>> triple(3) + 1
    9
    Error
    >>> def triple(x):
    ...     return print(x * 3)
    ...
    >>> triple(3) + 1
    9
    Error 

    >>> print(3)
    3
    >>> 3
    3
    >>> x = 3
    >>> x
    3
    >>> x = print(3)
    3
    >>> x
    >>> x
    >>> print(x)
    None

    >>> def triple(x):
    ...     print(x * 4)
    ...     return x * 3
    ...
    >>> triple(3) + 1 #?
    12
    10
    >>> triple(triple(3)) #?
    12
    36
    27
    """

def noisy(x):
    """
    >>> noisy(5)
    NOISY 5
    6
    >>> noise(5) + 1
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

# Smalls

def f(x):
    return x - 1
def g(x):
    return 2 * (x + 1)
def h(x, y):
    return int(str(x) + str(y))

class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def calls(self):
        return 0

class Call:
    """A call expression."""
    def __init__(self, f, operands):
        self.f = f
        self.operands = operands
        self.value = f(*[e.value for e in operands])

    def __repr__(self):
        return f'{self.f.__name__}({",".join(map(str, self.operands))})'

    def calls(self):
        return 1 + sum(o.calls() for o in self.operands)

def smalls(n):
    if n == 0:
        yield Number(5)
    else:
        for operand in smalls(n-1):
            yield Call(f, [operand])
            yield Call(g, [operand])
        for k in range(n):
            for first in smalls(k):
                for second in smalls(n-k-1):
                    if first.value > 0 and second.value > 0:
                        yield Call(h, [first, second])

def show_all(i=3):
    for e in smalls(i):
        print(e, '->', e.value)

def sol():
    for i in range(9):
        r = [e for e in smalls(i) if e.value == 2025]
        for e in r:
            print(e, '->', e.value, 'has', e.calls(), 'calls')
