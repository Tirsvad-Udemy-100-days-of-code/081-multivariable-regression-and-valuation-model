"""@brief Tests for the log transformation and the two models of step 5."""

import numpy as np
import pandas as pd
import pytest

from boston_valuation import constants
from boston_valuation.domain import log_model, regression

EXPECTED_TRAIN_ROWS = 404
EXPECTED_TEST_ROWS = 102
POSITIVE_FEATURES = ("CHAS", "RM")
NEGATIVE_FEATURES = ("PTRATIO", "LSTAT", "NOX")


@pytest.fixture(scope="module")
def linear(boston_data: pd.DataFrame) -> log_model.FittedModel:
    """@brief Fit the linear model on the price once.

    @param boston_data The real table.
    @return The fitted linear model.
    """
    return log_model.fit_linear_model(boston_data)


@pytest.fixture(scope="module")
def log(boston_data: pd.DataFrame) -> log_model.FittedModel:
    """@brief Fit the linear model on the log price once.

    @param boston_data The real table.
    @return The fitted log model.
    """
    return log_model.fit_log_model(boston_data)


@pytest.fixture(scope="module")
def log_coefficients(log: log_model.FittedModel) -> pd.DataFrame:
    """@brief Build the coefficient table of the log model once.

    @param log The fitted log model.
    @return The one-column table named `coef`.
    """
    return log_model.log_coefficient_table(log)


def test_price_skew_is_1_11(boston_data: pd.DataFrame) -> None:
    """@brief The prices have a long tail on the right."""
    assert log_model.price_skew(boston_data) == pytest.approx(1.11, abs=0.005)


def test_log_price_skew_is_minus_0_33(boston_data: pd.DataFrame) -> None:
    """@brief The log prices lean slightly to the left."""
    assert log_model.log_price_skew(boston_data) == pytest.approx(-0.33, abs=0.005)


def test_log_price_skew_is_closer_to_zero_than_price_skew(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The log transformation makes the target more symmetric."""
    assert abs(log_model.log_price_skew(boston_data)) < abs(
        log_model.price_skew(boston_data)
    )


def test_skew_is_zero_for_symmetric_values() -> None:
    """@brief Symmetric values have no skew."""
    assert log_model.skew(pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])) == 0.0


def test_skew_is_positive_when_the_tail_is_on_the_right() -> None:
    """@brief A long right tail gives a positive skew."""
    assert log_model.skew(pd.Series([1.0, 1.0, 1.0, 2.0, 20.0])) > 0


def test_log_price_is_the_natural_log_of_each_price(
    boston_data: pd.DataFrame,
) -> None:
    """@brief Each log price is `ln(price)` and keeps the row index."""
    logged = log_model.log_price(boston_data)
    assert logged.index.equals(boston_data.index)
    assert np.exp(logged).to_numpy() == pytest.approx(
        boston_data[constants.COL_PRICE].to_numpy()
    )


def test_log_price_compresses_large_prices_more_than_small_ones() -> None:
    """@brief Doubling a price adds the same log amount, not the same dollars."""
    table = pd.DataFrame({constants.COL_PRICE: [5.0, 10.0, 25.0, 50.0]})
    logged = log_model.log_price(table).to_numpy()
    assert logged[1] - logged[0] == pytest.approx(logged[3] - logged[2])
    assert (np.diff(logged) < np.diff(table[constants.COL_PRICE])).all()


def test_both_models_use_the_same_training_and_test_rows(
    linear: log_model.FittedModel, log: log_model.FittedModel
) -> None:
    """@brief The fixed random state picks the same rows whatever the target."""
    assert log.split.x_train.index.equals(linear.split.x_train.index)
    assert log.split.x_test.index.equals(linear.split.x_test.index)
    assert len(log.split.x_train) == EXPECTED_TRAIN_ROWS
    assert len(log.split.x_test) == EXPECTED_TEST_ROWS


def test_log_model_target_is_the_log_of_the_price(
    boston_data: pd.DataFrame, linear: log_model.FittedModel, log: log_model.FittedModel
) -> None:
    """@brief The log model learns the log of the prices of the linear model."""
    assert log.split.y_train.to_numpy() == pytest.approx(
        np.log(linear.split.y_train.to_numpy())
    )
    assert log.split.y_test.index.equals(linear.split.y_test.index)
    assert linear.split.y_train.equals(
        boston_data.loc[linear.split.y_train.index, constants.COL_PRICE]
    )


def test_training_r_squared_of_the_linear_model_is_075(
    linear: log_model.FittedModel,
) -> None:
    """@brief The first model explains 75 % of the training variance."""
    assert linear.train_r_squared == pytest.approx(0.75, abs=0.005)


def test_training_r_squared_of_the_log_model_is_079(
    log: log_model.FittedModel,
) -> None:
    """@brief The log model explains 79 % of the training variance."""
    assert log.train_r_squared == pytest.approx(0.79, abs=0.005)


def test_log_model_trains_better_than_the_linear_model(
    linear: log_model.FittedModel, log: log_model.FittedModel
) -> None:
    """@brief The transformation raises the training r-squared."""
    assert log.train_r_squared > linear.train_r_squared


def test_test_r_squared_of_the_linear_model_is_067(
    linear: log_model.FittedModel,
) -> None:
    """@brief The first model scores 0.67 on rows it never saw."""
    assert linear.test_r_squared == pytest.approx(0.67, abs=0.01)


def test_test_r_squared_of_the_log_model_is_074(log: log_model.FittedModel) -> None:
    """@brief The log model scores 0.74 on rows it never saw."""
    assert log.test_r_squared == pytest.approx(0.74, abs=0.01)


def test_test_r_squared_is_lower_than_training_r_squared_for_both_models(
    linear: log_model.FittedModel, log: log_model.FittedModel
) -> None:
    """@brief A model is never as good on new rows as on the rows it learned."""
    assert linear.test_r_squared < linear.train_r_squared
    assert log.test_r_squared < log.train_r_squared


def test_log_model_also_wins_on_the_test_rows(
    linear: log_model.FittedModel, log: log_model.FittedModel
) -> None:
    """@brief The improvement holds out of sample."""
    assert log.test_r_squared > linear.test_r_squared


def test_scores_match_the_regression_rules(log: log_model.FittedModel) -> None:
    """@brief The model is scored by the step 4 function, not a second formula."""
    split = log.split
    assert log.train_r_squared == regression.r_squared(
        log.model, split.x_train, split.y_train
    )
    assert log.test_r_squared == regression.r_squared(
        log.model, split.x_test, split.y_test
    )


def test_predictions_and_residuals_are_for_the_training_rows(
    linear: log_model.FittedModel, log: log_model.FittedModel
) -> None:
    """@brief There is one prediction and one residual per training row."""
    for fitted in (linear, log):
        assert fitted.predictions.shape == (EXPECTED_TRAIN_ROWS,)
        assert fitted.residuals.index.equals(fitted.split.y_train.index)
        assert fitted.residuals.to_numpy() == pytest.approx(
            fitted.split.y_train.to_numpy() - fitted.predictions
        )


def test_compare_test_r_squared_returns_both_scores(
    boston_data: pd.DataFrame,
    linear: log_model.FittedModel,
    log: log_model.FittedModel,
) -> None:
    """@brief The comparison unpacks as linear then log."""
    linear_score, log_score = log_model.compare_test_r_squared(boston_data)
    assert linear_score == pytest.approx(0.67, abs=0.01)
    assert log_score == pytest.approx(0.74, abs=0.01)
    assert linear_score == linear.test_r_squared
    assert log_score == log.test_r_squared


def test_compare_test_r_squared_names_its_scores(boston_data: pd.DataFrame) -> None:
    """@brief The scores can be read by name."""
    scores = log_model.compare_test_r_squared(boston_data)
    assert scores.linear < scores.log


def test_log_coefficient_table_is_named_coef_and_indexed_by_feature(
    log_coefficients: pd.DataFrame,
) -> None:
    """@brief One `coef` column with a row per feature."""
    assert list(log_coefficients.columns) == ["coef"]
    assert list(log_coefficients.index) == list(constants.FEATURE_COLUMNS)


@pytest.mark.parametrize(
    ("feature", "expected"),
    [
        ("CHAS", 0.08),
        ("PTRATIO", -0.03),
        ("NOX", -0.70),
        ("RM", 0.07),
        ("LSTAT", -0.03),
    ],
)
def test_log_coefficients_match_the_course(
    log_coefficients: pd.DataFrame, feature: str, expected: float
) -> None:
    """@brief The coefficients round to the values of the course."""
    value = float(log_coefficients.loc[feature].iloc[0])
    assert value == pytest.approx(expected, abs=0.005)


def test_chas_coefficient_is_positive(log_coefficients: pd.DataFrame) -> None:
    """@brief Next to the river, prices are higher."""
    assert log_model.coefficient_sign(log_coefficients, constants.COL_CHAS) == 1


def test_ptratio_coefficient_is_negative(log_coefficients: pd.DataFrame) -> None:
    """@brief More students per teacher lowers prices."""
    assert log_model.coefficient_sign(log_coefficients, constants.COL_PTRATIO) == -1


@pytest.mark.parametrize("feature", POSITIVE_FEATURES)
def test_positive_features_raise_the_log_price(
    log_coefficients: pd.DataFrame, feature: str
) -> None:
    """@brief A river and more rooms raise the price."""
    assert float(log_coefficients.loc[feature].iloc[0]) > 0


@pytest.mark.parametrize("feature", NEGATIVE_FEATURES)
def test_negative_features_lower_the_log_price(
    log_coefficients: pd.DataFrame, feature: str
) -> None:
    """@brief Poverty, pollution and crowded classes lower the price."""
    assert float(log_coefficients.loc[feature].iloc[0]) < 0


def test_has_expected_signs_is_true_for_the_log_model(
    log_coefficients: pd.DataFrame,
) -> None:
    """@brief Every sign of the sense check holds."""
    assert log_model.has_expected_signs(log_coefficients)


def test_has_expected_signs_is_false_when_one_sign_is_flipped(
    log_coefficients: pd.DataFrame,
) -> None:
    """@brief A single wrong sign fails the check."""
    flipped = log_coefficients.copy()
    flipped.loc[constants.COL_PTRATIO] = 0.1
    assert not log_model.has_expected_signs(flipped)


def test_coefficient_sign_is_zero_for_a_zero_coefficient() -> None:
    """@brief Zero is neither positive nor negative."""
    table = pd.DataFrame({"coef": [0.0]}, index=["CHAS"])
    assert log_model.coefficient_sign(table, "CHAS") == 0


def test_residual_mean_of_both_models_is_zero(
    linear: log_model.FittedModel, log: log_model.FittedModel
) -> None:
    """@brief A fitted line with an intercept leaves a mean of zero."""
    assert abs(regression.residual_mean(linear.residuals)) < 1e-9
    assert abs(regression.residual_mean(log.residuals)) < 1e-9


def test_residual_skew_of_the_linear_model_is_146(
    linear: log_model.FittedModel,
) -> None:
    """@brief The linear residuals have a long right tail."""
    assert round(regression.residual_skew(linear.residuals), 2) == 1.46


def test_residual_skew_of_the_log_model_is_009(log: log_model.FittedModel) -> None:
    """@brief The log residuals are almost symmetric."""
    assert round(regression.residual_skew(log.residuals), 2) == 0.09


def test_log_residual_skew_is_closer_to_zero_than_linear_residual_skew(
    linear: log_model.FittedModel, log: log_model.FittedModel
) -> None:
    """@brief The transformation also improves the residuals."""
    assert abs(regression.residual_skew(log.residuals)) < abs(
        regression.residual_skew(linear.residuals)
    )
