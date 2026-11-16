"""@brief First look at the table: its size, its columns and its quality."""

import pandas as pd

from boston_valuation import constants


def table_shape(data: pd.DataFrame) -> tuple[int, int]:
    """@brief Give the number of rows and columns.

    @param data The house price table.
    @return A pair of row count and column count.
    """
    rows, columns = data.shape
    return rows, columns


def row_count(data: pd.DataFrame) -> int:
    """@brief Count the rows.

    @param data The house price table.
    @return The number of rows.
    """
    return len(data)


def column_names(data: pd.DataFrame) -> list[str]:
    """@brief List the column names in file order.

    @param data The house price table.
    @return The column names.
    """
    return [str(name) for name in data.columns]


def count_nan_values(data: pd.DataFrame) -> pd.Series:
    """@brief Count the missing values of every column.

    @param data The house price table.
    @return The number of NaN values, indexed by column name.
    """
    return data.isna().sum()


def has_nan_values(data: pd.DataFrame) -> bool:
    """@brief Tell whether any cell is missing.

    @param data The house price table.
    @return True when at least one value is NaN.
    """
    return bool(data.isna().to_numpy().any())


def count_duplicates(data: pd.DataFrame) -> int:
    """@brief Count the rows that repeat an earlier row.

    @param data The house price table.
    @return The number of duplicated rows; the first copy is not counted.
    """
    return int(data.duplicated().sum())


def has_duplicates(data: pd.DataFrame) -> bool:
    """@brief Tell whether any row repeats an earlier row.

    @param data The house price table.
    @return True when at least one row is a duplicate.
    """
    return count_duplicates(data) > 0


def first_rows(data: pd.DataFrame, count: int = constants.PREVIEW_ROWS) -> pd.DataFrame:
    """@brief Take the first rows of the table.

    @param data The house price table.
    @param count How many rows to take.
    @return The first rows, in file order.
    """
    return data.head(count)


def last_rows(data: pd.DataFrame, count: int = constants.PREVIEW_ROWS) -> pd.DataFrame:
    """@brief Take the last rows of the table.

    @param data The house price table.
    @param count How many rows to take.
    @return The last rows, in file order.
    """
    return data.tail(count)
