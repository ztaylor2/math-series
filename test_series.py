"""Tests for series.py."""
import pytest

FIB_TABLE = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8)]

LUC_TABLE = [(0, 2), (1, 1), (2, 3), (3, 4), (4, 7), (5, 11), (6, 18)]


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fibonacci(n, result):
    """Testing our fibonacci() funciton."""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', LUC_TABLE)
def test_lucas(n, result):
    """Testing our lucas function."""
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_sum_series_default(n, result):
    """Testing our sum_series funciton default values."""
    from series import sum_series
    assert sum_series(n) == result


@pytest.mark.parametrize('n, result', LUC_TABLE)
def test_sum_serie_lucas(n, result):
    """Testing our sum_series funciton, lucas values as optional input."""
    from series import sum_series
    assert sum_series(n, 2, 1) == result
