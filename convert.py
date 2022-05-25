from lambdalib import *


def from_int(n):
    return zero if n == 0 else succ(from_int(n - 1))

def to_int(n):
    return n(lambda r: r + 1)(0)

def from_bool(b):
    return true if b else false

def to_bool(b):
    return b(True)(False)

def from_list(xs, elt):
    if xs:
        y = elt(xs[0])
        ys = from_list(xs[1:], elt)
        return cons(y)(ys)
    else:
        return nil

def to_list(xs, elt):
    return xs(lambda x: lambda acc: [elt(x), *acc])([])
