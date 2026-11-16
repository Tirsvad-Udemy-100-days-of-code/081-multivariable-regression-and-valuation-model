"""@brief Valuing a property with the log model of the Day 81 analysis (step 6).

@details Plain pandas, NumPy and scikit-learn rules with no drawing. A property
is one row with the 13 features. The log model predicts the natural logarithm of
the price in thousands of dollars, so a prediction is turned back into dollars
with the exponential function and a factor of one thousand.
"""

from typing import NamedTuple

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

from boston_valuation import constants
from boston_valuation.domain import log_model


class ValueEstimate(NamedTuple):
    """@brief The estimated value of one property.

    @details It unpacks as `log_estimate, dollar_estimate = estimate`.
    """

    log_estimate: float
    dollar_estimate: float


def average_property(data: pd.DataFrame) -> pd.DataFrame:
    """@brief Build the property that has the mean of every feature.

    @param data The house price table.
    @return A table of one row and one column per feature, in the order of the
        table; PRICE is not a column.
    """
    features = data.drop(columns=constants.COL_PRICE)
    return features.mean().to_frame().T.reset_index(drop=True)


def estimate_value(
    model: LinearRegression, property_stats: pd.DataFrame
) -> ValueEstimate:
    """@brief Estimate the value of a property with the log model.

    @param model The model fitted on the log price.
    @param property_stats A one-row table of the features, in the order the
        model was fitted on.
    @return The log estimate, and the dollar estimate that reverses the log
        transformation with `exp` and scales the thousands to dollars.
    """
    log_estimate = float(model.predict(property_stats)[0])
    dollar_estimate = float(np.exp(log_estimate)) * constants.THOUSANDS
    return ValueEstimate(log_estimate=log_estimate, dollar_estimate=dollar_estimate)


def _require_positive(name: str, value: float) -> None:
    """@brief Reject a characteristic that must be greater than zero.

    @param name The parameter name, for the message.
    @param value The value to check.
    @throws ValueError When the value is not greater than zero.
    """
    if not value > 0:
        raise ValueError(f"{name} must be greater than zero, got {value}")


def _require_not_negative(name: str, value: float) -> None:
    """@brief Reject a characteristic that must not be below zero.

    @param name The parameter name, for the message.
    @param value The value to check.
    @throws ValueError When the value is below zero or not a number.
    """
    if not value >= 0:
        raise ValueError(f"{name} must not be negative, got {value}")


def described_property(
    data: pd.DataFrame,
    next_to_river: bool = constants.NEXT_TO_RIVER,
    nr_rooms: float = constants.NR_ROOMS,
    students_per_classroom: float = constants.STUDENTS_PER_CLASSROOM,
    distance_to_town: float = constants.DISTANCE_TO_TOWN,
    pollution: float | None = None,
    amount_of_poverty: float | None = None,
) -> pd.DataFrame:
    """@brief Build a property from its characteristics and the averages.

    @details RM, PTRATIO, DIS, CHAS, NOX and LSTAT are set; every other feature
    keeps its mean.

    @param data The house price table.
    @param next_to_river True when the property bounds the Charles River
        (CHAS 1), False otherwise (CHAS 0).
    @param nr_rooms Average number of rooms (RM); greater than zero.
    @param students_per_classroom Students per teacher (PTRATIO); greater than
        zero.
    @param distance_to_town Weighted distance to the five employment centres
        (DIS); greater than zero.
    @param pollution Nitric oxide concentration (NOX); the 75th percentile of
        NOX when omitted. It must not be negative.
    @param amount_of_poverty Share of the lower status population (LSTAT); the
        25th percentile of LSTAT when omitted. It must not be negative.
    @return A one-row table in the same columns as ::average_property.
    @throws ValueError When a characteristic is out of range.
    """
    if pollution is None:
        pollution = float(
            data[constants.COL_NOX].quantile(constants.POLLUTION_QUANTILE)
        )
    if amount_of_poverty is None:
        amount_of_poverty = float(
            data[constants.COL_LSTAT].quantile(constants.POVERTY_QUANTILE)
        )
    _require_positive("nr_rooms", nr_rooms)
    _require_positive("students_per_classroom", students_per_classroom)
    _require_positive("distance_to_town", distance_to_town)
    _require_not_negative("pollution", pollution)
    _require_not_negative("amount_of_poverty", amount_of_poverty)
    stats = average_property(data)
    stats[constants.COL_RM] = nr_rooms
    stats[constants.COL_PTRATIO] = students_per_classroom
    stats[constants.COL_DIS] = distance_to_town
    stats[constants.COL_CHAS] = (
        constants.RIVER_YES if next_to_river else constants.RIVER_NO
    )
    stats[constants.COL_NOX] = pollution
    stats[constants.COL_LSTAT] = amount_of_poverty
    return stats


def value_property(
    data: pd.DataFrame,
    model: LinearRegression | None = None,
    next_to_river: bool = constants.NEXT_TO_RIVER,
    nr_rooms: float = constants.NR_ROOMS,
    students_per_classroom: float = constants.STUDENTS_PER_CLASSROOM,
    distance_to_town: float = constants.DISTANCE_TO_TOWN,
    pollution: float | None = None,
    amount_of_poverty: float | None = None,
) -> ValueEstimate:
    """@brief Value a property described by its characteristics.

    @details With the defaults it is the property of the course: next to the
    river, 8 rooms, 20 students per teacher, a distance of 5, high pollution and
    low poverty. It is worth about 3.25 in log price and $25,792.

    @param data The house price table, for the averages and the quantiles.
    @param model The model fitted on the log price; fitted from `data` when
        omitted.
    @param next_to_river True when the property bounds the Charles River.
    @param nr_rooms Average number of rooms; greater than zero.
    @param students_per_classroom Students per teacher; greater than zero.
    @param distance_to_town Weighted distance to the employment centres;
        greater than zero.
    @param pollution Nitric oxide concentration; the 75th percentile of NOX when
        omitted.
    @param amount_of_poverty Share of the lower status population; the 25th
        percentile of LSTAT when omitted.
    @return The log estimate and the dollar estimate.
    @throws ValueError When a characteristic is out of range.
    """
    stats = described_property(
        data,
        next_to_river=next_to_river,
        nr_rooms=nr_rooms,
        students_per_classroom=students_per_classroom,
        distance_to_town=distance_to_town,
        pollution=pollution,
        amount_of_poverty=amount_of_poverty,
    )
    fitted = model if model is not None else log_model.fit_log_model(data).model
    return estimate_value(fitted, stats)


def property_characteristics(
    average: pd.DataFrame, described: pd.DataFrame
) -> pd.DataFrame:
    """@brief Put the six changed characteristics of two properties side by side.

    @param average The one-row table of ::average_property.
    @param described The one-row table of ::described_property.
    @return One row per feature of ::constants.VALUATION_CHANGED_FEATURES and
        two columns, the average and the described property.
    """
    features = list(constants.VALUATION_CHANGED_FEATURES)
    return pd.DataFrame(
        {
            constants.AVERAGE_PROPERTY_LABEL: average.loc[0, features],
            constants.DESCRIBED_PROPERTY_LABEL: described.loc[0, features],
        }
    )
