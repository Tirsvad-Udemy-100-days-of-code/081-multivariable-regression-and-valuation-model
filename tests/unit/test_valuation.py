"""@brief Tests for valuing a property with the log model (step 6)."""

import numpy as np
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression

from boston_valuation import constants
from boston_valuation.domain import log_model, valuation

AVERAGE_LOG_ESTIMATE = 3.03
AVERAGE_DOLLAR_ESTIMATE = 20_703
DESCRIBED_LOG_ESTIMATE = 3.25
DESCRIBED_DOLLAR_ESTIMATE = 25_792
FEATURE_COUNT = 13
LOW_VALUE = 0.0
NEGATIVE_VALUE = -1.0
CHANGED_FEATURES = set(constants.VALUATION_CHANGED_FEATURES)


@pytest.fixture(scope="module")
def model(boston_data: pd.DataFrame) -> LinearRegression:
    """@brief Fit the log model once.

    @param boston_data The real table.
    @return The fitted regression of the log price.
    """
    return log_model.fit_log_model(boston_data).model


@pytest.fixture(scope="module")
def average(boston_data: pd.DataFrame) -> pd.DataFrame:
    """@brief Build the average property once.

    @param boston_data The real table.
    @return The one-row table of the means.
    """
    return valuation.average_property(boston_data)


@pytest.fixture(scope="module")
def described(boston_data: pd.DataFrame) -> pd.DataFrame:
    """@brief Build the property of the course once.

    @param boston_data The real table.
    @return The one-row table of the described property.
    """
    return valuation.described_property(boston_data)


def test_average_property_is_one_row_of_13_features(average: pd.DataFrame) -> None:
    """@brief The row holds every feature and nothing else."""
    assert average.shape == (1, FEATURE_COUNT)
    assert constants.COL_PRICE not in average.columns


def test_average_property_keeps_the_feature_order(average: pd.DataFrame) -> None:
    """@brief The columns are the features in the order of the table."""
    assert tuple(average.columns) == constants.FEATURE_COLUMNS


def test_average_property_holds_the_column_means(
    boston_data: pd.DataFrame, average: pd.DataFrame
) -> None:
    """@brief Every value is the mean of its column."""
    expected = boston_data.drop(columns=constants.COL_PRICE).mean()
    assert average.iloc[0].to_numpy() == pytest.approx(expected.to_numpy())


def test_average_property_does_not_change_the_data(boston_data: pd.DataFrame) -> None:
    """@brief Building the row leaves the table as it was."""
    before = boston_data.copy()
    valuation.average_property(boston_data)
    pd.testing.assert_frame_equal(boston_data, before)


def test_average_property_log_estimate_is_3_03(
    model: LinearRegression, average: pd.DataFrame
) -> None:
    """@brief The average property has a log estimate of about 3.03."""
    estimate = valuation.estimate_value(model, average)
    assert estimate.log_estimate == pytest.approx(AVERAGE_LOG_ESTIMATE, abs=0.01)


def test_average_property_dollar_estimate_is_20703(
    model: LinearRegression, average: pd.DataFrame
) -> None:
    """@brief The average property is worth about $20,703."""
    estimate = valuation.estimate_value(model, average)
    assert estimate.dollar_estimate == pytest.approx(AVERAGE_DOLLAR_ESTIMATE, abs=5)


def test_dollar_estimate_reverses_the_log_transformation(
    model: LinearRegression, average: pd.DataFrame
) -> None:
    """@brief The dollars are exp of the log estimate, in thousands."""
    estimate = valuation.estimate_value(model, average)
    assert estimate.dollar_estimate == pytest.approx(
        np.exp(estimate.log_estimate) * constants.THOUSANDS
    )


def test_value_estimate_unpacks_log_then_dollars() -> None:
    """@brief The estimate unpacks in the order of its fields."""
    log_estimate, dollar_estimate = valuation.ValueEstimate(1.0, 2.0)
    assert (log_estimate, dollar_estimate) == (1.0, 2.0)


def test_described_property_changes_only_the_six_characteristics(
    average: pd.DataFrame, described: pd.DataFrame
) -> None:
    """@brief Every other feature keeps its mean."""
    assert tuple(described.columns) == tuple(average.columns)
    differing = {
        column
        for column in average.columns
        if average.loc[0, column] != described.loc[0, column]
    }
    assert differing == CHANGED_FEATURES


def test_described_property_has_the_course_characteristics(
    boston_data: pd.DataFrame, described: pd.DataFrame
) -> None:
    """@brief River, 8 rooms, 20 students, distance 5, quantiles for the rest."""
    row = described.iloc[0]
    assert row[constants.COL_CHAS] == constants.RIVER_YES
    assert row[constants.COL_RM] == constants.NR_ROOMS
    assert row[constants.COL_PTRATIO] == constants.STUDENTS_PER_CLASSROOM
    assert row[constants.COL_DIS] == constants.DISTANCE_TO_TOWN
    assert row[constants.COL_NOX] == pytest.approx(
        boston_data[constants.COL_NOX].quantile(0.75)
    )
    assert row[constants.COL_LSTAT] == pytest.approx(
        boston_data[constants.COL_LSTAT].quantile(0.25)
    )


def test_pollution_and_poverty_default_to_the_quantiles(
    boston_data: pd.DataFrame, described: pd.DataFrame
) -> None:
    """@brief NOX is the 75th and LSTAT the 25th percentile."""
    nox = boston_data[constants.COL_NOX].quantile(constants.POLLUTION_QUANTILE)
    lstat = boston_data[constants.COL_LSTAT].quantile(constants.POVERTY_QUANTILE)
    assert described.loc[0, constants.COL_NOX] == pytest.approx(nox)
    assert described.loc[0, constants.COL_LSTAT] == pytest.approx(lstat)
    assert (constants.POLLUTION_QUANTILE, constants.POVERTY_QUANTILE) == (0.75, 0.25)


def test_explicit_pollution_and_poverty_replace_the_defaults(
    boston_data: pd.DataFrame,
) -> None:
    """@brief Given values are used as they are."""
    row = valuation.described_property(
        boston_data, pollution=0.5, amount_of_poverty=10.0
    ).iloc[0]
    assert row[constants.COL_NOX] == 0.5
    assert row[constants.COL_LSTAT] == 10.0


def test_not_next_to_the_river_sets_chas_to_zero(boston_data: pd.DataFrame) -> None:
    """@brief CHAS is the dummy 0 when the property is away from the river."""
    row = valuation.described_property(boston_data, next_to_river=False).iloc[0]
    assert row[constants.COL_CHAS] == constants.RIVER_NO


def test_described_property_log_estimate_is_3_25(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The described property has a log estimate of about 3.25."""
    estimate = valuation.value_property(boston_data)
    assert estimate.log_estimate == pytest.approx(DESCRIBED_LOG_ESTIMATE, abs=0.01)


def test_described_property_dollar_estimate_is_25792(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The described property is worth about $25,792."""
    estimate = valuation.value_property(boston_data)
    assert estimate.dollar_estimate == pytest.approx(DESCRIBED_DOLLAR_ESTIMATE, abs=10)


def test_value_property_gives_the_same_result_with_a_fitted_model(
    boston_data: pd.DataFrame, model: LinearRegression
) -> None:
    """@brief Passing the fitted model changes nothing."""
    assert valuation.value_property(boston_data, model) == valuation.value_property(
        boston_data
    )


def test_value_property_uses_the_model_it_is_given(
    boston_data: pd.DataFrame,
) -> None:
    """@brief A model fitted on another target gives another estimate."""
    linear = log_model.fit_linear_model(boston_data).model
    assert valuation.value_property(boston_data, linear) != valuation.value_property(
        boston_data
    )


def test_value_property_is_higher_next_to_the_river(boston_data: pd.DataFrame) -> None:
    """@brief The CHAS coefficient is positive, so the river raises the value."""
    near = valuation.value_property(boston_data, next_to_river=True)
    away = valuation.value_property(boston_data, next_to_river=False)
    assert near.log_estimate > away.log_estimate
    assert near.dollar_estimate > away.dollar_estimate


def test_value_property_rises_with_more_rooms(boston_data: pd.DataFrame) -> None:
    """@brief The RM coefficient is positive."""
    small = valuation.value_property(boston_data, nr_rooms=5)
    large = valuation.value_property(boston_data, nr_rooms=8)
    assert large.dollar_estimate > small.dollar_estimate


def test_value_property_falls_with_more_students_per_teacher(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The PTRATIO coefficient is negative."""
    few = valuation.value_property(boston_data, students_per_classroom=15)
    many = valuation.value_property(boston_data, students_per_classroom=22)
    assert many.dollar_estimate < few.dollar_estimate


def test_value_property_does_not_change_the_data(boston_data: pd.DataFrame) -> None:
    """@brief Valuing a property leaves the table as it was."""
    before = boston_data.copy()
    valuation.value_property(boston_data)
    pd.testing.assert_frame_equal(boston_data, before)


@pytest.mark.parametrize("rooms", [LOW_VALUE, NEGATIVE_VALUE, float("nan")])
def test_value_property_rejects_rooms_that_are_not_positive(
    boston_data: pd.DataFrame, rooms: float
) -> None:
    """@brief Zero, negative and missing rooms are refused."""
    with pytest.raises(ValueError, match="nr_rooms"):
        valuation.value_property(boston_data, nr_rooms=rooms)


@pytest.mark.parametrize("students", [LOW_VALUE, NEGATIVE_VALUE])
def test_value_property_rejects_students_that_are_not_positive(
    boston_data: pd.DataFrame, students: float
) -> None:
    """@brief A class size of zero or less is refused."""
    with pytest.raises(ValueError, match="students_per_classroom"):
        valuation.value_property(boston_data, students_per_classroom=students)


@pytest.mark.parametrize("distance", [LOW_VALUE, NEGATIVE_VALUE])
def test_value_property_rejects_a_distance_that_is_not_positive(
    boston_data: pd.DataFrame, distance: float
) -> None:
    """@brief A distance of zero or less is refused."""
    with pytest.raises(ValueError, match="distance_to_town"):
        valuation.value_property(boston_data, distance_to_town=distance)


def test_value_property_rejects_negative_pollution(boston_data: pd.DataFrame) -> None:
    """@brief A concentration below zero is refused."""
    with pytest.raises(ValueError, match="pollution"):
        valuation.value_property(boston_data, pollution=NEGATIVE_VALUE)


def test_value_property_rejects_negative_poverty(boston_data: pd.DataFrame) -> None:
    """@brief A share below zero is refused."""
    with pytest.raises(ValueError, match="amount_of_poverty"):
        valuation.value_property(boston_data, amount_of_poverty=NEGATIVE_VALUE)


def test_value_property_accepts_zero_pollution_and_poverty(
    boston_data: pd.DataFrame,
) -> None:
    """@brief Zero is the boundary and it is allowed."""
    estimate = valuation.value_property(boston_data, pollution=0.0, amount_of_poverty=0)
    assert estimate.dollar_estimate > 0


def test_property_characteristics_lists_the_six_changed_features(
    average: pd.DataFrame, described: pd.DataFrame
) -> None:
    """@brief The table has one row per changed feature and two columns."""
    table = valuation.property_characteristics(average, described)
    assert tuple(table.index) == constants.VALUATION_CHANGED_FEATURES
    assert list(table.columns) == [
        constants.AVERAGE_PROPERTY_LABEL,
        constants.DESCRIBED_PROPERTY_LABEL,
    ]
    assert table.loc[constants.COL_RM].tolist() == pytest.approx([6.28, 8.0], abs=0.01)
    assert table.loc[constants.COL_PTRATIO].tolist() == pytest.approx(
        [18.46, 20.0], abs=0.01
    )
    assert table.loc[constants.COL_DIS].tolist() == pytest.approx([3.80, 5.0], abs=0.01)
    assert table.loc[constants.COL_CHAS].tolist() == pytest.approx(
        [0.07, 1.0], abs=0.01
    )
