"""@brief Valuation chart of the Day 81 analysis (step 6).

@details Every function returns a figure and never shows it; the caller saves
it and closes it with `plt.close`.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.axes import Axes  # noqa: E402
from matplotlib.figure import Figure  # noqa: E402
from matplotlib.table import Table  # noqa: E402
from matplotlib.ticker import StrMethodFormatter  # noqa: E402

from boston_valuation import constants  # noqa: E402
from boston_valuation.domain import log_model, valuation  # noqa: E402
from boston_valuation.domain.valuation import ValueEstimate  # noqa: E402

_HEADER_ROW = 0


def _draw_value_bars(
    ax: Axes, average: ValueEstimate, described: ValueEstimate
) -> None:
    """@brief Draw the dollar values of the two properties as two bars.

    @param ax Axis to draw on.
    @param average The estimate of the average property.
    @param described The estimate of the described property.
    """
    dollars = [average.dollar_estimate, described.dollar_estimate]
    bars = ax.bar(
        [constants.AVERAGE_PROPERTY_LABEL, constants.DESCRIBED_PROPERTY_LABEL],
        dollars,
        width=constants.VALUATION_BAR_WIDTH,
        color=constants.COLOR_LOG_MODEL,
    )
    ax.bar_label(
        bars,
        labels=[constants.VALUATION_DOLLAR_FORMAT.format(value=v) for v in dollars],
        padding=3,
        fontsize=constants.VALUATION_BAR_LABEL_FONT_SIZE,
        fontweight="bold",
    )
    ax.set_ylim(0, max(dollars) * constants.VALUATION_BAR_HEADROOM)
    ax.yaxis.set_major_formatter(StrMethodFormatter(constants.VALUATION_AXIS_FORMAT))
    ax.set_title(constants.VALUATION_BARS_TITLE)
    ax.set_ylabel(constants.VALUATION_BARS_Y_LABEL)


def _style_cells(table: Table) -> None:
    """@brief Colour the header row and the feature column of a table.

    @param table The table to style.
    """
    for (row, column), cell in table.get_celld().items():
        cell.set_edgecolor(constants.DESCRIPTIVE_EDGE_COLOR)
        if row == _HEADER_ROW or column == 0:
            cell.set_facecolor(constants.DESCRIPTIVE_HEADER_COLOR)
            cell.set_text_props(fontweight=constants.DESCRIPTIVE_HEADER_FONT_WEIGHT)


def _draw_characteristics_table(ax: Axes, characteristics: pd.DataFrame) -> None:
    """@brief Draw the characteristics of the two properties as a table.

    @param ax Axis to draw on.
    @param characteristics The table of ::valuation.property_characteristics.
    """
    decimals = constants.VALUATION_TABLE_DECIMALS
    rows = [
        [label, *(f"{value:.{decimals}f}" for value in values)]
        for label, values in zip(
            constants.VALUATION_FEATURE_LABELS,
            characteristics.to_numpy(),
            strict=True,
        )
    ]
    ax.axis("off")
    table = ax.table(
        cellText=rows,
        colLabels=[constants.FEATURE_COLUMN_LABEL, *characteristics.columns],
        colWidths=list(constants.VALUATION_TABLE_COLUMN_WIDTHS),
        cellLoc="center",
        bbox=(0.0, 0.0, 1.0, 1.0),
    )
    table.auto_set_font_size(False)
    table.set_fontsize(constants.VALUATION_TABLE_FONT_SIZE)
    _style_cells(table)
    ax.set_title(constants.VALUATION_TABLE_TITLE)


def valuation_figure(data: pd.DataFrame) -> Figure:
    """@brief Compare the value of the average and the described property.

    @param data The house price table.
    @return A figure with a bar chart of the two dollar estimates (about
        $20,703 and $25,792) on the left and a table of the six characteristics
        that change on the right. The title carries the log estimates, 3.03 and
        3.25. The caller saves and closes it.
    """
    model = log_model.fit_log_model(data).model
    average = valuation.average_property(data)
    described = valuation.described_property(data)
    average_estimate = valuation.estimate_value(model, average)
    described_estimate = valuation.estimate_value(model, described)
    fig, (bars_ax, table_ax) = plt.subplots(
        1,
        2,
        figsize=constants.VALUATION_PANEL_FIGURE_SIZE,
        dpi=constants.PICTURE_DPI,
        gridspec_kw={"width_ratios": list(constants.VALUATION_PANEL_WIDTH_RATIOS)},
        layout="constrained",
    )
    _draw_value_bars(bars_ax, average_estimate, described_estimate)
    _draw_characteristics_table(
        table_ax, valuation.property_characteristics(average, described)
    )
    fig.suptitle(
        constants.VALUATION_PANEL_TITLE.format(
            average_log=average_estimate.log_estimate,
            described_log=described_estimate.log_estimate,
        ),
        fontsize=constants.VALUATION_PANEL_TITLE_FONT_SIZE,
        fontweight="bold",
    )
    return fig
