true  = lambda t: lambda f: t
false = lambda t: lambda f: f

conj = lambda a: lambda b: lambda t: lambda f: a(b(t)(f))(f)
disj = lambda a: lambda b: lambda t: lambda f: a(t)(b(t)(f))
neg  = lambda a: a(false)(true)

zero = lambda s: lambda z: z    
succ = lambda n: lambda f: lambda x: f(n(f)(x))
pred = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda u: x)(lambda u: u)

is_zero = lambda n: n(lambda _: false)(true)

add = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))
mul = lambda m: lambda n: lambda f: m(n(f))
sub = lambda m: lambda n: n(pred)(m)
mod = lambda m: lambda n: lt(m)(n)(m)(lambda f: (mod(sub(m)(n))(n))(f))

le = lambda m: lambda n: is_zero(sub(m)(n))
lt = lambda m: lambda n: le(succ(m))(n)
ge = lambda m: lambda n: neg(lt(m)(n))
gt = lambda m: lambda n: neg(le(m)(n))
eq = lambda m: lambda n: conj(le(m)(n))(ge(m)(n))

divisible = lambda m: lambda n: is_zero(mod(m)(n))

nil  = lambda f: lambda e: e
cons = lambda x: lambda xs: lambda f: lambda e: f(x)(xs(f)(e))
is_empty = lambda xs: xs(lambda x: lambda acc: false)(true)

iota = lambda a: lambda b: lt(a)(b)(lambda x: (cons(a)(iota(succ(a))(b)))(x))(nil)

forall = lambda f: lambda xs: xs(lambda x: lambda acc: conj(f(x))(acc))(true)
filter = lambda f: lambda xs: xs(lambda x: lambda acc: f(x)(cons(x)(acc))(acc))(nil)

is_prime = lambda n: conj(ge(n)(two))(forall(lambda k: neg(divisible(n)(k)))(iota(two)(n)))
primes = lambda n: filter(is_prime)(iota(two)(n))

one = succ(zero)
two = succ(one)
three = succ(two)
four = succ(three)
five = succ(four)




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

for a in range(0, 10):
    for b in range(0, 10):
        expected = a <= b
        actual = to_bool(le(from_int(a))(from_int(b)))
        assert expected == actual

for a in range(0, 10):
    for b in range(0, 10):
        expected = a < b
        actual = to_bool(lt(from_int(a))(from_int(b)))
        assert expected == actual, f"{a} < {b} failed"

for a in range(0, 10):
    for b in range(0, 10):
        expected = a > b
        actual = to_bool(gt(from_int(a))(from_int(b)))
        assert expected == actual, f"{a} < {b} failed"

for a in range(0, 10):
    for b in range(0, 10):
        expected = a >= b
        actual = to_bool(ge(from_int(a))(from_int(b)))
        assert expected == actual, f"{a} < {b} failed"

for a in range(0, 10):
    for b in range(1, 10):
        print(f"Testing {a} % {b}")
        expected = a % b
        actual = to_int(mod(from_int(a))(from_int(b)))
        assert expected == actual, f"{a} % {b} failed"

assert to_bool(is_empty(nil))
assert to_bool(neg(is_empty(cons(one)(nil))))

assert to_list(nil, to_int) == []
assert to_list(cons(one)(nil), to_int) == [1]

for a in range(0, 10):
    for b in range(0, 10):
        print(f"from_list([{a}, {b}])")
        xs = from_list([a, b], from_int)
        actual = to_list(xs, to_int)
        expected = [a, b]
        assert actual == expected

for a in range(0, 10):
    for b in range(0, 10):
        actual = to_list(iota(from_int(a))(from_int(b)), to_int)
        expected = list(range(a, b))
        assert actual == expected, f"iota({a}, {b}): {actual} != {expected}"

assert to_bool(forall(lt(two))(nil))
assert to_bool(forall(lt(two))(from_list([3], from_int)))
assert to_bool(forall(lt(two))(from_list([3, 4], from_int)))
assert not to_bool(forall(lt(two))(from_list([2, 3, 4], from_int)))
assert to_bool(forall(lt(two))(iota(from_int(3))(from_int(10))))

assert to_bool(conj(true)(true)) == True
assert to_bool(conj(false)(true)) == False
assert to_bool(conj(false)(false)) == False
assert to_bool(conj(true)(false)) == False

for a in [2, 3, 5, 7, 11, 13, 17, 19]:
    assert to_bool(is_prime(from_int(a))), f"is_prime({a})"

for a in [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]:
    assert not to_bool(is_prime(from_int(a))), f"not is_prime({a})"

print(to_list(primes(from_int(20)), to_int))

print("Success!")
