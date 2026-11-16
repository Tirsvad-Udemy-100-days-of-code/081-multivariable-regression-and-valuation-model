"""@brief Averages and counts behind the distribution charts.

@details Plain pandas rules with no drawing. The averages of an empty table are
NaN, as pandas defines them, and the counts of an empty table are 0.
"""

import pandas as pd

from boston_valuation import constants
from boston_valuation.domain.descriptive import average_price, river_counts


def average_distance(data: pd.DataFrame) -> float:
    """@brief Average the distance to the employment centres.

    @param data The house price table.
    @return The mean of DIS, the weighted distance to the 5 Boston employment
        centres.
    """
    return float(data[constants.COL_DIS].mean())


def average_rooms(data: pd.DataFrame) -> float:
    """@brief Average the number of rooms per dwelling.

    @param data The house price table.
    @return The mean of RM.
    """
    return float(data[constants.COL_RM].mean())


def price_title(data: pd.DataFrame) -> str:
    """@brief Write the title of the price chart with the average price.

    @param data The house price table.
    @return The title, with the mean of PRICE in thousands of dollars.
    """
    return constants.PRICE_TITLE.format(average=average_price(data))


def distance_title(data: pd.DataFrame) -> str:
    """@brief Write the title of the distance chart with the average distance.

    @param data The house price table.
    @return The title, with the mean of DIS.
    """
    return constants.DISTANCE_TITLE.format(average=average_distance(data))


def rooms_title(data: pd.DataFrame) -> str:
    """@brief Write the title of the rooms chart with the average rooms.

    @param data The house price table.
    @return The title, with the mean of RM.
    """
    return constants.ROOMS_TITLE.format(average=average_rooms(data))


def highway_access_counts(data: pd.DataFrame) -> pd.Series:
    """@brief Count the tracts per value of the highway accessibility index.

    @param data The house price table.
    @return The number of tracts, indexed by the RAD values in ascending order.
    """
    return data[constants.COL_RAD].value_counts().sort_index()


def river_counts_by_label(data: pd.DataFrame) -> pd.Series:
    """@brief Count the tracts that do and do not bound the river, by label.

    @param data The house price table.
    @return The number of tracts, indexed by the labels `No` and `Yes`, in that
        order. A value that does not occur is counted as 0.
    """
    counts = river_counts(data)
    return pd.Series(
        counts.to_numpy(), index=pd.Index(constants.RIVER_LABELS), dtype=int
    )
