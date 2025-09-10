"""
While and If
Learning to use if and while is an essential skill. During this discussion, focus on what we've studied in the first three lectures: if, while, assignment (=), comparison (<, >, ==, ...), and arithmetic. Please don't use features of Python that we haven't discussed in class yet, such as for, range, and lists. We'll have plenty of time for those later in the course, but now is the time to practice the use of if (textbook section 1.5.4) and while (textbook section 1.5.5).
"""

def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes

# race(3, 5), race(4, 5), race(2, 3)

def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    for i in range(n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("fizz")
        elif i % 3 !=0 and i % 5 == 0:
            print("buzz")
        else:
            print(i)

"""
Problem Solving
A useful approach to implementing a function is to:

Pick an example input and corresponding output.
Describe a process (in English) that computes the output from the input using simple steps.
Figure out what additional names you'll need to carry out this process.
Implement the process in code using those additional names.
Determine whether the implementation really works on your original example.
Determine whether the implementation really works on other examples. (If not, you might need to revise step 2.)
Importantly, this approach doesn't go straight from reading a question to writing code.

For example, in the is_prime problem below, you could:

Pick n is 9 as the input and False as the output.
Here's a process: Check that 9 (n) is not a multiple of any integers between 1 and 9 (n).
Introduce i to represent each number between 1 and 9 (n).
Implement is_prime (you get to do this part with your group).
Check that is_prime(9) will return False by thinking through the execution of the code.
Check that is_prime(3) will return True and is_prime(1) will return False.
Try this approach together on the next two problems.
"""

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    assert n >= 1 and isinstance(n, int)
    i = 2
    if n == 1:
        return False
    
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


###########################


def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    count = 0
    for i in range(10):
        if has_digit(count, i):
            count += 1
    return count

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    while n:
        if n % 10 == k:
            return True
        n = n // 10
    return False


"""
Environment Diagrams

An environment diagram keeps track of names and their values in frames, which are drawn as boxes.
"""