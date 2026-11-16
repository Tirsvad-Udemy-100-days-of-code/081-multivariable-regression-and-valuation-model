"""@brief Charts of the Day 81 analysis.

@details Every function returns a matplotlib figure and never shows it; the
caller saves it and closes it with `plt.close`.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.axes import Axes  # noqa: E402
from matplotlib.figure import Figure  # noqa: E402
from matplotlib.table import Table  # noqa: E402

from boston_valuation import constants  # noqa: E402
from boston_valuation.domain.descriptive import descriptive_statistics  # noqa: E402

_HEADER_ROW = 0
_LABEL_COLUMN = -1


def _column_groups(columns: list[str]) -> list[list[str]]:
    """@brief Split the columns into groups that fit on one table.

    @param columns Column names in file order.
    @return Consecutive groups of at most DESCRIPTIVE_COLUMNS_PER_PANEL names.
    """
    size = constants.DESCRIPTIVE_COLUMNS_PER_PANEL
    return [columns[start : start + size] for start in range(0, len(columns), size)]


def _style_cells(table: Table) -> None:
    """@brief Colour the header row and the statistic labels of a table.

    @param table The table to style.
    """
    for (row, column), cell in table.get_celld().items():
        cell.set_edgecolor(constants.DESCRIPTIVE_EDGE_COLOR)
        if row == _HEADER_ROW or column == _LABEL_COLUMN:
            cell.set_facecolor(constants.DESCRIPTIVE_HEADER_COLOR)
            cell.set_text_props(fontweight=constants.DESCRIPTIVE_HEADER_FONT_WEIGHT)


def _draw_statistics_table(ax: Axes, statistics: pd.DataFrame) -> None:
    """@brief Draw a table of statistics filling an axis.

    @param ax Axis to draw on.
    @param statistics One row per statistic and one column per data column.
    """
    ax.axis("off")
    rounded = statistics.round(constants.DESCRIPTIVE_DECIMALS)
    table = ax.table(
        cellText=[
            [f"{value:.{constants.DESCRIPTIVE_DECIMALS}f}" for value in row]
            for row in rounded.to_numpy()
        ],
        rowLabels=[str(name) for name in rounded.index],
        colLabels=[str(name) for name in rounded.columns],
        cellLoc="center",
        bbox=(0.0, 0.0, 1.0, 1.0),
    )
    table.auto_set_font_size(False)
    table.set_fontsize(constants.DESCRIPTIVE_FONT_SIZE)
    _style_cells(table)


def descriptive_table_figure(data: pd.DataFrame) -> Figure:
    """@brief Draw the descriptive statistics of every column as tables.

    @details The columns are split over stacked tables so that the numbers stay
    legible; each table has one row per statistic.

    @param data The house price table.
    @return A figure with the title and the rounded statistics. The caller
        saves and closes it.
    """
    statistics = descriptive_statistics(data)
    groups = _column_groups([str(name) for name in statistics.columns])
    fig, axes = plt.subplots(
        len(groups),
        1,
        figsize=constants.DESCRIPTIVE_FIGURE_SIZE,
        dpi=constants.PICTURE_DPI,
        squeeze=False,
    )
    fig.suptitle(
        constants.DESCRIPTIVE_TITLE,
        fontsize=constants.DESCRIPTIVE_TITLE_FONT_SIZE,
        fontweight="bold",
    )
    for ax, group in zip(axes[:, 0], groups, strict=True):
        _draw_statistics_table(ax, statistics[group])
    fig.tight_layout()
    return fig
