"""@brief Distribution charts of the Day 81 analysis (step 2).

@details Every function returns a figure and never shows it; the caller saves
it and closes it with `plt.close`. The price, distance and rooms charts are
Seaborn `displot` histograms with a Kernel Density Estimate (KDE), the highway
chart is a Matplotlib histogram and the river chart is a Plotly bar chart.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import plotly.express as px  # noqa: E402
import plotly.graph_objects as go  # noqa: E402
import seaborn as sns  # noqa: E402
from matplotlib.axes import Axes  # noqa: E402
from matplotlib.figure import Figure  # noqa: E402

from boston_valuation import constants  # noqa: E402
from boston_valuation.domain.distributions import (  # noqa: E402
    distance_title,
    price_title,
    river_counts_by_label,
    rooms_title,
)


def _distribution_figure(
    values: pd.Series,
    color: str,
    title: str,
    x_label: str,
    bins: int | str,
) -> Figure:
    """@brief Draw a histogram with a KDE as a Seaborn displot.

    @param values The numbers to count.
    @param color Colour of the bars and the curve.
    @param title Title of the chart.
    @param x_label Label of the horizontal axis.
    @param bins Number of bins, or `auto` to let Seaborn choose.
    @return The figure of the facet grid. The caller saves and closes it.
    """
    grid = sns.displot(
        values,
        bins=bins,
        aspect=constants.DISPLOT_ASPECT,
        kde=True,
        color=color,
    )
    grid.set_axis_labels(x_label, constants.HOMES_Y_LABEL)
    grid.axes[0, 0].set_title(title)
    return grid.figure


def price_distribution_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the distribution of the home prices.

    @param data The house price table.
    @return A histogram of PRICE with a KDE, with the average in the title. The
        caller saves and closes it.
    """
    return _distribution_figure(
        data[constants.COL_PRICE],
        constants.COLOR_PRICE,
        price_title(data),
        constants.PRICE_X_LABEL,
        constants.PRICE_BINS,
    )


def distance_distribution_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the distribution of the distance to the employment centres.

    @param data The house price table.
    @return A histogram of DIS with a KDE, with the average in the title. The
        caller saves and closes it.
    """
    return _distribution_figure(
        data[constants.COL_DIS],
        constants.COLOR_DIS,
        distance_title(data),
        constants.DISTANCE_X_LABEL,
        constants.DISTANCE_BINS,
    )


def rooms_distribution_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the distribution of the number of rooms.

    @details The bins are chosen by Seaborn, as the course does.

    @param data The house price table.
    @return A histogram of RM with a KDE, with the average in the title. The
        caller saves and closes it.
    """
    return _distribution_figure(
        data[constants.COL_RM],
        constants.COLOR_RM,
        rooms_title(data),
        constants.ROOMS_X_LABEL,
        "auto",
    )


def _draw_highway_histogram(ax: Axes, data: pd.DataFrame) -> None:
    """@brief Draw the histogram of RAD on an axis.

    @param ax Axis to draw on.
    @param data The house price table.
    """
    ax.hist(
        data[constants.COL_RAD],
        bins=constants.RAD_BINS,
        ec=constants.RAD_EDGE_COLOR,
        color=constants.COLOR_RAD,
        rwidth=constants.RAD_BAR_WIDTH,
    )
    ax.set_xlabel(constants.RAD_X_LABEL)
    ax.set_ylabel(constants.RAD_Y_LABEL)


def highway_access_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the distribution of the highway accessibility index.

    @param data The house price table.
    @return A Matplotlib histogram of RAD with 24 bins, black edges and purple
        bars of half width. The caller saves and closes it.
    """
    fig, ax = plt.subplots(
        figsize=constants.HISTOGRAM_FIGURE_SIZE, dpi=constants.HISTOGRAM_DPI
    )
    _draw_highway_histogram(ax, data)
    return fig


def river_bar_chart(data: pd.DataFrame) -> go.Figure:
    """@brief Draw how many homes are and are not next to the Charles River.

    @param data The house price table.
    @return A Plotly bar chart with the categories `No` and `Yes`, coloured by
        count on the haline scale without a colour axis. The caller shows or
        saves it.
    """
    counts = river_counts_by_label(data)
    values = [int(value) for value in counts]
    bar = px.bar(
        x=list(counts.index),
        y=values,
        color=values,
        color_continuous_scale=constants.RIVER_COLOR_SCALE,
        title=constants.RIVER_TITLE,
    )
    bar.update_layout(
        xaxis_title=constants.RIVER_X_LABEL,
        yaxis_title=constants.RIVER_Y_LABEL,
        coloraxis_showscale=False,
    )
    return bar


def _draw_kde_histogram(
    ax: Axes, values: pd.Series, color: str, title: str, bins: int | str
) -> None:
    """@brief Draw a histogram with a KDE on an axis.

    @param ax Axis to draw on.
    @param values The numbers to count.
    @param color Colour of the bars and the curve.
    @param title Title of the axis.
    @param bins Number of bins, or `auto` to let Seaborn choose.
    """
    sns.histplot(values, bins=bins, kde=True, color=color, ax=ax)
    ax.set_title(title, fontsize=constants.PANEL_AXES_TITLE_FONT_SIZE)
    ax.set_ylabel(constants.HOMES_Y_LABEL)


def distribution_panel_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the price, distance, rooms and highway charts in one figure.

    @details The Seaborn `displot` makes its own figure, so the panel draws the
    same histograms, colours, bins and titles on shared axes.

    @param data The house price table.
    @return A figure of two rows and two columns. The caller saves and closes
        it.
    """
    fig, axes = plt.subplots(
        constants.PANEL_ROWS,
        constants.PANEL_COLUMNS,
        figsize=constants.PANEL_FIGURE_SIZE,
        dpi=constants.PICTURE_DPI,
    )
    price_ax, distance_ax, rooms_ax, highway_ax = axes.ravel()
    _draw_kde_histogram(
        price_ax,
        data[constants.COL_PRICE],
        constants.COLOR_PRICE,
        price_title(data),
        constants.PRICE_BINS,
    )
    price_ax.set_xlabel(constants.PRICE_X_LABEL)
    _draw_kde_histogram(
        distance_ax,
        data[constants.COL_DIS],
        constants.COLOR_DIS,
        distance_title(data),
        constants.DISTANCE_BINS,
    )
    distance_ax.set_xlabel(constants.DISTANCE_X_LABEL)
    _draw_kde_histogram(
        rooms_ax,
        data[constants.COL_RM],
        constants.COLOR_RM,
        rooms_title(data),
        "auto",
    )
    rooms_ax.set_xlabel(constants.ROOMS_X_LABEL)
    _draw_highway_histogram(highway_ax, data)
    highway_ax.set_title(
        constants.RAD_TITLE, fontsize=constants.PANEL_AXES_TITLE_FONT_SIZE
    )
    fig.suptitle(
        constants.PANEL_TITLE,
        fontsize=constants.PANEL_TITLE_FONT_SIZE,
        fontweight="bold",
    )
    fig.tight_layout()
    return fig
