"""@brief Relationship charts of the Day 81 analysis (step 3).

@details Every function returns a figure and never shows it; the caller saves
it and closes it with `plt.close`. The pair plot and the five joint plots are
Seaborn charts; the panel for the README draws the same pairs on shared axes.
"""

from collections.abc import Sequence

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import seaborn as sns  # noqa: E402
from matplotlib.axes import Axes  # noqa: E402
from matplotlib.figure import Figure  # noqa: E402

from boston_valuation import constants  # noqa: E402
from boston_valuation.domain.relationships import (  # noqa: E402
    correlation,
    correlation_with_price,
)


def pair_plot_figure(
    data: pd.DataFrame,
    columns: Sequence[str] | None = None,
    regression_line: bool = False,
) -> Figure:
    """@brief Draw a Seaborn pair plot of the columns.

    @details The grid holds a scatter plot for every pair of columns and a
    histogram of each column on the diagonal. Drawing all 14 columns takes
    one to two minutes, so a subset can be chosen.

    @param data The house price table.
    @param columns The columns to draw; every column when omitted.
    @param regression_line Draw a cyan regression line in every scatter plot.
    @return The figure of the grid. The caller saves and closes it.
    """
    table = data if columns is None else data[list(columns)]
    if regression_line:
        grid = sns.pairplot(
            table,
            kind="reg",
            plot_kws={"line_kws": {"color": constants.PAIR_REGRESSION_LINE_COLOR}},
        )
    else:
        grid = sns.pairplot(table)
    return grid.figure


def joint_plot_figure(
    data: pd.DataFrame,
    x: str,
    y: str,
    colour: str,
    height: float,
    style: str = constants.JOINT_STYLE_DARK,
) -> Figure:
    """@brief Draw a Seaborn joint plot of two columns.

    @details The scatter plot is half transparent so that overlapping homes
    show up darker.

    @param data The house price table.
    @param x Column on the horizontal axis.
    @param y Column on the vertical axis.
    @param colour Colour of the dots and the histograms.
    @param height Height and width of the figure, in inches.
    @param style Seaborn axes style, such as `darkgrid` or `whitegrid`.
    @return The figure of the joint grid. The caller saves and closes it.
    """
    with sns.axes_style(style):
        grid = sns.jointplot(
            x=data[x],
            y=data[y],
            height=height,
            kind=constants.JOINT_KIND,
            color=colour,
            joint_kws={"alpha": constants.JOINT_ALPHA},
        )
    return grid.figure


def distance_pollution_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the distance to employment against the pollution.

    @param data The house price table.
    @return A joint plot of DIS and NOX in deep pink. The caller saves and
        closes it.
    """
    x, y = constants.PAIR_DISTANCE_POLLUTION
    return joint_plot_figure(
        data, x, y, constants.JOINT_COLOR_DIS, constants.JOINT_HEIGHT
    )


def pollution_industry_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the pollution against the share of industry.

    @param data The house price table.
    @return A joint plot of NOX and INDUS in dark green. The caller saves and
        closes it.
    """
    x, y = constants.PAIR_POLLUTION_INDUSTRY
    return joint_plot_figure(
        data, x, y, constants.JOINT_COLOR_NOX, constants.JOINT_HEIGHT_SMALL
    )


def poverty_rooms_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the poverty against the number of rooms.

    @param data The house price table.
    @return A joint plot of LSTAT and RM in orange. The caller saves and closes
        it.
    """
    x, y = constants.PAIR_POVERTY_ROOMS
    return joint_plot_figure(
        data, x, y, constants.JOINT_COLOR_RM, constants.JOINT_HEIGHT_SMALL
    )


def poverty_price_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the poverty against the home price.

    @param data The house price table.
    @return A joint plot of LSTAT and PRICE in crimson. The caller saves and
        closes it.
    """
    x, y = constants.PAIR_POVERTY_PRICE
    return joint_plot_figure(
        data, x, y, constants.JOINT_COLOR_LSTAT, constants.JOINT_HEIGHT_SMALL
    )


def rooms_price_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the number of rooms against the home price.

    @param data The house price table.
    @return A joint plot of RM and PRICE in dark blue on a white grid. The
        caller saves and closes it.
    """
    x, y = constants.PAIR_ROOMS_PRICE
    return joint_plot_figure(
        data,
        x,
        y,
        constants.JOINT_COLOR_RM_PRICE,
        constants.JOINT_HEIGHT_SMALL,
        constants.JOINT_STYLE_LIGHT,
    )


def _draw_pair_scatter(
    ax: Axes, data: pd.DataFrame, pair: tuple[str, str], colour: str
) -> None:
    """@brief Draw one relationship as a scatter plot with its coefficient.

    @param ax Axis to draw on.
    @param data The house price table.
    @param pair The columns of the horizontal and the vertical axis.
    @param colour Colour of the dots.
    """
    first, second = pair
    ax.scatter(
        data[first],
        data[second],
        s=constants.RELATIONSHIP_SCATTER_SIZE,
        color=colour,
        alpha=constants.JOINT_ALPHA,
    )
    ax.set_xlabel(first)
    ax.set_ylabel(second)
    ax.set_title(
        constants.RELATIONSHIP_PAIR_TITLE.format(
            first=first, second=second, value=correlation(data, first, second)
        ),
        fontsize=constants.PANEL_AXES_TITLE_FONT_SIZE,
    )


def _draw_price_correlations(ax: Axes, data: pd.DataFrame) -> None:
    """@brief Draw the correlation of every feature with the price as bars.

    @param ax Axis to draw on.
    @param data The house price table.
    """
    coefficients = correlation_with_price(data)
    colours = [
        constants.CORRELATION_COLOR_POSITIVE
        if value >= 0
        else constants.CORRELATION_COLOR_NEGATIVE
        for value in coefficients
    ]
    ax.barh(list(coefficients.index), coefficients.to_numpy(), color=colours)
    ax.invert_yaxis()
    ax.axvline(
        0,
        color=constants.CORRELATION_ZERO_LINE_COLOR,
        linewidth=constants.CORRELATION_ZERO_LINE_WIDTH,
    )
    ax.set_xlim(-constants.CORRELATION_AXIS_LIMIT, constants.CORRELATION_AXIS_LIMIT)
    ax.set_xlabel(constants.CORRELATION_BARS_X_LABEL)
    ax.set_title(
        constants.CORRELATION_BARS_TITLE,
        fontsize=constants.PANEL_AXES_TITLE_FONT_SIZE,
    )


def relationship_panel_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the five relationships and the price correlations in one figure.

    @details The Seaborn joint plots make their own figures, so the panel draws
    the same pairs, colours and opacity on shared axes, with the correlation
    coefficient in each title, and a bar chart of every feature's correlation
    with the price.

    @param data The house price table.
    @return A figure of two rows and three columns. The caller saves and closes
        it.
    """
    fig, axes = plt.subplots(
        constants.RELATIONSHIP_PANEL_ROWS,
        constants.RELATIONSHIP_PANEL_COLUMNS,
        figsize=constants.RELATIONSHIP_PANEL_FIGURE_SIZE,
        dpi=constants.PICTURE_DPI,
    )
    cells = list(axes.ravel())
    for ax, pair, colour in zip(
        cells, constants.RELATIONSHIP_PAIRS, constants.RELATIONSHIP_COLORS, strict=False
    ):
        _draw_pair_scatter(ax, data, pair, colour)
    _draw_price_correlations(ax=cells[-1], data=data)
    fig.suptitle(
        constants.RELATIONSHIP_PANEL_TITLE,
        fontsize=constants.PANEL_TITLE_FONT_SIZE,
        fontweight="bold",
    )
    fig.tight_layout()
    return fig
