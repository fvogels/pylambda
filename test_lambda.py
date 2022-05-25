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
