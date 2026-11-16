"""@brief Correlations behind the relationship charts.

@details Plain pandas rules with no drawing. Each helper backs one observation
of the assignment: the sign of the Pearson correlation of a pair of columns.
"""

import pandas as pd

from boston_valuation import constants


class UnknownColumnError(KeyError):
    """@brief Raised when a column asked for is not in the table."""


def correlation(data: pd.DataFrame, first: str, second: str) -> float:
    """@brief Compute the Pearson correlation of two columns.

    @param data The house price table.
    @param first Name of the first column.
    @param second Name of the second column.
    @return The coefficient, from -1 to 1. It does not depend on the order of
        the columns.
    @throws UnknownColumnError When a column is not in the table.
    """
    missing = [name for name in (first, second) if name not in data.columns]
    if missing:
        raise UnknownColumnError(", ".join(missing))
    return float(data[first].corr(data[second]))


def _pair_correlation(data: pd.DataFrame, pair: tuple[str, str]) -> float:
    """@brief Compute the correlation of a pair of columns.

    @param data The house price table.
    @param pair The two column names.
    @return The Pearson coefficient of the pair.
    """
    return correlation(data, *pair)


def distance_pollution_correlation(data: pd.DataFrame) -> float:
    """@brief Correlate the distance to employment with the pollution.

    @param data The house price table.
    @return The coefficient of DIS and NOX; negative, as pollution falls with
        the distance.
    """
    return _pair_correlation(data, constants.PAIR_DISTANCE_POLLUTION)


def pollution_industry_correlation(data: pd.DataFrame) -> float:
    """@brief Correlate the pollution with the share of industry.

    @param data The house price table.
    @return The coefficient of NOX and INDUS; positive, as pollution rises with
        the share of industry.
    """
    return _pair_correlation(data, constants.PAIR_POLLUTION_INDUSTRY)


def poverty_rooms_correlation(data: pd.DataFrame) -> float:
    """@brief Correlate the poverty with the number of rooms.

    @param data The house price table.
    @return The coefficient of LSTAT and RM; negative, as homes have fewer rooms
        where poverty is high.
    """
    return _pair_correlation(data, constants.PAIR_POVERTY_ROOMS)


def poverty_price_correlation(data: pd.DataFrame) -> float:
    """@brief Correlate the poverty with the home price.

    @param data The house price table.
    @return The coefficient of LSTAT and PRICE; negative, as prices fall where
        poverty is high.
    """
    return _pair_correlation(data, constants.PAIR_POVERTY_PRICE)


def rooms_price_correlation(data: pd.DataFrame) -> float:
    """@brief Correlate the number of rooms with the home price.

    @param data The house price table.
    @return The coefficient of RM and PRICE; positive, as prices rise with the
        number of rooms.
    """
    return _pair_correlation(data, constants.PAIR_ROOMS_PRICE)


def correlation_with_price(data: pd.DataFrame) -> pd.Series:
    """@brief Correlate every feature with the home price.

    @param data The house price table.
    @return The coefficient of each feature and PRICE, indexed by the feature
        name and sorted from the strongest to the weakest by absolute value.
        PRICE itself is not in the result.
    @throws UnknownColumnError When PRICE is not in the table.
    """
    if constants.COL_PRICE not in data.columns:
        raise UnknownColumnError(constants.COL_PRICE)
    features = data.drop(columns=constants.COL_PRICE)
    coefficients = features.corrwith(data[constants.COL_PRICE])
    order = coefficients.abs().sort_values(ascending=False).index
    return coefficients.loc[order]
