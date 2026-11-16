"""@brief Tests for the valuation chart of step 6."""

from collections.abc import Iterator

import matplotlib.pyplot as plt
import pandas as pd
import pytest
from matplotlib.axes import Axes
from matplotlib.colors import to_rgb
from matplotlib.figure import Figure
from matplotlib.table import Table

from boston_valuation import constants
from boston_valuation.presentation import valuation_charts

NAVY = to_rgb(constants.COLOR_LOG_MODEL)
TABLE_ROWS = 7
TABLE_COLUMNS = 3


@pytest.fixture(scope="module")
def figure(boston_data: pd.DataFrame) -> Iterator[Figure]:
    """@brief Draw the valuation figure once for several tests.

    @param boston_data The real table.
    @return The figure, closed after the last test of the module.
    """
    fig = valuation_charts.valuation_figure(boston_data)
    yield fig
    plt.close(fig)


def _table(ax: Axes) -> Table:
    """@brief Return the table of an axis.

    @param ax An axis with one table.
    @return Its table.
    """
    assert len(ax.tables) == 1
    return ax.tables[0]


def test_figure_has_a_bar_chart_and_a_table(figure: Figure) -> None:
    """@brief Two panels: the bars on the left and the table on the right."""
    bars_ax, table_ax = figure.axes
    assert len(bars_ax.patches) == 2
    assert len(table_ax.tables) == 1


def test_bars_show_the_two_dollar_estimates(figure: Figure) -> None:
    """@brief The bars are about $20,703 and $25,792 high."""
    heights = [bar.get_height() for bar in figure.axes[0].patches]
    assert heights == pytest.approx([20_703, 25_792], abs=10)


def test_bars_are_navy(figure: Figure) -> None:
    """@brief Both bars use the colour of the log model."""
    for bar in figure.axes[0].patches:
        assert tuple(bar.get_facecolor()[:3]) == pytest.approx(NAVY)


def test_bars_carry_the_dollar_values_as_labels(figure: Figure) -> None:
    """@brief The labels read `$20,703` and `$25,792`."""
    labels = [text.get_text() for text in figure.axes[0].texts]
    assert labels == ["$20,703", "$25,792"]


def test_bars_are_named_after_the_two_properties(figure: Figure) -> None:
    """@brief The ticks name the average and the described property."""
    ticks = [tick.get_text() for tick in figure.axes[0].get_xticklabels()]
    assert ticks == [
        constants.AVERAGE_PROPERTY_LABEL,
        constants.DESCRIBED_PROPERTY_LABEL,
    ]


def test_y_axis_is_in_dollars_with_thousands_separators(figure: Figure) -> None:
    """@brief The ticks read like `$25,000`."""
    ax = figure.axes[0]
    ax.figure.canvas.draw()
    texts = [tick.get_text() for tick in ax.get_yticklabels()]
    assert "$25,000" in texts
    assert ax.get_ylabel() == constants.VALUATION_BARS_Y_LABEL
    assert ax.get_title() == constants.VALUATION_BARS_TITLE


def test_y_axis_leaves_room_for_the_labels(figure: Figure) -> None:
    """@brief The tallest bar is below the top of the axis."""
    ax = figure.axes[0]
    top = max(bar.get_height() for bar in ax.patches)
    assert ax.get_ylim()[1] > top
    assert ax.get_ylim()[0] == 0


def test_title_carries_the_two_log_estimates(figure: Figure) -> None:
    """@brief The title states 3.03 and 3.25."""
    title = figure.get_suptitle()
    assert "3.03" in title
    assert "3.25" in title


def test_table_compares_the_six_characteristics(figure: Figure) -> None:
    """@brief A header and six rows of three columns."""
    cells = _table(figure.axes[1]).get_celld()
    assert max(row for row, _ in cells) + 1 == TABLE_ROWS
    assert max(column for _, column in cells) + 1 == TABLE_COLUMNS


def test_table_shows_the_average_and_described_values(figure: Figure) -> None:
    """@brief RM 6.28 vs 8.00, CHAS 0.07 vs 1.00 and so on."""
    cells = _table(figure.axes[1]).get_celld()
    rows = [
        [cells[row, column].get_text().get_text() for column in range(TABLE_COLUMNS)]
        for row in range(1, TABLE_ROWS)
    ]
    assert rows == [
        ["RM (rooms)", "6.28", "8.00"],
        ["PTRATIO (students per teacher)", "18.46", "20.00"],
        ["DIS (distance to town)", "3.80", "5.00"],
        ["CHAS (next to river)", "0.07", "1.00"],
        ["NOX (pollution)", "0.55", "0.62"],
        ["LSTAT (poverty)", "12.65", "6.95"],
    ]


def test_table_header_names_the_two_properties(figure: Figure) -> None:
    """@brief The header row has the feature column and both properties."""
    cells = _table(figure.axes[1]).get_celld()
    header = [cells[0, column].get_text().get_text() for column in range(3)]
    assert header == [
        constants.FEATURE_COLUMN_LABEL,
        constants.AVERAGE_PROPERTY_LABEL,
        constants.DESCRIBED_PROPERTY_LABEL,
    ]


def test_figure_uses_the_picture_resolution_and_size(figure: Figure) -> None:
    """@brief The figure has the size and dpi set in the constants."""
    assert figure.dpi == constants.PICTURE_DPI
    assert tuple(figure.get_size_inches()) == pytest.approx(
        constants.VALUATION_PANEL_FIGURE_SIZE
    )
