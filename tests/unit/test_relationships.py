"""@brief Tests for the correlations behind the relationship charts."""

import pandas as pd
import pytest

from boston_valuation import constants
from boston_valuation.domain import relationships

TOLERANCE = 0.005


def test_distance_pollution_correlation_is_negative(boston_data: pd.DataFrame) -> None:
    """@brief Pollution goes down as the distance to employment goes up."""
    value = relationships.distance_pollution_correlation(boston_data)
    assert value < 0
    assert value == pytest.approx(-0.77, abs=TOLERANCE)


def test_pollution_industry_correlation_is_positive(boston_data: pd.DataFrame) -> None:
    """@brief Pollution goes up with the share of industry."""
    value = relationships.pollution_industry_correlation(boston_data)
    assert value > 0
    assert value == pytest.approx(0.76, abs=TOLERANCE)


def test_poverty_rooms_correlation_is_negative(boston_data: pd.DataFrame) -> None:
    """@brief Homes have fewer rooms where poverty is high."""
    value = relationships.poverty_rooms_correlation(boston_data)
    assert value < 0
    assert value == pytest.approx(-0.61, abs=TOLERANCE)


def test_poverty_price_correlation_is_negative(boston_data: pd.DataFrame) -> None:
    """@brief Prices are lower where poverty is high."""
    value = relationships.poverty_price_correlation(boston_data)
    assert value < 0
    assert value == pytest.approx(-0.74, abs=TOLERANCE)


def test_rooms_price_correlation_is_positive(boston_data: pd.DataFrame) -> None:
    """@brief Prices are higher for homes with more rooms."""
    value = relationships.rooms_price_correlation(boston_data)
    assert value > 0
    assert value == pytest.approx(0.70, abs=TOLERANCE)


def test_correlation_is_symmetric(boston_data: pd.DataFrame) -> None:
    """@brief The order of the two columns does not matter."""
    forward = relationships.correlation(boston_data, constants.COL_DIS, "NOX")
    backward = relationships.correlation(boston_data, "NOX", constants.COL_DIS)
    assert forward == pytest.approx(backward)


def test_correlation_of_a_column_with_itself_is_one(boston_data: pd.DataFrame) -> None:
    """@brief A column is perfectly correlated with itself."""
    assert relationships.correlation(
        boston_data, constants.COL_RM, constants.COL_RM
    ) == pytest.approx(1.0)


def test_correlation_of_a_straight_line_is_exact() -> None:
    """@brief Two columns on a rising line give 1, on a falling line -1."""
    table = pd.DataFrame({"a": [1.0, 2.0, 3.0], "b": [2.0, 4.0, 6.0], "c": [3, 2, 1]})
    assert relationships.correlation(table, "a", "b") == pytest.approx(1.0)
    assert relationships.correlation(table, "a", "c") == pytest.approx(-1.0)


@pytest.mark.parametrize(("first", "second"), [("nope", "RM"), ("RM", "nope")])
def test_correlation_rejects_unknown_column(
    boston_data: pd.DataFrame, first: str, second: str
) -> None:
    """@brief A column that is not in the table raises a specific error."""
    with pytest.raises(relationships.UnknownColumnError, match="nope"):
        relationships.correlation(boston_data, first, second)


def test_correlation_with_price_excludes_price(boston_data: pd.DataFrame) -> None:
    """@brief The result has the 13 features and not PRICE."""
    result = relationships.correlation_with_price(boston_data)
    assert constants.COL_PRICE not in result.index
    assert set(result.index) == set(constants.FEATURE_COLUMNS)


def test_correlation_with_price_is_sorted_by_absolute_value(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The strongest relationship comes first, whatever its sign."""
    result = relationships.correlation_with_price(boston_data)
    magnitudes = result.abs().tolist()
    assert magnitudes == sorted(magnitudes, reverse=True)
    assert list(result.index[:2]) == [constants.COL_LSTAT, constants.COL_RM]


def test_correlation_with_price_matches_the_pair_helpers(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The ranking agrees with the single-pair correlations."""
    result = relationships.correlation_with_price(boston_data)
    assert result[constants.COL_LSTAT] == pytest.approx(
        relationships.poverty_price_correlation(boston_data)
    )
    assert result[constants.COL_RM] == pytest.approx(
        relationships.rooms_price_correlation(boston_data)
    )


def test_correlation_with_price_rejects_table_without_price() -> None:
    """@brief A table without PRICE raises a specific error."""
    with pytest.raises(relationships.UnknownColumnError):
        relationships.correlation_with_price(pd.DataFrame({"RM": [1, 2]}))


def test_correlations_do_not_change_data(boston_data: pd.DataFrame) -> None:
    """@brief Computing leaves the table as it was."""
    before = boston_data.copy()
    relationships.correlation_with_price(boston_data)
    pd.testing.assert_frame_equal(boston_data, before)
