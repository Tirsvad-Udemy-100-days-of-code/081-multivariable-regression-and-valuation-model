"""@brief Tests for the distribution charts."""

from collections.abc import Iterator

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import pytest
from matplotlib.colors import to_rgb
from matplotlib.figure import Figure
from plotly.graph_objects import Figure as PlotlyFigure

from boston_valuation import constants
from boston_valuation.presentation import distribution_charts as charts

PRICE_BIN_COUNT = 50
ASPECT_RATIO = 2.0
RIVER_COUNTS = (471, 35)


def _bars(fig: Figure) -> list[float]:
    """@brief Collect the widths of the bars of the first axis.

    @param fig The figure to read.
    @return One width per bar.
    """
    return [bar.get_width() for bar in fig.axes[0].patches]


def _line_color(fig: Figure) -> tuple[float, float, float]:
    """@brief Read the colour of the KDE curve of the first axis.

    @param fig The figure to read.
    @return The curve colour as red, green and blue.
    """
    return to_rgb(fig.axes[0].lines[0].get_color())


@pytest.fixture
def price_figure(boston_data: pd.DataFrame) -> Iterator[Figure]:
    """@brief Draw the price chart and close it afterwards.

    @param boston_data The real table.
    @return The price figure.
    """
    fig = charts.price_distribution_figure(boston_data)
    yield fig
    plt.close(fig)


@pytest.fixture
def distance_figure(boston_data: pd.DataFrame) -> Iterator[Figure]:
    """@brief Draw the distance chart and close it afterwards.

    @param boston_data The real table.
    @return The distance figure.
    """
    fig = charts.distance_distribution_figure(boston_data)
    yield fig
    plt.close(fig)


@pytest.fixture
def rooms_figure(boston_data: pd.DataFrame) -> Iterator[Figure]:
    """@brief Draw the rooms chart and close it afterwards.

    @param boston_data The real table.
    @return The rooms figure.
    """
    fig = charts.rooms_distribution_figure(boston_data)
    yield fig
    plt.close(fig)


@pytest.fixture
def highway_figure(boston_data: pd.DataFrame) -> Iterator[Figure]:
    """@brief Draw the highway chart and close it afterwards.

    @param boston_data The real table.
    @return The highway figure.
    """
    fig = charts.highway_access_figure(boston_data)
    yield fig
    plt.close(fig)


def test_price_figure_title_carries_average(price_figure: Figure) -> None:
    """@brief The title shows the mean price 22.53."""
    assert "Average: 22.53" in price_figure.axes[0].get_title()


def test_price_figure_has_fifty_bins(price_figure: Figure) -> None:
    """@brief Fifty bins give fifty bars."""
    assert len(_bars(price_figure)) == PRICE_BIN_COUNT


def test_price_figure_counts_every_home(
    price_figure: Figure, boston_data: pd.DataFrame
) -> None:
    """@brief The bar heights add up to the 506 homes."""
    heights = [bar.get_height() for bar in price_figure.axes[0].patches]
    assert sum(heights) == len(boston_data)


def test_price_figure_has_aspect_two(price_figure: Figure) -> None:
    """@brief The figure is twice as wide as it is high."""
    width, height = price_figure.get_size_inches()
    assert width / height == pytest.approx(ASPECT_RATIO)


def test_price_figure_draws_a_kde_curve(price_figure: Figure) -> None:
    """@brief The histogram has a curve on top."""
    assert len(price_figure.axes[0].lines) == 1


def test_price_figure_uses_price_colour(price_figure: Figure) -> None:
    """@brief The curve is drawn in the price blue."""
    assert _line_color(price_figure) == to_rgb(constants.COLOR_PRICE)


def test_price_figure_labels_axes(price_figure: Figure) -> None:
    """@brief The axes say price in 000s and number of homes."""
    ax = price_figure.axes[0]
    assert (ax.get_xlabel(), ax.get_ylabel()) == ("Price in 000s", "Nr. of Homes")


def test_distance_figure_title_carries_average(distance_figure: Figure) -> None:
    """@brief The title shows the mean distance 3.80."""
    assert distance_figure.axes[0].get_title().endswith("Average: 3.80")


def test_distance_figure_uses_dark_blue_and_fifty_bins(
    distance_figure: Figure,
) -> None:
    """@brief The curve is dark blue and the histogram has fifty bars."""
    assert _line_color(distance_figure) == to_rgb("darkblue")
    assert len(_bars(distance_figure)) == PRICE_BIN_COUNT


def test_distance_figure_has_aspect_two(distance_figure: Figure) -> None:
    """@brief The figure is twice as wide as it is high."""
    width, height = distance_figure.get_size_inches()
    assert width / height == pytest.approx(ASPECT_RATIO)


def test_distance_figure_labels_axes(distance_figure: Figure) -> None:
    """@brief The x axis names the five employment centres."""
    ax = distance_figure.axes[0]
    assert ax.get_xlabel() == "Weighted Distance to 5 Boston Employment Centres"
    assert ax.get_ylabel() == "Nr. of Homes"


def test_rooms_figure_title_carries_average(rooms_figure: Figure) -> None:
    """@brief The title shows the mean number of rooms 6.28."""
    assert rooms_figure.axes[0].get_title().endswith("Average: 6.28")


def test_rooms_figure_uses_teal(rooms_figure: Figure) -> None:
    """@brief The curve is drawn in teal."""
    assert _line_color(rooms_figure) == to_rgb("#00796b")


def test_rooms_figure_has_aspect_two(rooms_figure: Figure) -> None:
    """@brief The figure is twice as wide as it is high."""
    width, height = rooms_figure.get_size_inches()
    assert width / height == pytest.approx(ASPECT_RATIO)


def test_rooms_figure_labels_axes(rooms_figure: Figure) -> None:
    """@brief The axes say average number of rooms and number of homes."""
    ax = rooms_figure.axes[0]
    assert (ax.get_xlabel(), ax.get_ylabel()) == (
        "Average Number of Rooms",
        "Nr. of Homes",
    )


def test_highway_figure_has_24_bins(highway_figure: Figure) -> None:
    """@brief Twenty-four bins give twenty-four bars."""
    assert len(highway_figure.axes[0].patches) == constants.RAD_BINS


def test_highway_figure_counts_every_home(
    highway_figure: Figure, boston_data: pd.DataFrame
) -> None:
    """@brief The bar heights add up to the 506 homes."""
    heights = [bar.get_height() for bar in highway_figure.axes[0].patches]
    assert sum(heights) == len(boston_data)


def test_highway_figure_bars_are_half_a_bin_wide(
    highway_figure: Figure, boston_data: pd.DataFrame
) -> None:
    """@brief The bar width is 0.5 of the bin width."""
    column = boston_data[constants.COL_RAD]
    bin_width = (column.max() - column.min()) / constants.RAD_BINS
    widths = _bars(highway_figure)
    assert widths[0] == pytest.approx(constants.RAD_BAR_WIDTH * bin_width)


def test_highway_figure_bars_are_purple_with_black_edges(
    highway_figure: Figure,
) -> None:
    """@brief The bars are purple and have black edges."""
    bar = highway_figure.axes[0].patches[0]
    assert to_rgb(bar.get_facecolor()) == to_rgb("#7b1fa2")
    assert to_rgb(bar.get_edgecolor()) == to_rgb("black")


def test_highway_figure_labels_axes(highway_figure: Figure) -> None:
    """@brief The axes say accessibility to highways and number of houses."""
    ax = highway_figure.axes[0]
    assert (ax.get_xlabel(), ax.get_ylabel()) == (
        "Accessibility to Highways",
        "Nr. of Houses",
    )


def test_highway_figure_size_and_dpi(highway_figure: Figure) -> None:
    """@brief The figure is 10 by 5 inches at 200 dpi."""
    assert tuple(highway_figure.get_size_inches()) == (10, 5)
    assert highway_figure.dpi == constants.HISTOGRAM_DPI


def test_river_bar_chart_returns_plotly_figure(boston_data: pd.DataFrame) -> None:
    """@brief The river chart is a Plotly figure."""
    assert isinstance(charts.river_bar_chart(boston_data), PlotlyFigure)


def test_river_bar_chart_has_no_and_yes_categories(boston_data: pd.DataFrame) -> None:
    """@brief The categories are No and Yes."""
    bar = charts.river_bar_chart(boston_data)
    assert list(bar.data[0].x) == ["No", "Yes"]


def test_river_bar_chart_has_471_and_35_homes(boston_data: pd.DataFrame) -> None:
    """@brief 471 homes are away from the river and 35 are next to it."""
    bar = charts.river_bar_chart(boston_data)
    assert tuple(bar.data[0].y) == RIVER_COUNTS


def test_river_bar_chart_uses_haline_without_colour_axis(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The bars are coloured on the haline scale and the scale is hidden."""
    layout = charts.river_bar_chart(boston_data).layout
    assert layout.coloraxis.showscale is False
    colours = [stop[1] for stop in layout.coloraxis.colorscale]
    assert colours[0] == px.colors.sequential.haline[0]
    assert colours[-1] == px.colors.sequential.haline[-1]


def test_river_bar_chart_has_titles(boston_data: pd.DataFrame) -> None:
    """@brief The chart and its axes are titled."""
    layout = charts.river_bar_chart(boston_data).layout
    assert layout.title.text == "Next to Charles River?"
    assert layout.xaxis.title.text == "Property Located Next to the River?"
    assert layout.yaxis.title.text == "Number of Homes"


def test_river_bar_chart_of_table_without_river_counts_zero() -> None:
    """@brief A table with no river tract shows 0 under Yes."""
    table = pd.DataFrame({constants.COL_CHAS: [0, 0]})
    bar = charts.river_bar_chart(table)
    assert tuple(bar.data[0].y) == (2, 0)


def test_distribution_panel_has_four_axes(boston_data: pd.DataFrame) -> None:
    """@brief The panel holds the price, distance, rooms and highway charts."""
    fig = charts.distribution_panel_figure(boston_data)
    try:
        assert len(fig.axes) == 4
    finally:
        plt.close(fig)


def test_distribution_panel_titles_carry_averages(boston_data: pd.DataFrame) -> None:
    """@brief The three averages are in the panel titles."""
    fig = charts.distribution_panel_figure(boston_data)
    try:
        titles = [ax.get_title() for ax in fig.axes]
    finally:
        plt.close(fig)
    assert "22.53" in titles[0]
    assert "3.80" in titles[1]
    assert "6.28" in titles[2]


def test_distribution_panel_highway_chart_has_24_bars(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The fourth axis is the highway histogram with 24 bars."""
    fig = charts.distribution_panel_figure(boston_data)
    try:
        assert len(fig.axes[3].patches) == constants.RAD_BINS
    finally:
        plt.close(fig)


def test_charts_do_not_change_data(boston_data: pd.DataFrame) -> None:
    """@brief Drawing leaves the table as it was."""
    before = boston_data.copy()
    plt.close(charts.price_distribution_figure(boston_data))
    plt.close(charts.highway_access_figure(boston_data))
    charts.river_bar_chart(boston_data)
    pd.testing.assert_frame_equal(boston_data, before)


def test_distribution_charts_accept_an_empty_table() -> None:
    """@brief An empty table draws empty charts with a nan average."""
    table = pd.DataFrame(columns=list(constants.ALL_COLUMNS), dtype=float)
    price = charts.price_distribution_figure(table)
    try:
        assert "nan" in price.axes[0].get_title()
    finally:
        plt.close(price)
    assert tuple(charts.river_bar_chart(table).data[0].y) == (0, 0)
