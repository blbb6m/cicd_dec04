import sys
from pathlib import Path
import math
import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import (
    add,
    sub,
    multiply,
    divide,
    square,
    sqrt,
    log,
    sin,
    cos,
    percentage,
)


def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_sub():
    assert sub(11, 6) == 5

def test_multiply():
    assert multiply(6, 7) == 42
    assert multiply(-2, 3) == -6
    assert multiply(0, 999) == 0

def test_divide_normal():
    assert divide(8, 2) == 4
    assert math.isclose(divide(1, 3), 1/3, rel_tol=1e-12)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_square():
    assert square(5) == 25
    assert square(-4) == 16
    assert square(0) == 0

def test_sqrt_normal():
    assert sqrt(9) == 3
    assert math.isclose(sqrt(2), math.sqrt(2), rel_tol=1e-12)

def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-1)

def test_log_default_base10():
    assert math.isclose(log(100), 2.0, rel_tol=1e-12)

def test_log_natural_base_none():
    assert math.isclose(log(math.e, base=None), 1.0, rel_tol=1e-12)

def test_log_custom_base():
    assert math.isclose(log(8, base=2), 3.0, rel_tol=1e-12)

def test_log_invalid_x():
    with pytest.raises(ValueError):
        log(0)
    with pytest.raises(ValueError):
        log(-10)

def test_log_invalid_base():
    with pytest.raises(ValueError):
        log(10, base=1)
    with pytest.raises(ValueError):
        log(10, base=0)
    with pytest.raises(ValueError):
        log(10, base=-2)

def test_sin_cos_known_angles():
    assert math.isclose(sin(0), 0.0, abs_tol=1e-12)
    assert math.isclose(cos(0), 1.0, abs_tol=1e-12)
    assert math.isclose(sin(math.pi / 2), 1.0, abs_tol=1e-12)
    assert math.isclose(cos(math.pi), -1.0, abs_tol=1e-12)

def test_percentage_no_total():
    assert math.isclose(percentage(25), 0.25, rel_tol=1e-12)
    assert math.isclose(percentage(0), 0.0, rel_tol=1e-12)

def test_percentage_with_total():
    assert math.isclose(percentage(25, 200), 50.0, rel_tol=1e-12)
    assert math.isclose(percentage(10, 0), 0.0, rel_tol=1e-12)