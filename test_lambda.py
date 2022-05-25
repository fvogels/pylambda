from lambdalib import *
from convert import *
import pytest


def test_true():
    assert true("a")("b") == "a"

def test_false():
    assert false("a")("b") == "b"

@pytest.mark.parametrize("a", [True, False])
@pytest.mark.parametrize("b", [True, False])
def test_conj(a, b):
    assert to_bool(conj(from_bool(a))(from_bool(b))) == (a and b)


@pytest.mark.parametrize("a", [True, False])
@pytest.mark.parametrize("b", [True, False])
def test_disj(a, b):
    assert to_bool(disj(from_bool(a))(from_bool(b))) == (a or b)


@pytest.mark.parametrize("a", [True, False])
def test_neg(a):
    assert to_bool(neg(from_bool(a))) == (not a)


def test_iszero_zero():
    assert to_bool(is_zero(zero)) == True


def test_iszero_szero():
    assert to_bool(is_zero(succ(zero))) == False


@pytest.mark.parametrize("a", range(0, 10))
@pytest.mark.parametrize("b", range(0, 10))
def test_add(a, b):
    x = from_int(a)
    y = from_int(b)
    z = add(x)(y)
    assert to_int(z) == a + b


@pytest.mark.parametrize("a", range(0, 10))
@pytest.mark.parametrize("b", range(0, 10))
def test_sub(a, b):
    x = from_int(a)
    y = from_int(b)
    z = sub(x)(y)
    assert to_int(z) == max(a - b, 0)


@pytest.mark.parametrize("a", range(0, 10))
@pytest.mark.parametrize("b", range(0, 10))
def test_mul(a, b):
    x = from_int(a)
    y = from_int(b)
    z = mul(x)(y)
    assert to_int(z) == a * b


@pytest.mark.parametrize("a", range(0, 10))
@pytest.mark.parametrize("b", range(1, 10))
def test_mod(a, b):
    x = from_int(a)
    y = from_int(b)
    z = mod(x)(y)
    assert to_int(z) == a % b
