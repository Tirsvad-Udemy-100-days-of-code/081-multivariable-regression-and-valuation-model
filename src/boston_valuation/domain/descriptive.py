"""@brief Descriptive statistics of the Boston house price table.

@details The columns are the features of a census tract plus the price. The
price is in thousands of dollars. CHAS is a dummy variable: 1 when the tract
bounds the Charles River and 0 when it does not. The statistics of an empty
table are NaN, as pandas defines them.
"""

import pandas as pd

from boston_valuation import constants


def descriptive_statistics(data: pd.DataFrame) -> pd.DataFrame:
    """@brief Summarise every column.

    @param data The house price table.
    @return One row per statistic (count, mean, std, min, 25%, 50%, 75%, max)
        and one column per table column.
    """
    return data.describe()


def average_students_per_teacher(data: pd.DataFrame) -> float:
    """@brief Average the pupil-teacher ratio of the tracts.

    @param data The house price table.
    @return The mean of PTRATIO.
    """
    return float(data[constants.COL_PTRATIO].mean())


def average_price(data: pd.DataFrame) -> float:
    """@brief Average the home price of the tracts.

    @param data The house price table.
    @return The mean of PRICE, in thousands of dollars.
    """
    return float(data[constants.COL_PRICE].mean())


def average_price_in_dollars(data: pd.DataFrame) -> float:
    """@brief Average the home price of the tracts in dollars.

    @param data The house price table.
    @return The mean of PRICE, in dollars. It is a statistic of a float
        column, so it is a float and not a Decimal.
    """
    return average_price(data) * constants.THOUSANDS


def river_value_range(data: pd.DataFrame) -> tuple[float, float]:
    """@brief Find the smallest and largest value of CHAS.

    @details CHAS is the Charles River dummy: 1 when the tract bounds the
    river, 0 when it does not.

    @param data The house price table.
    @return A pair of the minimum and the maximum of CHAS.
    """
    column = data[constants.COL_CHAS]
    return float(column.min()), float(column.max())


def river_counts(data: pd.DataFrame) -> pd.Series:
    """@brief Count the tracts that do and do not bound the river.

    @param data The house price table.
    @return The number of tracts, indexed by the CHAS values 0 (not next to
        the river) and 1 (next to the river), in that order. A value that does
        not occur is counted as 0.
    """
    counts = data[constants.COL_CHAS].value_counts()
    return counts.reindex(constants.RIVER_VALUES, fill_value=0).astype(int)


def room_range(data: pd.DataFrame) -> tuple[float, float]:
    """@brief Find the smallest and largest average number of rooms.

    @param data The house price table.
    @return A pair of the minimum and the maximum of RM.
    """
    column = data[constants.COL_RM]
    return float(column.min()), float(column.max())
