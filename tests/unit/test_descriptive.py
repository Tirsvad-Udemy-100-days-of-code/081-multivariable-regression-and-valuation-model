"""@brief Tests for the descriptive statistics."""

import math

import pandas as pd
import pytest

from boston_valuation import constants
from boston_valuation.domain import descriptive

STATISTIC_ROWS = ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]


def _frame(**columns: list[float]) -> pd.DataFrame:
    """@brief Build a small table from named columns.

    @param columns Values of each column.
    @return The table.
    """
    return pd.DataFrame(columns)


def test_descriptive_statistics_has_eight_statistic_rows(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The summary has count, mean, std, min, quartiles and max."""
    assert list(descriptive.descriptive_statistics(boston_data).index) == (
        STATISTIC_ROWS
    )


def test_descriptive_statistics_has_every_column(boston_data: pd.DataFrame) -> None:
    """@brief All fourteen columns are summarised."""
    summary = descriptive.descriptive_statistics(boston_data)
    assert tuple(summary.columns) == constants.ALL_COLUMNS


def test_descriptive_statistics_counts_every_row(boston_data: pd.DataFrame) -> None:
    """@brief Every column has 506 values."""
    summary = descriptive.descriptive_statistics(boston_data)
    assert (summary.loc["count"] == constants.EXPECTED_ROWS).all()


def test_average_students_per_teacher_of_real_data(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The mean pupil-teacher ratio is about 18.46."""
    result = descriptive.average_students_per_teacher(boston_data)
    assert result == pytest.approx(18.46, abs=0.005)


def test_average_students_per_teacher_of_small_frame() -> None:
    """@brief The mean is taken over the PTRATIO column."""
    data = _frame(PTRATIO=[10.0, 20.0])
    assert descriptive.average_students_per_teacher(data) == pytest.approx(15.0)


def test_average_price_is_in_thousands(boston_data: pd.DataFrame) -> None:
    """@brief The mean price is about 22.53 thousand dollars."""
    assert descriptive.average_price(boston_data) == pytest.approx(22.53, abs=0.005)


def test_average_price_in_dollars_of_real_data(boston_data: pd.DataFrame) -> None:
    """@brief The mean price is about 22,533 dollars."""
    result = descriptive.average_price_in_dollars(boston_data)
    assert result == pytest.approx(22_533, abs=0.5)


def test_average_price_in_dollars_is_thousand_times_price() -> None:
    """@brief Dollars are the price in thousands times 1000."""
    data = _frame(PRICE=[10.0, 20.0])
    assert descriptive.average_price_in_dollars(data) == pytest.approx(15_000.0)


def test_average_price_is_nan_for_empty_column() -> None:
    """@brief A table without rows has no average."""
    data = _frame(PRICE=[])
    assert math.isnan(descriptive.average_price(data))


def test_river_value_range_of_real_data(boston_data: pd.DataFrame) -> None:
    """@brief CHAS is a dummy variable that runs from 0 to 1."""
    assert descriptive.river_value_range(boston_data) == (0.0, 1.0)


def test_river_counts_of_real_data(boston_data: pd.DataFrame) -> None:
    """@brief 471 tracts are away from the river and 35 are next to it."""
    counts = descriptive.river_counts(boston_data)
    assert counts.to_dict() == {0: 471, 1: 35}


def test_river_counts_are_ordered_not_next_then_next() -> None:
    """@brief The order is 0 then 1 whatever the order in the data."""
    data = _frame(CHAS=[1.0, 1.0, 0.0])
    assert list(descriptive.river_counts(data).index) == [0, 1]


def test_river_counts_gives_zero_for_missing_value() -> None:
    """@brief A table with no river tract counts 0 for the river."""
    data = _frame(CHAS=[0.0, 0.0])
    assert descriptive.river_counts(data).to_dict() == {0: 2, 1: 0}


def test_room_range_of_real_data(boston_data: pd.DataFrame) -> None:
    """@brief The average rooms run from about 3.56 to 8.78."""
    low, high = descriptive.room_range(boston_data)
    assert (low, high) == (pytest.approx(3.561), pytest.approx(8.78))


def test_room_range_of_small_frame() -> None:
    """@brief The range is the minimum and the maximum of RM."""
    assert descriptive.room_range(_frame(RM=[5.0, 7.0, 6.0])) == (5.0, 7.0)
