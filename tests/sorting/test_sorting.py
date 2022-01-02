from src.sorting import sort_by
import pytest

# Mocks
JOBS = [
    {
        "max_salary": 4000,
        "min_salary": 2000,
        "date_posted": "2021-10-23",
    },
    {
        "max_salary": 8000,
        "min_salary": 4000,
        "date_posted": "2021-09-18",
    },
    {
        "max_salary": 5000,
        "min_salary": 2500,
        "date_posted": "2021-09-22",
    },
    {
        "max_salary": 2000,
        "min_salary": 1000,
        "date_posted": "2021-06-19",
    },
]


def elementByMax(e):
    return e["max_salary"]


JOBS_BY_MAX_SALARY = sorted(JOBS, key=elementByMax, reverse=True)


def elementByMin(e):
    return e["min_salary"]


JOBS_BY_MIN_SALARY = sorted(JOBS, key=elementByMin)


def elementByDte(e):
    return e["date_posted"]


JOBS_BY_DATE = sorted(JOBS, reverse=True, key=elementByDte)

# Tests


def test_sort_by_criteria():
    sort_by(JOBS, "max_salary")
    assert JOBS == JOBS_BY_MAX_SALARY

    sort_by(JOBS, "min_salary")
    assert JOBS == JOBS_BY_MIN_SALARY

    sort_by(JOBS, "date_posted")
    assert JOBS == JOBS_BY_DATE

    criteria = "invalid_string"
    with pytest.raises(
        ValueError, match=f"error: {criteria}"
    ):
        sort_by(JOBS, criteria)
