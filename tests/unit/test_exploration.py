"""@brief Tests for the first look at the table."""

import numpy as np
import pandas as pd
import pytest

from boston_valuation import constants
from boston_valuation.domain import exploration


@pytest.fixture
def small() -> pd.DataFrame:
    """@brief Build a clean three-row table.

    @return A table with two columns and no NaN or duplicate.
    """
    return pd.DataFrame({"A": [1.0, 2.0, 3.0], "B": [4.0, 5.0, 6.0]})


def test_table_shape_of_real_data(boston_data: pd.DataFrame) -> None:
    """@brief The real table has 506 rows and 14 columns."""
    assert exploration.table_shape(boston_data) == (506, 14)


def test_row_count_of_real_data(boston_data: pd.DataFrame) -> None:
    """@brief There is one row per census tract."""
    assert exploration.row_count(boston_data) == constants.EXPECTED_ROWS


def test_column_names_of_real_data(boston_data: pd.DataFrame) -> None:
    """@brief The names follow the order of the file."""
    assert tuple(exploration.column_names(boston_data)) == constants.ALL_COLUMNS


def test_table_shape_of_empty_frame() -> None:
    """@brief An empty table has no rows and no columns."""
    assert exploration.table_shape(pd.DataFrame()) == (0, 0)


def test_row_count_of_empty_frame() -> None:
    """@brief An empty table has zero rows."""
    assert exploration.row_count(pd.DataFrame()) == 0


def test_has_nan_values_false_for_real_data(boston_data: pd.DataFrame) -> None:
    """@brief The real table has no missing value."""
    assert exploration.has_nan_values(boston_data) is False


def test_has_nan_values_true_when_cell_is_missing(small: pd.DataFrame) -> None:
    """@brief One missing cell is enough."""
    small.loc[1, "A"] = np.nan
    assert exploration.has_nan_values(small) is True


def test_has_nan_values_false_for_empty_frame() -> None:
    """@brief An empty table has nothing missing."""
    assert exploration.has_nan_values(pd.DataFrame()) is False


def test_count_nan_values_is_zero_for_every_real_column(
    boston_data: pd.DataFrame,
) -> None:
    """@brief No column of the real table has a missing value."""
    counts = exploration.count_nan_values(boston_data)
    assert counts.sum() == 0
    assert len(counts) == constants.EXPECTED_COLUMNS


def test_count_nan_values_counts_per_column(small: pd.DataFrame) -> None:
    """@brief The count is given per column."""
    small.loc[[0, 1], "A"] = np.nan
    counts = exploration.count_nan_values(small)
    assert counts.to_dict() == {"A": 2, "B": 0}


def test_has_duplicates_false_for_real_data(boston_data: pd.DataFrame) -> None:
    """@brief The real table has no repeated row."""
    assert exploration.has_duplicates(boston_data) is False


def test_has_duplicates_true_when_row_repeats(small: pd.DataFrame) -> None:
    """@brief A repeated row is detected."""
    repeated = pd.concat([small, small.iloc[[0]]], ignore_index=True)
    assert exploration.has_duplicates(repeated) is True


def test_count_duplicates_is_zero_for_real_data(boston_data: pd.DataFrame) -> None:
    """@brief The real table has zero duplicated rows."""
    assert exploration.count_duplicates(boston_data) == 0


def test_count_duplicates_does_not_count_first_copy(small: pd.DataFrame) -> None:
    """@brief A row that appears three times is two duplicates."""
    tripled = pd.concat([small, small.iloc[[0]], small.iloc[[0]]], ignore_index=True)
    assert exploration.count_duplicates(tripled) == 2


def test_has_duplicates_false_for_empty_frame() -> None:
    """@brief An empty table has no duplicate."""
    assert exploration.has_duplicates(pd.DataFrame()) is False


def test_first_rows_defaults_to_preview_size(boston_data: pd.DataFrame) -> None:
    """@brief The default is the number of rows named in the constants."""
    assert len(exploration.first_rows(boston_data)) == constants.PREVIEW_ROWS


def test_first_rows_starts_at_first_row(boston_data: pd.DataFrame) -> None:
    """@brief The preview begins with the first row of the file."""
    preview = exploration.first_rows(boston_data)
    assert preview.index[0] == boston_data.index[0]


def test_last_rows_defaults_to_preview_size(boston_data: pd.DataFrame) -> None:
    """@brief The default is the number of rows named in the constants."""
    assert len(exploration.last_rows(boston_data)) == constants.PREVIEW_ROWS


def test_last_rows_ends_at_last_row(boston_data: pd.DataFrame) -> None:
    """@brief The preview ends with the last row of the file."""
    preview = exploration.last_rows(boston_data)
    assert preview.index[-1] == boston_data.index[-1]


def test_first_rows_takes_all_when_table_is_shorter(small: pd.DataFrame) -> None:
    """@brief Asking for more rows than exist returns every row."""
    assert len(exploration.first_rows(small, 10)) == len(small)


def test_last_rows_honours_given_count(small: pd.DataFrame) -> None:
    """@brief The caller can choose how many rows to see."""
    assert len(exploration.last_rows(small, 2)) == 2
