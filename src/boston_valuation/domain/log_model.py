"""@brief Log transformation and the two compared models of the Day 81 analysis.

@details Plain pandas, NumPy and scikit-learn rules with no drawing (step 5).
The linear model on the price and the linear model on the log price are fitted
on the same rows, so they come back in one shape, ::FittedModel, and every
split, fit, score and residual rule of ::boston_valuation.domain.regression is
reused.
"""

from typing import NamedTuple

import numpy as np
import pandas as pd
from numpy.typing import NDArray
from sklearn.linear_model import LinearRegression

from boston_valuation import constants
from boston_valuation.domain import regression
from boston_valuation.domain.regression import TrainTestSplit


class FittedModel(NamedTuple):
    """@brief A regression fitted on the training rows, with what it explains.

    @details The target of `split` is the price for the linear model and the
    natural logarithm of the price for the log model; the predictions and the
    residuals are in the same unit as that target.
    """

    split: TrainTestSplit
    model: LinearRegression
    train_r_squared: float
    test_r_squared: float
    predictions: NDArray[np.float64]
    residuals: pd.Series


type LinearModel = FittedModel
type LogModel = FittedModel


class ModelScores(NamedTuple):
    """@brief The r-squared of both models on the rows they never saw.

    @details It unpacks as `linear, log = compare_test_r_squared(data)`.
    """

    linear: float
    log: float


def skew(values: pd.Series) -> float:
    """@brief Measure how lopsided a distribution is.

    @param values The values to measure.
    @return The skew; zero for a symmetric distribution, positive when the tail
        is long on the right.
    """
    return float(values.skew())


def price_skew(data: pd.DataFrame) -> float:
    """@brief Measure the skew of the house prices.

    @param data The house price table.
    @return The skew of PRICE, about 1.11.
    """
    return skew(data[constants.COL_PRICE])


def log_price(data: pd.DataFrame) -> pd.Series:
    """@brief Take the natural logarithm of the house prices.

    @details Large prices are compressed more than small prices, which pulls in
    the long right tail of the prices.

    @param data The house price table.
    @return The log of PRICE, with the index of the table.
    """
    return pd.Series(np.log(data[constants.COL_PRICE]), index=data.index)


def log_price_skew(data: pd.DataFrame) -> float:
    """@brief Measure the skew of the log of the house prices.

    @param data The house price table.
    @return The skew of the log price, about -0.33 and closer to zero than the
        skew of the price.
    """
    return skew(log_price(data))


def _fit_on_target(data: pd.DataFrame, target: pd.Series) -> FittedModel:
    """@brief Split, fit and score a regression of the features on a target.

    @param data The house price table, for its features.
    @param target The values to predict, in the rows of `data`.
    @return The fitted model with its scores, predictions and residuals.
    """
    features = data.drop(columns=constants.COL_PRICE)
    split = regression.split_train_test(features, target)
    model = regression.fit_linear_regression(split.x_train, split.y_train)
    predicted = regression.predictions(model, split.x_train)
    return FittedModel(
        split=split,
        model=model,
        train_r_squared=regression.r_squared(model, split.x_train, split.y_train),
        test_r_squared=regression.r_squared(model, split.x_test, split.y_test),
        predictions=predicted,
        residuals=regression.residuals(split.y_train, predicted),
    )


def fit_linear_model(data: pd.DataFrame) -> LinearModel:
    """@brief Fit the regression on the price.

    @param data The house price table.
    @return The model of step 4: training r-squared 0.75, test r-squared 0.67.
    """
    return _fit_on_target(data, data[constants.COL_PRICE])


def fit_log_model(data: pd.DataFrame) -> LogModel:
    """@brief Fit the regression on the log of the price.

    @details The split uses the same random state as the linear model, so both
    models train and test on the same rows and can be compared.

    @param data The house price table.
    @return The model with training r-squared 0.79 and test r-squared 0.74.
    """
    return _fit_on_target(data, log_price(data))


def log_coefficient_table(fitted: LogModel) -> pd.DataFrame:
    """@brief List the coefficient of every feature of the log model.

    @param fitted The log model.
    @return A one-column table named `coef`, indexed by the feature name. A
        coefficient is the change of the log price for one more unit of the
        feature.
    """
    return regression.coefficient_table(
        fitted.model, fitted.split.x_train.columns, constants.LOG_COEFFICIENT_COLUMN
    )


def coefficient_sign(coefficients: pd.DataFrame, feature: str) -> int:
    """@brief Read the sign of one coefficient.

    @param coefficients A one-column coefficient table.
    @param feature The feature to look up.
    @return 1 for a positive coefficient, -1 for a negative one, 0 for zero.
    """
    return int(np.sign(float(coefficients.loc[feature].iloc[0])))


def has_expected_signs(coefficients: pd.DataFrame) -> bool:
    """@brief Check the signs of the coefficients against what is expected.

    @details A river (CHAS) and more rooms (RM) raise the price; more students
    per teacher (PTRATIO), poverty (LSTAT) and pollution (NOX) lower it.

    @param coefficients The coefficient table of the log model.
    @return True when every feature of ::constants.LOG_EXPECTED_SIGNS has its
        expected sign.
    """
    return all(
        coefficient_sign(coefficients, feature) == sign
        for feature, sign in constants.LOG_EXPECTED_SIGNS
    )


def compare_test_r_squared(data: pd.DataFrame) -> ModelScores:
    """@brief Score both models on the test rows.

    @details The test rows were not used to fit either model, so the scores
    are lower than the training scores. The log model is scored on the log
    price, as the course does.

    @param data The house price table.
    @return The test r-squared of the linear model (0.67) and of the log model
        (0.74).
    """
    return ModelScores(
        linear=fit_linear_model(data).test_r_squared,
        log=fit_log_model(data).test_r_squared,
    )
