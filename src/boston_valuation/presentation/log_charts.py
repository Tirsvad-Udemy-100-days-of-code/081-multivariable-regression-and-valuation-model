"""@brief Log transformation and model comparison charts of the Day 81 analysis.

@details Every function returns a figure and never shows it; the caller saves
it and closes it with `plt.close`. The regression charts of step 4 are reused,
with the navy colour and the log price texts of the log model.
"""

import matplotlib

matplotlib.use("Agg")

from dataclasses import dataclass  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import seaborn as sns  # noqa: E402
from matplotlib.figure import Figure, SubFigure  # noqa: E402

from boston_valuation import constants  # noqa: E402
from boston_valuation.domain import log_model  # noqa: E402
from boston_valuation.domain.log_model import FittedModel  # noqa: E402
from boston_valuation.presentation import regression_charts  # noqa: E402


@dataclass(frozen=True, slots=True)
class _RowStyle:
    """@brief Colour and texts of one row of the comparison panel."""

    colour: str
    row_title: str
    actual_title: str
    actual_x_label: str
    actual_y_label: str
    residuals_title: str
    residuals_x_label: str
    residual_prefix: str


_LINEAR_STYLE = _RowStyle(
    colour=constants.COLOR_LINEAR_MODEL,
    row_title=constants.LINEAR_ROW_TITLE,
    actual_title=constants.ACTUAL_VS_PREDICTED_TITLE,
    actual_x_label=constants.ACTUAL_PRICE_X_LABEL,
    actual_y_label=constants.PREDICTED_PRICE_Y_LABEL,
    residuals_title=constants.RESIDUALS_VS_PREDICTED_TITLE,
    residuals_x_label=constants.PREDICTED_PRICE_X_LABEL,
    residual_prefix=constants.ORIGINAL_RESIDUAL_PREFIX,
)
_LOG_STYLE = _RowStyle(
    colour=constants.COLOR_LOG_MODEL,
    row_title=constants.LOG_ROW_TITLE,
    actual_title=constants.LOG_ACTUAL_VS_PREDICTED_PANEL_TITLE,
    actual_x_label=constants.LOG_ACTUAL_X_LABEL,
    actual_y_label=constants.LOG_PREDICTED_Y_LABEL,
    residuals_title=constants.LOG_RESIDUALS_VS_PREDICTED_TITLE,
    residuals_x_label=constants.LOG_PREDICTED_X_LABEL,
    residual_prefix=constants.LOG_RESIDUAL_PREFIX,
)


def _distribution_figure(
    values: pd.Series, colour: str, title: str, x_label: str
) -> Figure:
    """@brief Draw a histogram with a KDE of some values.

    @param values The values to show.
    @param colour Colour of the bars and the curve.
    @param title Title of the chart.
    @param x_label Label of the horizontal axis.
    @return The figure. The caller saves and closes it.
    """
    fig, ax = regression_charts.single_axes()
    sns.histplot(values, kde=True, color=colour, ax=ax)
    ax.set_title(title, fontsize=constants.REGRESSION_LABEL_FONT_SIZE)
    ax.set_xlabel(x_label, fontsize=constants.REGRESSION_LABEL_FONT_SIZE)
    ax.set_ylabel(
        constants.DISTRIBUTION_COUNT_LABEL,
        fontsize=constants.REGRESSION_LABEL_FONT_SIZE,
    )
    return fig


def price_skew_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the distribution of the prices with its skew.

    @param data The house price table.
    @return A green histogram with a KDE, titled `Normal Prices. Skew is 1.11`.
        The caller saves and closes it.
    """
    return _distribution_figure(
        data[constants.COL_PRICE],
        constants.COLOR_PRICE_SKEW,
        constants.PRICE_SKEW_TITLE.format(skew=log_model.price_skew(data)),
        constants.PRICE_X_LABEL,
    )


def log_price_skew_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the distribution of the log prices with its skew.

    @param data The house price table.
    @return A navy histogram with a KDE, titled `Log Prices. Skew is -0.33`.
        The caller saves and closes it.
    """
    return _distribution_figure(
        log_model.log_price(data),
        constants.COLOR_LOG_MODEL,
        constants.LOG_PRICE_SKEW_TITLE.format(skew=log_model.log_price_skew(data)),
        constants.LOG_PRICE_X_LABEL,
    )


def log_mapping_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw how the log maps each price to a smaller number.

    @param data The house price table.
    @return A scatter plot of the price against its log, which bends flatter
        for large prices. The caller saves and closes it.
    """
    fig, ax = plt.subplots(dpi=constants.LOG_MAPPING_DPI)
    ax.scatter(data[constants.COL_PRICE], log_model.log_price(data))
    ax.set_title(constants.LOG_MAPPING_TITLE)
    ax.set_xlabel(constants.LOG_MAPPING_X_LABEL)
    ax.set_ylabel(constants.LOG_MAPPING_Y_LABEL)
    return fig


def log_actual_vs_predicted_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the predicted log prices against the actual log prices.

    @param data The house price table.
    @return A navy scatter plot with a cyan line `y = x`, titled with the
        training r-squared, for example `(R-Squared 0.79)`. The caller saves and
        closes it.
    """
    fitted = log_model.fit_log_model(data)
    return regression_charts.actual_vs_predicted_figure(
        fitted.split.y_train,
        fitted.predictions,
        colour=constants.COLOR_LOG_MODEL,
        title=constants.LOG_ACTUAL_VS_PREDICTED_TITLE.format(
            r_squared=fitted.train_r_squared
        ),
        x_label=constants.LOG_ACTUAL_X_LABEL,
        y_label=constants.LOG_PREDICTED_Y_LABEL,
    )


def log_residuals_vs_predicted_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the residuals of the log model against its predictions.

    @param data The house price table.
    @return A navy scatter plot. The caller saves and closes it.
    """
    fitted = log_model.fit_log_model(data)
    return regression_charts.residuals_vs_predicted_figure(
        fitted.predictions,
        fitted.residuals,
        colour=constants.COLOR_LOG_MODEL,
        title=constants.LOG_RESIDUALS_VS_PREDICTED_TITLE,
        x_label=constants.LOG_PREDICTED_X_LABEL,
    )


def log_residual_distribution_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the distribution of the residuals of the log model.

    @param data The house price table.
    @return A navy histogram with a KDE, titled for example
        `Log price model: Residuals Skew (0.09) Mean (0.0)`. The caller saves
        and closes it.
    """
    return regression_charts.residual_distribution_figure(
        log_model.fit_log_model(data).residuals,
        colour=constants.COLOR_LOG_MODEL,
        title_prefix=constants.LOG_RESIDUAL_PREFIX,
    )


def _draw_row(subfigure: SubFigure, fitted: FittedModel, style: _RowStyle) -> None:
    """@brief Draw the three charts of one model in a row.

    @param subfigure The part of the figure that holds the row.
    @param fitted The model to show.
    @param style Colour and texts of the row.
    """
    size = constants.PANEL_AXES_TITLE_FONT_SIZE
    axes = subfigure.subplots(1, constants.COMPARISON_PANEL_COLUMNS)
    actual_ax, residuals_ax, distribution_ax = axes.ravel()
    regression_charts.draw_actual_vs_predicted(
        actual_ax,
        fitted.split.y_train,
        fitted.predictions,
        style.colour,
        style.actual_title,
        style.actual_x_label,
        style.actual_y_label,
        size,
        size,
    )
    regression_charts.draw_residuals_vs_predicted(
        residuals_ax,
        fitted.predictions,
        fitted.residuals,
        style.colour,
        size,
        size,
        style.residuals_title,
        style.residuals_x_label,
    )
    regression_charts.draw_residual_distribution(
        distribution_ax,
        fitted.residuals,
        style.colour,
        style.residual_prefix,
        size,
        size,
    )
    subfigure.suptitle(
        style.row_title.format(
            train=fitted.train_r_squared, test=fitted.test_r_squared
        ),
        fontsize=constants.COMPARISON_ROW_TITLE_FONT_SIZE,
    )


def model_comparison_panel_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the linear model and the log model side by side.

    @param data The house price table.
    @return A figure of two rows and three columns. The top row shows the
        linear model in indigo and the bottom row the log model in navy: actual
        against predicted, residuals against predicted and the residual
        distribution. The titles carry the training and the test r-squared of
        both models. The caller saves and closes it.
    """
    linear = log_model.fit_linear_model(data)
    log = log_model.fit_log_model(data)
    fig = plt.figure(
        figsize=constants.COMPARISON_PANEL_FIGURE_SIZE,
        dpi=constants.PICTURE_DPI,
        layout="constrained",
    )
    top, bottom = fig.subfigures(constants.COMPARISON_PANEL_ROWS, 1)
    _draw_row(top, linear, _LINEAR_STYLE)
    _draw_row(bottom, log, _LOG_STYLE)
    fig.suptitle(
        constants.COMPARISON_PANEL_TITLE.format(
            linear_train=linear.train_r_squared,
            log_train=log.train_r_squared,
            linear_test=linear.test_r_squared,
            log_test=log.test_r_squared,
        ),
        fontsize=constants.PANEL_TITLE_FONT_SIZE,
        fontweight="bold",
    )
    return fig
