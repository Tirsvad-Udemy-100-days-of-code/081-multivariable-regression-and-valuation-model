"""@brief Tests for the split, regression and residual rules of step 4."""

import numpy as np
import pandas as pd
import pytest
from numpy.typing import NDArray
from sklearn.linear_model import LinearRegression

from boston_valuation import constants
from boston_valuation.domain import regression

EXPECTED_TRAIN_ROWS = 404
EXPECTED_TEST_ROWS = 102
EXPECTED_SIGNS = {
    "RM": 3.11,
    "LSTAT": -0.58,
    "NOX": -16.27,
    "CHAS": 1.98,
    "DIS": -1.48,
    "PTRATIO": -0.82,
}


@pytest.fixture(scope="module")
def features_and_target(boston_data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """@brief Separate the price from the features once.

    @param boston_data The real table.
    @return The features and the price.
    """
    return regression.split_features_and_target(boston_data)


@pytest.fixture(scope="module")
def split(
    features_and_target: tuple[pd.DataFrame, pd.Series],
) -> regression.TrainTestSplit:
    """@brief Split the real table with the fixed random state once.

    @param features_and_target The features and the price.
    @return The train and test split.
    """
    features, target = features_and_target
    return regression.split_train_test(features, target)


@pytest.fixture(scope="module")
def model(split: regression.TrainTestSplit) -> LinearRegression:
    """@brief Fit the regression on the training rows once.

    @param split The train and test split.
    @return The fitted model.
    """
    return regression.fit_linear_regression(split.x_train, split.y_train)


@pytest.fixture(scope="module")
def coefficients(
    model: LinearRegression, split: regression.TrainTestSplit
) -> pd.DataFrame:
    """@brief Build the coefficient table once.

    @param model The fitted model.
    @param split The train and test split.
    @return The one-column table of coefficients.
    """
    return regression.coefficient_table(model, split.x_train.columns)


@pytest.fixture(scope="module")
def training_predictions(
    model: LinearRegression, split: regression.TrainTestSplit
) -> NDArray[np.float64]:
    """@brief Predict the training rows once.

    @param model The fitted model.
    @param split The train and test split.
    @return The predicted prices of the training rows.
    """
    return regression.predictions(model, split.x_train)


@pytest.fixture(scope="module")
def training_residuals(
    split: regression.TrainTestSplit, training_predictions: NDArray[np.float64]
) -> pd.Series:
    """@brief Compute the residuals of the training rows once.

    @param split The train and test split.
    @param training_predictions The predicted prices of the training rows.
    @return The actual minus the predicted prices.
    """
    return regression.residuals(split.y_train, training_predictions)


def test_split_features_and_target_keeps_every_other_column(
    features_and_target: tuple[pd.DataFrame, pd.Series],
) -> None:
    """@brief The target column is not among the features."""
    features, target = features_and_target
    assert list(features.columns) == list(constants.FEATURE_COLUMNS)
    assert target.name == constants.COL_PRICE


def test_split_features_and_target_accepts_other_target_column() -> None:
    """@brief Any column can be the target."""
    table = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    features, target = regression.split_features_and_target(table, "b")
    assert list(features.columns) == ["a"]
    assert target.tolist() == [3, 4]


def test_split_train_test_gives_404_training_and_102_test_rows(
    split: regression.TrainTestSplit,
) -> None:
    """@brief The 80/20 split of 506 rows is 404 and 102."""
    assert len(split.x_train) == len(split.y_train) == EXPECTED_TRAIN_ROWS
    assert len(split.x_test) == len(split.y_test) == EXPECTED_TEST_ROWS


def test_split_train_test_unpacks_like_train_test_split(
    split: regression.TrainTestSplit,
) -> None:
    """@brief The split unpacks in the order of the scikit-learn function."""
    x_train, x_test, y_train, y_test = split
    assert x_train is split.x_train
    assert y_test is split.y_test
    assert len(x_test) == len(y_test)
    assert len(y_train) == len(x_train)


def test_split_percentages_are_79_8_and_20_2(
    split: regression.TrainTestSplit,
) -> None:
    """@brief The shares of 404 and 102 of 506 rows."""
    train, test = regression.split_percentages(split)
    assert train == pytest.approx(79.8, abs=0.05)
    assert test == pytest.approx(20.2, abs=0.05)
    assert train + test == pytest.approx(constants.PERCENT)


def test_split_train_test_is_repeatable_with_fixed_random_state(
    features_and_target: tuple[pd.DataFrame, pd.Series],
    split: regression.TrainTestSplit,
) -> None:
    """@brief The same seed picks the same rows."""
    again = regression.split_train_test(*features_and_target)
    assert again.x_train.index.equals(split.x_train.index)
    assert again.x_test.index.equals(split.x_test.index)


def test_split_train_test_changes_rows_with_other_random_state(
    features_and_target: tuple[pd.DataFrame, pd.Series],
    split: regression.TrainTestSplit,
) -> None:
    """@brief Another seed picks other rows."""
    other = regression.split_train_test(*features_and_target, random_state=11)
    assert not other.x_train.index.equals(split.x_train.index)


def test_split_train_test_respects_test_size(
    features_and_target: tuple[pd.DataFrame, pd.Series],
) -> None:
    """@brief A test size of one half gives two equal parts."""
    parts = regression.split_train_test(*features_and_target, test_size=0.5)
    assert len(parts.x_train) == len(parts.x_test) == len(features_and_target[0]) / 2


def test_training_r_squared_is_075(
    model: LinearRegression, split: regression.TrainTestSplit
) -> None:
    """@brief The first model explains 75 % of the training variance."""
    score = regression.r_squared(model, split.x_train, split.y_train)
    assert score == pytest.approx(0.75, abs=0.005)


def test_test_r_squared_is_067(
    model: LinearRegression, split: regression.TrainTestSplit
) -> None:
    """@brief The same model scores lower on rows it never saw."""
    score = regression.r_squared(model, split.x_test, split.y_test)
    assert score == pytest.approx(0.67, abs=0.005)


def test_coefficient_table_has_one_column_indexed_by_feature(
    coefficients: pd.DataFrame,
) -> None:
    """@brief One coefficient per feature, in the order of the features."""
    assert list(coefficients.columns) == [constants.COEFFICIENT_COLUMN]
    assert list(coefficients.index) == list(constants.FEATURE_COLUMNS)


def test_coefficient_table_accepts_column_name(
    model: LinearRegression, split: regression.TrainTestSplit
) -> None:
    """@brief The column can be named for another model."""
    table = regression.coefficient_table(model, split.x_train.columns, "coef")
    assert list(table.columns) == ["coef"]


@pytest.mark.parametrize(("feature", "expected"), EXPECTED_SIGNS.items())
def test_coefficient_table_has_expected_values_and_signs(
    coefficients: pd.DataFrame, feature: str, expected: float
) -> None:
    """@brief The coefficients match the course, including their signs."""
    value = float(coefficients.loc[feature].iloc[0])
    assert value == pytest.approx(expected, abs=0.01)
    assert np.sign(value) == np.sign(expected)


def test_room_premium_is_about_3108_5_dollars(coefficients: pd.DataFrame) -> None:
    """@brief One more room adds about 3108.5 dollars."""
    assert regression.room_premium(coefficients) == pytest.approx(3108.5, abs=0.1)


def test_room_premium_scales_the_rm_coefficient_by_one_thousand() -> None:
    """@brief The price is in thousands, so the premium is 1000 times larger."""
    table = pd.DataFrame({"any": [2.5, 0.1]}, index=[constants.COL_RM, "OTHER"])
    assert regression.room_premium(table) == pytest.approx(2500.0)


def test_predictions_give_one_value_per_row(
    training_predictions: NDArray[np.float64],
) -> None:
    """@brief A prediction for each of the 404 training rows."""
    assert training_predictions.shape == (EXPECTED_TRAIN_ROWS,)


def test_residuals_keep_the_index_of_the_actual_values(
    split: regression.TrainTestSplit, training_residuals: pd.Series
) -> None:
    """@brief Residuals line up with the training rows."""
    assert training_residuals.index.equals(split.y_train.index)


def test_residuals_are_actual_minus_predicted() -> None:
    """@brief The sign follows actual minus predicted."""
    actual = pd.Series([10.0, 20.0], index=[3, 7])
    errors = regression.residuals(actual, np.array([12.0, 15.0]))
    assert errors.tolist() == [-2.0, 5.0]
    assert list(errors.index) == [3, 7]


def test_residual_mean_is_zero_for_a_fitted_line(
    training_residuals: pd.Series,
) -> None:
    """@brief Least squares with an intercept leaves a mean of zero."""
    assert abs(regression.residual_mean(training_residuals)) < 1e-9


def test_residual_skew_is_146(training_residuals: pd.Series) -> None:
    """@brief The residuals have a long tail on the right."""
    assert round(regression.residual_skew(training_residuals), 2) == 1.46


def test_residual_skew_is_zero_for_symmetric_values() -> None:
    """@brief Symmetric values have no skew."""
    assert regression.residual_skew(pd.Series([-2.0, -1.0, 0.0, 1.0, 2.0])) == 0.0


def test_pipeline_works_with_a_log_target(
    features_and_target: tuple[pd.DataFrame, pd.Series],
    split: regression.TrainTestSplit,
) -> None:
    """@brief The same functions serve the log model of the next step."""
    features, target = features_and_target
    log_split = regression.split_train_test(features, np.log(target))
    log_model = regression.fit_linear_regression(log_split.x_train, log_split.y_train)
    score = regression.r_squared(log_model, log_split.x_train, log_split.y_train)
    assert log_split.x_train.index.equals(split.x_train.index)
    assert log_split.y_test.index.equals(split.y_test.index)
    assert score == pytest.approx(0.79, abs=0.005)
