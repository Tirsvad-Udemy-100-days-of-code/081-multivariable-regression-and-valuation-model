"""@brief Split, regression and residual rules of the Day 81 analysis (step 4).

@details Plain pandas, NumPy and scikit-learn rules with no drawing. Nothing
here knows which target is modelled, so the log model and the valuation reuse
every function with a log-transformed target. The fixed random state makes the
split pick the same rows whatever the target holds.
"""

from collections.abc import Sequence
from typing import NamedTuple

import numpy as np
import pandas as pd
from numpy.typing import NDArray
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from boston_valuation import constants


class TrainTestSplit(NamedTuple):
    """@brief The four parts of a train and test split.

    @details It unpacks in the order of `train_test_split`:
    `x_train, x_test, y_train, y_test = split`.
    """

    x_train: pd.DataFrame
    x_test: pd.DataFrame
    y_train: pd.Series
    y_test: pd.Series


def split_features_and_target(
    data: pd.DataFrame, target_column: str = constants.COL_PRICE
) -> tuple[pd.DataFrame, pd.Series]:
    """@brief Separate the target from the features.

    @param data The house price table.
    @param target_column Name of the column to predict.
    @return The features (every other column) and the target.
    """
    return data.drop(columns=target_column), data[target_column]


def split_train_test(
    features: pd.DataFrame,
    target: pd.Series,
    test_size: float = constants.TEST_SIZE,
    random_state: int = constants.RANDOM_STATE,
) -> TrainTestSplit:
    """@brief Shuffle and split the rows into training and test data.

    @param features The columns the model learns from.
    @param target The values to predict; it may be transformed, such as
        `np.log(price)`, and the same rows are chosen.
    @param test_size Share of the rows kept for the test data.
    @param random_state Seed of the shuffle, so the split can be repeated.
    @return The training and the test parts of the features and the target.
    """
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=test_size, random_state=random_state
    )
    return TrainTestSplit(x_train, x_test, y_train, y_test)


def split_percentages(split: TrainTestSplit) -> tuple[float, float]:
    """@brief Compute the share of the rows in the training and test data.

    @param split The train and test split.
    @return The training and the test share, in percent of all rows.
    """
    train_rows = len(split.x_train)
    test_rows = len(split.x_test)
    total = train_rows + test_rows
    return (
        constants.PERCENT * train_rows / total,
        constants.PERCENT * test_rows / total,
    )


def fit_linear_regression(
    x_train: pd.DataFrame, y_train: pd.Series
) -> LinearRegression:
    """@brief Fit an ordinary least squares regression on the training data.

    @param x_train The training features.
    @param y_train The training target.
    @return The fitted model.
    """
    return LinearRegression().fit(x_train, y_train)


def r_squared(
    model: LinearRegression, features: pd.DataFrame, target: pd.Series
) -> float:
    """@brief Score a fitted model with the coefficient of determination.

    @param model The fitted model.
    @param features The features to predict from; the training features give
        the training r-squared and the test features the test r-squared.
    @param target The actual values of the same rows.
    @return The r-squared, 1 for a perfect fit.
    """
    return float(model.score(features, target))


def coefficient_table(
    model: LinearRegression,
    columns: Sequence[str] | pd.Index,
    column_name: str = constants.COEFFICIENT_COLUMN,
) -> pd.DataFrame:
    """@brief List the coefficient of every feature.

    @param model The fitted model.
    @param columns The feature names, in the order the model was fitted on.
    @param column_name Name of the single column of the table.
    @return A one-column table indexed by the feature name.
    """
    return pd.DataFrame(data=model.coef_, index=list(columns), columns=[column_name])


def room_premium(coefficients: pd.DataFrame) -> float:
    """@brief Compute the price of one extra room in dollars.

    @details The target is in thousands of dollars, so the coefficient of RM is
    scaled by one thousand.

    @param coefficients The one-column table of ::coefficient_table.
    @return The dollars one more room adds, other features held equal.
    """
    return float(coefficients.loc[constants.COL_RM].iloc[0]) * constants.THOUSANDS


def predictions(model: LinearRegression, features: pd.DataFrame) -> NDArray[np.float64]:
    """@brief Predict the target of every row.

    @param model The fitted model.
    @param features The features to predict from.
    @return One predicted value per row.
    """
    return np.asarray(model.predict(features), dtype=np.float64)


def residuals(actual: pd.Series, predicted: NDArray[np.float64]) -> pd.Series:
    """@brief Compute the errors of the predictions.

    @param actual The actual values.
    @param predicted The predicted values of the same rows.
    @return The actual minus the predicted value, with the index of `actual`.
    """
    return actual - predicted


def residual_mean(errors: pd.Series) -> float:
    """@brief Compute the mean of the residuals.

    @param errors The residuals; a fitted line has a mean of zero.
    @return The mean.
    """
    return float(errors.mean())


def residual_skew(errors: pd.Series) -> float:
    """@brief Compute the skew of the residuals.

    @param errors The residuals.
    @return The skew; zero for a symmetric distribution, positive when the tail
        is long on the right.
    """
    return float(errors.skew())
