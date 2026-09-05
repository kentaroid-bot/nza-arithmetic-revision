import math

import pytest

from nza import NZA


def test_init():
    n = NZA(5)
    assert n.local == 5.0
    assert math.isinf(n.universe)


def test_conservation():
    """Thm4: total always ∞"""
    assert NZA(0).total() == math.inf
    assert NZA(-999).total() == math.inf
    assert (NZA(5) - NZA(5)).total() == math.inf  # No annihilation (Thm5)


def test_add():
    assert (NZA(2) + NZA(3)).local == 5.0
    assert (NZA(1) + 2).local == 3.0


def test_sub():
    assert (NZA(5) - NZA(3)).local == 2.0
    assert (NZA(3) - NZA(5)).local == -2.0
    assert (5 - NZA(2)).local == 3.0


def test_mul():
    assert (NZA(2) * NZA(3)).local == 6.0
    assert (2 * NZA(3)).local == 6.0


def test_div():
    assert (NZA(6) / NZA(2)).local == 3.0
    assert (NZA(1) / 2).local == 0.5


def test_div_zero():
    result = NZA(1) / NZA(0)
    assert math.isinf(result.local) and result.local > 0
    assert str(result) == "∞_universe"


def test_floordiv():
    assert (NZA(6) // NZA(2)).local == 3.0
    inf_div = NZA(1) // NZA(0)
    assert math.isinf(inf_div.local)


def test_pow():
    assert (NZA(2) ** NZA(3)).local == 8.0
    assert (NZA(2) ** 3).local == 8.0


def test_unary():
    assert (-NZA(5)).local == -5.0
    assert abs(NZA(-5)).local == 5.0


def test_repr():
    assert "0.0_local + ∞_universe" in str(NZA(0))
    assert "∞_universe" == str(NZA(1) / NZA(0))
    assert "-3.0_local + ∞_universe" in str(NZA(-3))


def test_comparisons():
    a, b = NZA(1), NZA(2)
    assert a < b
    assert a == NZA(1)
    assert a != NZA(2)
    assert a <= b
    assert b >= a
