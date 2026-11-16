"""@brief Regression and residual charts of the Day 81 analysis (step 4).

@details Every function returns a figure and never shows it; the caller saves
it and closes it with `plt.close`. The charts take the actual values, the
predictions or the residuals, so the log model reuses them with its own colour
and text.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
import seaborn as sns  # noqa: E402
from matplotlib.axes import Axes  # noqa: E402
from matplotlib.figure import Figure  # noqa: E402
from numpy.typing import NDArray  # noqa: E402

from boston_valuation import constants  # noqa: E402
from boston_valuation.domain.regression import (  # noqa: E402
    coefficient_table,
    fit_linear_regression,
    predictions,
    r_squared,
    residual_mean,
    residual_skew,
    residuals,
    room_premium,
    split_features_and_target,
    split_train_test,
)


def single_axes() -> tuple[Figure, Axes]:
    """@brief Make a figure with one axis in the size of a lecture chart.

    @return The figure and its axis.
    """
    return plt.subplots(
        figsize=constants.REGRESSION_FIGURE_SIZE, dpi=constants.REGRESSION_DPI
    )


def _label_axes(
    ax: Axes, title: str, x_label: str, y_label: str, title_size: int, label_size: int
) -> None:
    """@brief Set the title and the axis labels of a chart.

    @param ax Axis to label.
    @param title Title of the chart.
    @param x_label Label of the horizontal axis.
    @param y_label Label of the vertical axis.
    @param title_size Font size of the title.
    @param label_size Font size of the axis labels.
    """
    ax.set_title(title, fontsize=title_size)
    ax.set_xlabel(x_label, fontsize=label_size)
    ax.set_ylabel(y_label, fontsize=label_size)


def draw_actual_vs_predicted(
    ax: Axes,
    actual: pd.Series,
    predicted: NDArray[np.float64],
    colour: str,
    title: str,
    x_label: str,
    y_label: str,
    title_size: int,
    label_size: int,
) -> None:
    """@brief Draw the predictions against the actual values on an axis.

    @details A perfect model puts every dot on the cyan line `y = x`.

    @param ax Axis to draw on.
    @param actual The actual values.
    @param predicted The predicted values of the same rows.
    @param colour Colour of the dots.
    @param title Title of the chart.
    @param x_label Label of the horizontal axis.
    @param y_label Label of the vertical axis.
    @param title_size Font size of the title.
    @param label_size Font size of the axis labels.
    """
    ax.scatter(actual, predicted, c=colour, alpha=constants.RESIDUAL_ALPHA)
    ax.plot(actual, actual, color=constants.COLOR_IDENTITY_LINE)
    _label_axes(ax, title, x_label, y_label, title_size, label_size)


def draw_residuals_vs_predicted(
    ax: Axes,
    predicted: NDArray[np.float64],
    errors: pd.Series,
    colour: str,
    title_size: int,
    label_size: int,
    title: str = constants.RESIDUALS_VS_PREDICTED_TITLE,
    x_label: str = constants.PREDICTED_PRICE_X_LABEL,
) -> None:
    """@brief Draw the residuals against the predictions on an axis.

    @param ax Axis to draw on.
    @param predicted The predicted values.
    @param errors The residuals of the same rows.
    @param colour Colour of the dots.
    @param title_size Font size of the title.
    @param label_size Font size of the axis labels.
    @param title Title of the chart.
    @param x_label Label of the horizontal axis.
    """
    ax.scatter(predicted, errors, c=colour, alpha=constants.RESIDUAL_ALPHA)
    _label_axes(ax, title, x_label, constants.RESIDUALS_LABEL, title_size, label_size)


def residual_distribution_title(errors: pd.Series, title_prefix: str = "") -> str:
    """@brief Write the title that reports the skew and the mean of residuals.

    @param errors The residuals.
    @param title_prefix Text before the title, such as `Log price model: `.
    @return For example `Residuals Skew (1.46) Mean (-0.0)`; both figures are
        rounded to two decimals.
    """
    return constants.RESIDUAL_DISTRIBUTION_TITLE.format(
        prefix=title_prefix,
        skew=round(residual_skew(errors), constants.RESIDUAL_DECIMALS),
        mean=round(residual_mean(errors), constants.RESIDUAL_DECIMALS),
    )


def draw_residual_distribution(
    ax: Axes,
    errors: pd.Series,
    colour: str,
    title_prefix: str,
    title_size: int,
    label_size: int,
) -> None:
    """@brief Draw a histogram with a KDE of the residuals on an axis.

    @param ax Axis to draw on.
    @param errors The residuals.
    @param colour Colour of the bars and the curve.
    @param title_prefix Text before the title.
    @param title_size Font size of the title.
    @param label_size Font size of the axis labels.
    """
    sns.histplot(errors, kde=True, color=colour, ax=ax)
    _label_axes(
        ax,
        residual_distribution_title(errors, title_prefix),
        constants.RESIDUALS_LABEL,
        constants.RESIDUAL_COUNT_LABEL,
        title_size,
        label_size,
    )


def actual_vs_predicted_figure(
    actual: pd.Series,
    predicted: NDArray[np.float64],
    colour: str = constants.COLOR_LINEAR_MODEL,
    title: str = constants.ACTUAL_VS_PREDICTED_TITLE,
    x_label: str = constants.ACTUAL_PRICE_X_LABEL,
    y_label: str = constants.PREDICTED_PRICE_Y_LABEL,
) -> Figure:
    """@brief Draw the predicted values against the actual values.

    @param actual The actual values.
    @param predicted The predicted values of the same rows.
    @param colour Colour of the dots.
    @param title Title of the chart.
    @param x_label Label of the horizontal axis.
    @param y_label Label of the vertical axis.
    @return A half transparent scatter plot with a cyan line `y = x`. The
        caller saves and closes it.
    """
    fig, ax = single_axes()
    draw_actual_vs_predicted(
        ax,
        actual,
        predicted,
        colour,
        title,
        x_label,
        y_label,
        constants.REGRESSION_TITLE_FONT_SIZE,
        constants.REGRESSION_LABEL_FONT_SIZE,
    )
    return fig


def residuals_vs_predicted_figure(
    predicted: NDArray[np.float64],
    errors: pd.Series,
    colour: str = constants.COLOR_LINEAR_MODEL,
    title: str = constants.RESIDUALS_VS_PREDICTED_TITLE,
    x_label: str = constants.PREDICTED_PRICE_X_LABEL,
) -> Figure:
    """@brief Draw the residuals against the predicted values.

    @param predicted The predicted values.
    @param errors The residuals of the same rows.
    @param colour Colour of the dots.
    @param title Title of the chart.
    @param x_label Label of the horizontal axis.
    @return A half transparent scatter plot. The caller saves and closes it.
    """
    fig, ax = single_axes()
    draw_residuals_vs_predicted(
        ax,
        predicted,
        errors,
        colour,
        constants.REGRESSION_TITLE_FONT_SIZE,
        constants.REGRESSION_LABEL_FONT_SIZE,
        title,
        x_label,
    )
    return fig


def residual_distribution_figure(
    errors: pd.Series,
    colour: str = constants.COLOR_LINEAR_MODEL,
    title_prefix: str = "",
) -> Figure:
    """@brief Draw the distribution of the residuals.

    @param errors The residuals.
    @param colour Colour of the bars and the curve.
    @param title_prefix Text before the title, such as `Original model: `.
    @return A histogram with a KDE whose title carries the skew and the mean.
        The caller saves and closes it.
    """
    fig, ax = single_axes()
    draw_residual_distribution(
        ax,
        errors,
        colour,
        title_prefix,
        constants.REGRESSION_LABEL_FONT_SIZE,
        constants.REGRESSION_LABEL_FONT_SIZE,
    )
    return fig


def regression_panel_figure(data: pd.DataFrame) -> Figure:
    """@brief Fit the linear model and draw its three charts in one figure.

    @details The model is fitted on the training rows of an 80/20 split. The
    Seaborn and Matplotlib charts of the lectures make their own figures, so
    the panel draws the same charts on shared axes, with smaller text.

    @param data The house price table.
    @return A figure of one row and three columns: actual against predicted,
        residuals against predicted and the residual distribution, with the
        training r-squared and the room premium in the title. The caller saves
        and closes it.
    """
    features, target = split_features_and_target(data)
    split = split_train_test(features, target)
    model = fit_linear_regression(split.x_train, split.y_train)
    predicted = predictions(model, split.x_train)
    errors = residuals(split.y_train, predicted)
    size = constants.PANEL_AXES_TITLE_FONT_SIZE
    fig, axes = plt.subplots(
        1,
        constants.REGRESSION_PANEL_COLUMNS,
        figsize=constants.REGRESSION_PANEL_FIGURE_SIZE,
        dpi=constants.PICTURE_DPI,
    )
    actual_ax, residual_ax, distribution_ax = axes.ravel()
    draw_actual_vs_predicted(
        actual_ax,
        split.y_train,
        predicted,
        constants.COLOR_LINEAR_MODEL,
        constants.ACTUAL_VS_PREDICTED_TITLE,
        constants.ACTUAL_PRICE_X_LABEL,
        constants.PREDICTED_PRICE_Y_LABEL,
        size,
        size,
    )
    draw_residuals_vs_predicted(
        residual_ax, predicted, errors, constants.COLOR_LINEAR_MODEL, size, size
    )
    draw_residual_distribution(
        distribution_ax, errors, constants.COLOR_LINEAR_MODEL, "", size, size
    )
    fig.suptitle(
        constants.REGRESSION_PANEL_TITLE.format(
            r_squared=r_squared(model, split.x_train, split.y_train),
            premium=room_premium(coefficient_table(model, split.x_train.columns)),
        ),
        fontsize=constants.PANEL_TITLE_FONT_SIZE,
        fontweight="bold",
    )
    fig.tight_layout()
    return fig
