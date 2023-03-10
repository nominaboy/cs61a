def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    result = 1
    if k == 0:
        return 1
    else:
        while k > 0:
            result = result * n
            n -= 1
            k -= 1
        return result 
    '''
    if k == 0:
        return 1
    else:
        return falling(n, k - 1) * (n - k + 1)
    '''




def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"

    result = 0
    while y > 0:
        result = result + y % 10
        y = y // 10
    return result 

    """ 
    if y == 0:
        return 0
    else:
        return sum_digits(y // 10) + y % 10
    """



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    counter_for_eights = 0
    while n > 0:
        if n % 10 == 8:
            counter_for_eights += 1
        else:
            counter_for_eights = 0
        if counter_for_eights == 2:
            return True
        n = n // 10
    return False

        

        


