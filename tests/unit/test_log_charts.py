"""@brief Tests for the log transformation charts of step 5."""

from collections.abc import Iterator

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from matplotlib.axes import Axes
from matplotlib.colors import to_rgb
from matplotlib.figure import Figure

from boston_valuation import constants
from boston_valuation.domain import log_model
from boston_valuation.presentation import log_charts

PANEL_AXES = 6
PANEL_ROWS = 2
PANEL_COLUMNS = 3
INDIGO = to_rgb(constants.COLOR_LINEAR_MODEL)
NAVY = to_rgb(constants.COLOR_LOG_MODEL)


def _only_axis(fig: Figure) -> Axes:
    """@brief Return the single axis of a figure.

    @param fig A figure with one axis.
    @return Its axis.
    """
    assert len(fig.axes) == 1
    return fig.axes[0]


def _dot_colour(ax: Axes) -> tuple[float, float, float]:
    """@brief Read the colour of the first scatter collection of an axis.

    @param ax The axis.
    @return The red, green and blue of the dots.
    """
    r, g, b = ax.collections[0].get_facecolor()[0][:3]
    return (float(r), float(g), float(b))


@pytest.fixture
def close_figures() -> Iterator[None]:
    """@brief Close every figure a test drew.

    @return Nothing; the figures are closed after the test.
    """
    yield
    plt.close("all")


@pytest.fixture(scope="module")
def panel(boston_data: pd.DataFrame) -> Iterator[Figure]:
    """@brief Draw the comparison panel once for several tests.

    @param boston_data The real table.
    @return The figure, closed after the last test of the module.
    """
    fig = log_charts.model_comparison_panel_figure(boston_data)
    yield fig
    plt.close(fig)


@pytest.mark.usefixtures("close_figures")
def test_price_skew_figure_is_green_with_the_skew_in_the_title(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The course title reads `Normal Prices. Skew is 1.11`."""
    ax = _only_axis(log_charts.price_skew_figure(boston_data))
    assert ax.get_title() == "Normal Prices. Skew is 1.11"
    assert tuple(ax.patches[0].get_facecolor()[:3]) == pytest.approx(to_rgb("green"))
    (curve,) = ax.lines
    assert to_rgb(curve.get_color()) == pytest.approx(to_rgb("green"))


@pytest.mark.usefixtures("close_figures")
def test_price_skew_figure_shows_the_prices(boston_data: pd.DataFrame) -> None:
    """@brief The bars cover every price of the table."""
    ax = _only_axis(log_charts.price_skew_figure(boston_data))
    assert sum(p.get_height() for p in ax.patches) == len(boston_data)
    assert ax.get_xlabel() == constants.PRICE_X_LABEL


@pytest.mark.usefixtures("close_figures")
def test_log_price_skew_figure_has_the_negative_skew_in_the_title(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The course title reads `Log Prices. Skew is -0.33`."""
    ax = _only_axis(log_charts.log_price_skew_figure(boston_data))
    assert ax.get_title() == "Log Prices. Skew is -0.33"
    assert tuple(ax.patches[0].get_facecolor()[:3]) == pytest.approx(NAVY)
    assert ax.get_xlabel() == "Log Price"


@pytest.mark.usefixtures("close_figures")
def test_log_price_skew_figure_is_on_the_log_scale(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The log prices lie between ln(5) and ln(50)."""
    ax = _only_axis(log_charts.log_price_skew_figure(boston_data))
    low, high = ax.get_xlim()
    assert low > 0
    assert high < float(np.log(constants.THOUSANDS))


@pytest.mark.usefixtures("close_figures")
def test_log_mapping_figure_plots_price_against_log_price(
    boston_data: pd.DataFrame,
) -> None:
    """@brief Each dot is a price and its natural logarithm."""
    fig = log_charts.log_mapping_figure(boston_data)
    ax = _only_axis(fig)
    offsets = np.asarray(ax.collections[0].get_offsets())
    prices = boston_data[constants.COL_PRICE].to_numpy()
    assert offsets[:, 0].tolist() == prices.tolist()
    assert offsets[:, 1] == pytest.approx(np.log(prices))
    assert fig.dpi == constants.LOG_MAPPING_DPI == 150


@pytest.mark.usefixtures("close_figures")
def test_log_mapping_figure_has_the_course_texts(boston_data: pd.DataFrame) -> None:
    """@brief Title and labels are the ones of the lecture."""
    ax = _only_axis(log_charts.log_mapping_figure(boston_data))
    assert ax.get_title() == "Mapping the Original Price to a Log Price"
    assert ax.get_xlabel() == "Actual $ Price in 000s"
    assert ax.get_ylabel() == "Log Price"


@pytest.mark.usefixtures("close_figures")
def test_log_actual_vs_predicted_is_navy_with_a_cyan_line_and_the_r_squared(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The title carries the training r-squared 0.79."""
    ax = _only_axis(log_charts.log_actual_vs_predicted_figure(boston_data))
    assert _dot_colour(ax) == pytest.approx(NAVY)
    assert ax.collections[0].get_alpha() == constants.RESIDUAL_ALPHA
    (line,) = ax.lines
    assert line.get_color() == constants.COLOR_IDENTITY_LINE == "cyan"
    assert ax.get_title() == (
        r"Actual vs Predicted Log Prices: $y _i$ vs $\hat y_i$ (R-Squared 0.79)"
    )
    assert ax.get_xlabel() == r"Actual Log Prices $y _i$"
    assert ax.get_ylabel() == r"Predicted Log Prices $\hat y _i$"


@pytest.mark.usefixtures("close_figures")
def test_log_actual_vs_predicted_holds_the_training_rows(
    boston_data: pd.DataFrame,
) -> None:
    """@brief Log prices run along x and the predictions along y."""
    fitted = log_model.fit_log_model(boston_data)
    ax = _only_axis(log_charts.log_actual_vs_predicted_figure(boston_data))
    offsets = np.asarray(ax.collections[0].get_offsets())
    assert offsets[:, 0].tolist() == fitted.split.y_train.tolist()
    assert offsets[:, 1].tolist() == fitted.predictions.tolist()


@pytest.mark.usefixtures("close_figures")
def test_log_residuals_vs_predicted_is_navy_with_the_course_texts(
    boston_data: pd.DataFrame,
) -> None:
    """@brief Predictions run along x and residuals along y."""
    fitted = log_model.fit_log_model(boston_data)
    ax = _only_axis(log_charts.log_residuals_vs_predicted_figure(boston_data))
    offsets = np.asarray(ax.collections[0].get_offsets())
    assert _dot_colour(ax) == pytest.approx(NAVY)
    assert offsets[:, 0].tolist() == fitted.predictions.tolist()
    assert offsets[:, 1].tolist() == fitted.residuals.tolist()
    assert ax.get_title() == "Residuals vs Fitted Values for Log Prices"
    assert ax.get_xlabel() == r"Predicted Log Prices $\hat y _i$"
    assert ax.get_ylabel() == "Residuals"


@pytest.mark.usefixtures("close_figures")
def test_log_residual_distribution_title_carries_skew_and_mean(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The log residuals read skew 0.09 and a mean of zero."""
    ax = _only_axis(log_charts.log_residual_distribution_figure(boston_data))
    assert ax.get_title().startswith("Log price model: Residuals Skew (0.09) Mean (")
    assert ax.get_title().endswith(("0.0)", "-0.0)"))
    assert tuple(ax.patches[0].get_facecolor()[:3]) == pytest.approx(NAVY)
    (curve,) = ax.lines
    assert to_rgb(curve.get_color()) == pytest.approx(NAVY)


def test_panel_is_two_rows_of_three_charts(panel: Figure) -> None:
    """@brief Both models are drawn with the same three charts."""
    assert len(panel.axes) == PANEL_AXES
    assert len(panel.subfigs) == PANEL_ROWS
    assert all(len(row.axes) == PANEL_COLUMNS for row in panel.subfigs)


def test_panel_top_row_is_the_linear_model_in_indigo(panel: Figure) -> None:
    """@brief The scatter dots and the bars of the top row are indigo."""
    actual_ax, residuals_ax, distribution_ax = panel.subfigs[0].axes
    assert _dot_colour(actual_ax) == pytest.approx(INDIGO)
    assert _dot_colour(residuals_ax) == pytest.approx(INDIGO)
    assert tuple(distribution_ax.patches[0].get_facecolor()[:3]) == pytest.approx(
        INDIGO
    )


def test_panel_bottom_row_is_the_log_model_in_navy(panel: Figure) -> None:
    """@brief The scatter dots and the bars of the bottom row are navy."""
    actual_ax, residuals_ax, distribution_ax = panel.subfigs[1].axes
    assert _dot_colour(actual_ax) == pytest.approx(NAVY)
    assert _dot_colour(residuals_ax) == pytest.approx(NAVY)
    assert tuple(distribution_ax.patches[0].get_facecolor()[:3]) == pytest.approx(NAVY)


def test_panel_draws_a_cyan_identity_line_in_both_actual_charts(
    panel: Figure,
) -> None:
    """@brief A perfect model would lie on the cyan line in both rows."""
    for row in panel.subfigs:
        line = row.axes[0].lines[0]
        assert line.get_color() == constants.COLOR_IDENTITY_LINE


def test_panel_title_carries_the_training_and_test_r_squared(panel: Figure) -> None:
    """@brief The figure states 0.75 vs 0.79 and 0.67 vs 0.74."""
    assert panel.get_suptitle() == (
        "Linear vs log price model: training r-squared 0.75 vs 0.79, "
        "test r-squared 0.67 vs 0.74"
    )


def test_panel_row_titles_carry_the_r_squared_of_their_model(panel: Figure) -> None:
    """@brief Each row names its model and its two scores."""
    top, bottom = panel.subfigs
    assert top.get_suptitle() == (
        "Linear model on the price (indigo): training r-squared 0.75, "
        "test r-squared 0.67"
    )
    assert bottom.get_suptitle() == (
        "Linear model on the log price (navy): training r-squared 0.79, "
        "test r-squared 0.74"
    )


def test_panel_axis_titles_name_the_models_and_the_residual_figures(
    panel: Figure,
) -> None:
    """@brief Residual distribution titles carry 1.46 and 0.09."""
    top, bottom = panel.subfigs
    assert top.axes[0].get_title().startswith("Actual vs Predicted Prices")
    assert top.axes[1].get_title() == "Residuals vs Predicted Values"
    assert top.axes[2].get_title().startswith("Original model: Residuals Skew (1.46)")
    assert bottom.axes[0].get_title().startswith("Actual vs Predicted Log Prices")
    assert bottom.axes[1].get_title() == "Residuals vs Fitted Values for Log Prices"
    assert (
        bottom.axes[2].get_title().startswith("Log price model: Residuals Skew (0.09)")
    )


def test_panel_uses_the_picture_resolution_and_size(panel: Figure) -> None:
    """@brief The panel has the size and dpi set in the constants."""
    assert panel.dpi == constants.PICTURE_DPI
    assert tuple(panel.get_size_inches()) == pytest.approx(
        constants.COMPARISON_PANEL_FIGURE_SIZE
    )
