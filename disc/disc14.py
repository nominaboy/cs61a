from disc08 import *

def paths(x, y):
    """Return a list of ways to reach y from x by repeated
    incrementing or doubling.
    >>> paths(3, 5)
    [[3, 4, 5]]
    >>> sorted(paths(3, 6))
    [[3, 4, 5, 6], [3, 6]]
    >>> sorted(paths(3, 9))
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
    >>> paths(3, 3) # No calls is a valid path
    [[3]]
    """
    if x == y:
        return [[x]]
    elif y % 2 == 1 or (y % 2 == 0 and (y // 2) < x):
        return [path + [y] for path in paths(x, y - 1)]
    else:
        a = [path + [y] for path in paths(x, y - 1)]
        b = [path + [y] for path in paths(x, y // 2)]
        return a + b

def merge(s1, s2):
    """ Merges two sorted lists """
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    elif s1[0] < s2[0]:
        return [s1[0]] + merge(s1[1:], s2)
    else:
        return [s2[0]] + merge(s1, s2[1:])

def mergesort(seq):
    cut_point = len(seq) // 2
    first = seq[:cut_point]
    rest = seq[cut_point:len(seq)]
    if len(rest) > 1:
        return merge(mergesort(first), mergesort(rest))
    else:
        return merge(first, rest)

def long_paths(tree, n):
    """Return a list of all paths in tree with length at least n.
    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    <0 1 2>
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 6 9>
    <0 11 12 13 14>
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 11 12 13 14>
    >>> long_paths(whole, 4)
    [Link(0, Link(11, Link(12, Link(13, Link(14)))))]
    """
    paths = []
    if n == 0:
        if tree.is_leaf():
            return [Link(tree.label)]
        else:
            for br in tree.branches:
                for path in long_paths(br, 0):
                    path = Link(tree.label, path) 
                    paths.append(path)
            return paths
    elif n > 0:
        if tree.is_leaf():
            return []
        else:
            for br in tree.branches:
                for path in long_paths(br, n - 1):
                    path = Link(tree.label, path) 
                    paths.append(path)
            return paths



def widest_level(t):
    """
    >>> sum([[1], [2]], [])
    [1, 2]
    >>> t = Tree(3, [Tree(1, [Tree(1), Tree(5)]),
    ...         Tree(4, [Tree(9, [Tree(2)])])])
    >>> widest_level(t)
    [1, 5, 9]
    """
    levels = []
    x = [t]
    while x:
        levels.append([t.label for t in x])
        x = sum([t.branches for t in x], [])
    return max(levels, key=len)


class Emotion:
    num = 0
    def __init__(self):
        Emotion.num += 1
        self.power = 5


    def feeling(self, other):
        if self.power == other.power:
            print("Together")
        elif self.power > other.power:
            self.catchphrase()
            other.catchphrase()
        else:
            other.catchphrase()
            self.catchphrase()


class Joy(Emotion):
    def catchphrase(self):
        print("Think positive thoughts")

class Sadness(Emotion):
    def catchphrase(self):
        print("I'm positive you will get lost")


def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(5))
    """
    if lnk.rest is Link.empty:
        return
    elif lnk.first == lnk.rest.first:
        lnk.rest = lnk.rest.rest
        return remove_duplicates(lnk)
    else:
        remove_duplicates(lnk.rest)




def repeated(f):
    """
    >>> double = lambda x: 2 * x
    >>> funcs = repeated(double)
    >>> identity = next(funcs)
    >>> double = next(funcs)
    >>> quad = next(funcs)
    >>> oct = next(funcs)
    >>> quad(1)
    4
    >>> oct(1)
    8
    >>> [g(1) for _, g in
    ... zip(range(5), repeated(lambda x: 2 * x))]
    [1, 2, 4, 8, 16]
    """
    g = lambda x : x
    while True:
        yield g
        h = g
        g = lambda x : f(h(x))

double = lambda x: 2 * x
funcs = repeated(double)
identity = next(funcs)
double = next(funcs)
quad = next(funcs)
oct = next(funcs)
double(1)
