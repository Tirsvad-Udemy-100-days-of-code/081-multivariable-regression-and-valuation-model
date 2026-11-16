"""@brief Tests for the regression charts of step 4."""

from collections.abc import Iterator

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from matplotlib.axes import Axes
from matplotlib.colors import to_rgb
from matplotlib.figure import Figure
from numpy.typing import NDArray

from boston_valuation import constants
from boston_valuation.domain import regression as rules
from boston_valuation.presentation import regression_charts as charts

PANEL_AXES = 3


@pytest.fixture(scope="module")
def actual() -> pd.Series:
    """@brief Make a few actual prices.

    @return Five prices in thousands of dollars.
    """
    return pd.Series([10.0, 15.0, 20.0, 25.0, 40.0])


@pytest.fixture(scope="module")
def predicted() -> NDArray[np.float64]:
    """@brief Make predictions for the actual prices.

    @return Five predicted prices.
    """
    return np.array([12.0, 14.0, 22.0, 24.0, 33.0])


@pytest.fixture(scope="module")
def errors(actual: pd.Series, predicted: NDArray[np.float64]) -> pd.Series:
    """@brief Make the residuals of the predictions.

    @param actual The actual prices.
    @param predicted The predicted prices.
    @return The actual minus the predicted prices.
    """
    return rules.residuals(actual, predicted)


@pytest.fixture
def fig_actual(actual: pd.Series, predicted: NDArray[np.float64]) -> Iterator[Figure]:
    """@brief Draw the actual against predicted chart and close it afterwards.

    @param actual The actual prices.
    @param predicted The predicted prices.
    @return The figure.
    """
    fig = charts.actual_vs_predicted_figure(actual, predicted)
    yield fig
    plt.close(fig)


@pytest.fixture
def fig_residuals(
    predicted: NDArray[np.float64], errors: pd.Series
) -> Iterator[Figure]:
    """@brief Draw the residuals against predicted chart and close it afterwards.

    @param predicted The predicted prices.
    @param errors The residuals.
    @return The figure.
    """
    fig = charts.residuals_vs_predicted_figure(predicted, errors)
    yield fig
    plt.close(fig)


@pytest.fixture
def fig_distribution(errors: pd.Series) -> Iterator[Figure]:
    """@brief Draw the residual distribution and close it afterwards.

    @param errors The residuals.
    @return The figure.
    """
    fig = charts.residual_distribution_figure(errors)
    yield fig
    plt.close(fig)


def _only_axis(fig: Figure) -> Axes:
    """@brief Return the single axis of a figure.

    @param fig A figure with one axis.
    @return Its axis.
    """
    assert len(fig.axes) == 1
    return fig.axes[0]


def test_actual_vs_predicted_scatter_is_indigo_and_half_transparent(
    fig_actual: Figure,
) -> None:
    """@brief The dots are indigo with an opacity of 0.6."""
    scatter = _only_axis(fig_actual).collections[0]
    assert scatter.get_alpha() == constants.RESIDUAL_ALPHA == 0.6
    assert tuple(scatter.get_facecolor()[0][:3]) == pytest.approx(to_rgb("indigo"))


def test_actual_vs_predicted_scatter_holds_actual_and_predicted(
    fig_actual: Figure, actual: pd.Series, predicted: NDArray[np.float64]
) -> None:
    """@brief Actual prices run along x and predictions along y."""
    offsets = _only_axis(fig_actual).collections[0].get_offsets()
    assert np.asarray(offsets)[:, 0].tolist() == actual.tolist()
    assert np.asarray(offsets)[:, 1].tolist() == predicted.tolist()


def test_actual_vs_predicted_has_cyan_identity_line(
    fig_actual: Figure, actual: pd.Series
) -> None:
    """@brief A cyan line y = x is drawn over the actual values."""
    (line,) = _only_axis(fig_actual).lines
    assert line.get_color() == constants.COLOR_IDENTITY_LINE == "cyan"
    assert list(line.get_xdata()) == list(line.get_ydata()) == actual.tolist()


def test_actual_vs_predicted_labels_and_title_use_math_text(
    fig_actual: Figure,
) -> None:
    """@brief The course titles and labels are used, in the course font sizes."""
    ax = _only_axis(fig_actual)
    assert ax.get_title() == r"Actual vs Predicted Prices: $y _i$ vs $\hat y_i$"
    assert ax.get_xlabel() == r"Actual prices 000s $y _i$"
    assert ax.get_ylabel() == r"Predicted prices 000s $\hat y _i$"
    assert ax.title.get_fontsize() == 17
    assert ax.xaxis.label.get_fontsize() == 14
    assert ax.yaxis.label.get_fontsize() == 14


def test_actual_vs_predicted_accepts_colour_and_text_for_the_log_model(
    actual: pd.Series, predicted: NDArray[np.float64]
) -> None:
    """@brief Colour, title and labels can be replaced."""
    fig = charts.actual_vs_predicted_figure(
        actual,
        predicted,
        colour=constants.COLOR_LOG_MODEL,
        title="Log",
        x_label="x",
        y_label="y",
    )
    try:
        ax = _only_axis(fig)
        face = tuple(ax.collections[0].get_facecolor()[0][:3])
        assert face == pytest.approx(to_rgb(constants.COLOR_LOG_MODEL))
        assert (ax.get_title(), ax.get_xlabel(), ax.get_ylabel()) == ("Log", "x", "y")
    finally:
        plt.close(fig)


def test_residuals_vs_predicted_scatter_is_indigo_and_half_transparent(
    fig_residuals: Figure, predicted: NDArray[np.float64], errors: pd.Series
) -> None:
    """@brief Predictions run along x and residuals along y."""
    scatter = _only_axis(fig_residuals).collections[0]
    offsets = np.asarray(scatter.get_offsets())
    assert scatter.get_alpha() == 0.6
    assert tuple(scatter.get_facecolor()[0][:3]) == pytest.approx(to_rgb("indigo"))
    assert offsets[:, 0].tolist() == predicted.tolist()
    assert offsets[:, 1].tolist() == errors.tolist()


def test_residuals_vs_predicted_has_labels_and_no_identity_line(
    fig_residuals: Figure,
) -> None:
    """@brief The chart has the course title and labels."""
    ax = _only_axis(fig_residuals)
    assert ax.get_title() == "Residuals vs Predicted Values"
    assert ax.get_xlabel() == r"Predicted Prices $\hat y _i$"
    assert ax.get_ylabel() == "Residuals"
    assert len(ax.lines) == 0


def test_residual_distribution_title_carries_skew_and_mean() -> None:
    """@brief The title reports both figures rounded to two decimals."""
    values = pd.Series([0.0, 0.0, 0.0, 1.0, 8.0])
    title = charts.residual_distribution_title(values)
    assert title == (
        f"Residuals Skew ({round(rules.residual_skew(values), 2)}) "
        f"Mean ({round(rules.residual_mean(values), 2)})"
    )


def test_residual_distribution_title_takes_a_prefix() -> None:
    """@brief A prefix names the model."""
    title = charts.residual_distribution_title(pd.Series([1.0, 2.0, 4.0]), "Log: ")
    assert title.startswith("Log: Residuals Skew (")


def test_residual_distribution_title_of_the_real_residuals(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The course reads skew 1.46 and a mean of zero."""
    features, target = rules.split_features_and_target(boston_data)
    parts = rules.split_train_test(features, target)
    model = rules.fit_linear_regression(parts.x_train, parts.y_train)
    errors = rules.residuals(parts.y_train, rules.predictions(model, parts.x_train))
    title = charts.residual_distribution_title(errors)
    assert title.startswith("Residuals Skew (1.46) Mean (")
    assert title.endswith(("0.0)", "-0.0)"))


def test_residual_distribution_is_indigo_with_a_kde(
    fig_distribution: Figure, errors: pd.Series
) -> None:
    """@brief Bars and the density curve are drawn, in indigo."""
    ax = _only_axis(fig_distribution)
    assert len(ax.patches) > 0
    assert tuple(ax.patches[0].get_facecolor()[:3]) == pytest.approx(to_rgb("indigo"))
    (curve,) = ax.lines
    assert to_rgb(curve.get_color()) == pytest.approx(to_rgb("indigo"))
    assert ax.get_title() == charts.residual_distribution_title(errors)
    assert ax.get_xlabel() == "Residuals"


def test_residual_distribution_accepts_colour_and_prefix(errors: pd.Series) -> None:
    """@brief Colour and title prefix can be replaced for the log model."""
    fig = charts.residual_distribution_figure(
        errors, colour=constants.COLOR_LOG_MODEL, title_prefix="Log price model: "
    )
    try:
        ax = _only_axis(fig)
        assert ax.get_title().startswith("Log price model: Residuals Skew (")
        face = tuple(ax.patches[0].get_facecolor()[:3])
        assert face == pytest.approx(to_rgb(constants.COLOR_LOG_MODEL))
    finally:
        plt.close(fig)


def test_regression_panel_has_three_charts_and_the_figures_in_the_title(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The panel carries the r-squared and the room premium."""
    fig = charts.regression_panel_figure(boston_data)
    try:
        assert len(fig.axes) == PANEL_AXES
        title = fig.get_suptitle()
        assert "0.75" in title
        assert "$3108.5" in title
        assert fig.axes[0].get_ylabel() == r"Predicted prices 000s $\hat y _i$"
        assert fig.axes[1].get_title() == "Residuals vs Predicted Values"
        assert fig.axes[2].get_title().startswith("Residuals Skew (1.46)")
    finally:
        plt.close(fig)
