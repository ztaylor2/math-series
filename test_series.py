import pytest

FIB_TABLE = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8)]

LUC_TABLE = [(0, 2), (1, 1), (2, 3), (3, 4), (4, 7), (5, 11), (6, 18)]


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fibonacci(n, result):
    """testing our fibonacci() funciton"""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', LUC_TABLE)
def test_lucas(n, result):
    """testing our lucas function"""
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_sum_series_default(n, result):
    """testing our sum_series funciton default"""
    from series import sum_series
    assert sum_series(n) == result


@pytest.mark.parametrize('n, result', LUC_TABLE)
def test_sum_serie_lucas(n, result):
    """testing our sum_series funciton default"""
    from series import sum_series
    assert sum_series(n, 2, 1) == result
