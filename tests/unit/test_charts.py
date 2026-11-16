"""@brief Tests for the charts."""

from collections.abc import Iterator

import matplotlib.pyplot as plt
import pandas as pd
import pytest
from matplotlib.figure import Figure

from boston_valuation import constants
from boston_valuation.presentation import charts


@pytest.fixture
def table_figure(boston_data: pd.DataFrame) -> Iterator[Figure]:
    """@brief Draw the descriptive table and close it afterwards.

    @param boston_data The real table.
    @return The figure of the descriptive statistics.
    """
    fig = charts.descriptive_table_figure(boston_data)
    yield fig
    plt.close(fig)


def _tables(fig: Figure) -> list[dict[tuple[int, int], str]]:
    """@brief Read the text of every cell of every table in a figure.

    @param fig The figure to read.
    @return One mapping of (row, column) to text per table.
    """
    return [
        {
            key: cell.get_text().get_text()
            for key, cell in ax.tables[0].get_celld().items()
        }
        for ax in fig.axes
    ]


def _header_labels(fig: Figure) -> list[str]:
    """@brief Collect the column labels of every table, left to right.

    @param fig The figure to read.
    @return The header texts, top table first.
    """
    return [
        text
        for cells in _tables(fig)
        for (row, column), text in sorted(cells.items())
        if row == 0 and column >= 0
    ]


def test_descriptive_table_figure_has_title(table_figure: Figure) -> None:
    """@brief The figure carries the title of the picture."""
    assert table_figure.get_suptitle() == (
        "Descriptive statistics of the Boston house price data"
    )


def test_descriptive_table_figure_has_one_table_per_axis(
    table_figure: Figure,
) -> None:
    """@brief Every axis holds one table."""
    assert all(len(ax.tables) == 1 for ax in table_figure.axes)


def test_descriptive_table_figure_shows_every_column(table_figure: Figure) -> None:
    """@brief All fourteen columns are shown, in file order."""
    assert tuple(_header_labels(table_figure)) == constants.ALL_COLUMNS


def test_descriptive_table_figure_splits_columns_over_two_tables(
    table_figure: Figure,
) -> None:
    """@brief Fourteen columns in groups of seven give two tables."""
    assert len(table_figure.axes) == 2


def test_descriptive_table_figure_shows_every_statistic_row(
    table_figure: Figure,
) -> None:
    """@brief Each table lists the eight statistics as row labels."""
    labels = [
        [text for (row, column), text in sorted(cells.items()) if column == -1 and row]
        for cells in _tables(table_figure)
    ]
    expected = ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]
    assert labels == [expected, expected]


def test_descriptive_table_figure_rounds_to_two_decimals(
    table_figure: Figure,
) -> None:
    """@brief The mean of PRICE is shown as 22.53."""
    cells = _tables(table_figure)[1]
    price_column = next(k[1] for k, text in cells.items() if text == "PRICE")
    assert cells[(2, price_column)] == "22.53"


def test_descriptive_table_figure_does_not_change_data(
    boston_data: pd.DataFrame,
) -> None:
    """@brief Drawing leaves the table as it was."""
    before = boston_data.copy()
    plt.close(charts.descriptive_table_figure(boston_data))
    pd.testing.assert_frame_equal(boston_data, before)
