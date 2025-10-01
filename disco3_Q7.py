def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n:
            return who
        elif has_seven(i+1) == True or (i+1) % 7 == 0:
            next = (who + direction) % k
            if next < 1:
                next += k
            # print(f"Player {who} says {i}")
            return f(i + 1, next, -1 * direction)
        else:
            next = (who + direction) % k
            if next < 1:
                next += k
            # print(f"Player {who} says {i}")
            return f(i + 1, next, direction)
    return f(1, 1, 1)

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)
