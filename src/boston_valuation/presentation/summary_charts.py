"""@brief Summary chart of the Day 81 analysis (step 7).

@details Every function returns a figure and never shows it; the caller saves
it and closes it with `plt.close`.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.axes import Axes  # noqa: E402
from matplotlib.figure import Figure  # noqa: E402

from boston_valuation import constants  # noqa: E402
from boston_valuation.domain import log_model  # noqa: E402
from boston_valuation.domain.log_model import FittedModel  # noqa: E402


def _draw_model_bars(
    ax: Axes,
    offset: float,
    scores: tuple[float, float],
    colour: str,
    legend: str,
) -> None:
    """@brief Draw the training and the test bar of one model.

    @param ax Axis to draw on.
    @param offset Shift of the bars from the centre of each group.
    @param scores The training and the test r-squared of the model.
    @param colour Colour of the bars.
    @param legend Legend text of the model.
    """
    positions = np.arange(len(constants.SUMMARY_GROUP_LABELS)) + offset
    bars = ax.bar(
        positions,
        scores,
        width=constants.SUMMARY_BAR_WIDTH,
        color=colour,
        label=legend,
    )
    ax.bar_label(
        bars,
        labels=[constants.SUMMARY_SCORE_FORMAT.format(value=v) for v in scores],
        padding=3,
        fontsize=constants.SUMMARY_BAR_LABEL_FONT_SIZE,
        fontweight="bold",
    )


def _scores(fitted: FittedModel) -> tuple[float, float]:
    """@brief Read the training and the test r-squared of a model.

    @param fitted The fitted model.
    @return The training r-squared and the test r-squared.
    """
    return fitted.train_r_squared, fitted.test_r_squared


def model_scores_figure(data: pd.DataFrame) -> Figure:
    """@brief Compare both models on the training data and on the test data.

    @param data The house price table.
    @return A grouped bar chart: the linear model on the price in indigo (about
        0.75 and 0.67) and the log model on the log price in navy (about 0.79
        and 0.74), each bar labelled with two decimals. The caller saves and
        closes it.
    """
    linear = log_model.fit_linear_model(data)
    log = log_model.fit_log_model(data)
    offset = constants.SUMMARY_BAR_OFFSET
    fig, ax = plt.subplots(
        figsize=constants.SUMMARY_FIGURE_SIZE,
        dpi=constants.PICTURE_DPI,
        layout="constrained",
    )
    _draw_model_bars(
        ax,
        -offset,
        _scores(linear),
        constants.COLOR_LINEAR_MODEL,
        constants.SUMMARY_LINEAR_LEGEND,
    )
    _draw_model_bars(
        ax,
        offset,
        _scores(log),
        constants.COLOR_LOG_MODEL,
        constants.SUMMARY_LOG_LEGEND,
    )
    ax.set_xticks(
        range(len(constants.SUMMARY_GROUP_LABELS)),
        constants.SUMMARY_GROUP_LABELS,
        fontsize=constants.SUMMARY_TICK_FONT_SIZE,
    )
    ax.set_ylim(*constants.SUMMARY_Y_LIMITS)
    ax.set_ylabel(constants.SUMMARY_Y_LABEL)
    ax.set_title(
        constants.SUMMARY_SUBTITLE, fontsize=constants.SUMMARY_SUBTITLE_FONT_SIZE
    )
    ax.legend(loc="upper center", ncols=constants.SUMMARY_LEGEND_COLUMNS)
    fig.suptitle(
        constants.SUMMARY_TITLE,
        fontsize=constants.SUMMARY_TITLE_FONT_SIZE,
        fontweight="bold",
    )
    return fig
