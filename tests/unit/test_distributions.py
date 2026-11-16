"""@brief Tests for the averages and counts behind the distribution charts."""

import pandas as pd
import pytest

from boston_valuation import constants
from boston_valuation.domain import distributions

RIVER_NO_COUNT = 471
RIVER_YES_COUNT = 35


@pytest.fixture
def empty_table() -> pd.DataFrame:
    """@brief Build a table with the right columns and no rows.

    @return An empty frame with every column of the data.
    """
    return pd.DataFrame(columns=list(constants.ALL_COLUMNS), dtype=float)


def test_average_distance_is_3_80(boston_data: pd.DataFrame) -> None:
    """@brief The mean of DIS rounds to 3.80."""
    assert round(distributions.average_distance(boston_data), 2) == 3.80


def test_average_rooms_is_6_28(boston_data: pd.DataFrame) -> None:
    """@brief The mean of RM rounds to 6.28."""
    assert round(distributions.average_rooms(boston_data), 2) == 6.28


def test_price_title_carries_average_price(boston_data: pd.DataFrame) -> None:
    """@brief The price title shows the mean of PRICE as 22.53."""
    assert "Average: 22.53" in distributions.price_title(boston_data)


def test_distance_title_carries_average_distance(boston_data: pd.DataFrame) -> None:
    """@brief The distance title shows the mean of DIS as 3.80."""
    assert distributions.distance_title(boston_data).endswith("Average: 3.80")


def test_rooms_title_carries_average_rooms(boston_data: pd.DataFrame) -> None:
    """@brief The rooms title shows the mean of RM as 6.28."""
    assert distributions.rooms_title(boston_data).endswith("Average: 6.28")


def test_river_counts_by_label_uses_no_and_yes(boston_data: pd.DataFrame) -> None:
    """@brief The index is the labels No and Yes, in that order."""
    counts = distributions.river_counts_by_label(boston_data)
    assert list(counts.index) == ["No", "Yes"]


def test_river_counts_by_label_counts_471_and_35(boston_data: pd.DataFrame) -> None:
    """@brief 471 tracts are away from the river and 35 are next to it."""
    counts = distributions.river_counts_by_label(boston_data)
    assert counts.to_dict() == {"No": RIVER_NO_COUNT, "Yes": RIVER_YES_COUNT}


def test_river_counts_by_label_sum_to_row_count(boston_data: pd.DataFrame) -> None:
    """@brief Every tract is counted once."""
    counts = distributions.river_counts_by_label(boston_data)
    assert int(counts.sum()) == len(boston_data)


def test_river_counts_by_label_counts_missing_value_as_zero() -> None:
    """@brief A table with no river tract has 0 under Yes."""
    table = pd.DataFrame({constants.COL_CHAS: [0, 0, 0]})
    counts = distributions.river_counts_by_label(table)
    assert counts.to_dict() == {"No": 3, "Yes": 0}


def test_river_counts_by_label_of_empty_table_is_zero(
    empty_table: pd.DataFrame,
) -> None:
    """@brief An empty table gives 0 for both labels."""
    counts = distributions.river_counts_by_label(empty_table)
    assert counts.to_dict() == {"No": 0, "Yes": 0}


def test_highway_access_counts_sum_to_row_count(boston_data: pd.DataFrame) -> None:
    """@brief Every tract falls under one RAD value."""
    counts = distributions.highway_access_counts(boston_data)
    assert int(counts.sum()) == len(boston_data)


def test_highway_access_counts_index_is_ascending(boston_data: pd.DataFrame) -> None:
    """@brief The RAD values are listed from smallest to largest."""
    counts = distributions.highway_access_counts(boston_data)
    assert counts.index.is_monotonic_increasing


def test_highway_access_counts_has_nine_values(boston_data: pd.DataFrame) -> None:
    """@brief RAD takes the values 1 to 8 and 24."""
    counts = distributions.highway_access_counts(boston_data)
    assert list(counts.index) == [1, 2, 3, 4, 5, 6, 7, 8, 24]


def test_averages_of_empty_table_are_nan(empty_table: pd.DataFrame) -> None:
    """@brief An empty table has no average, as pandas defines it."""
    assert pd.isna(distributions.average_distance(empty_table))
    assert pd.isna(distributions.average_rooms(empty_table))


def test_title_of_empty_table_shows_nan(empty_table: pd.DataFrame) -> None:
    """@brief An empty table gives a title with nan and does not fail."""
    assert distributions.rooms_title(empty_table).endswith("Average: nan")


def test_highway_access_counts_of_empty_table_is_empty(
    empty_table: pd.DataFrame,
) -> None:
    """@brief An empty table has no RAD value to count."""
    assert distributions.highway_access_counts(empty_table).empty
