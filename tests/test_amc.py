import pytest
from cogs.amc import score


def test_wrong_number_of_problems():
    with pytest.raises(ValueError):
        score(0, 0, 0)


def test_all_correct():
    assert score(25, 0, 0, 15) == (150, 15, 300)


def test_all_skipped():
    assert score(0, 0, 25, 0) == (37.5, 0, 37.5)
