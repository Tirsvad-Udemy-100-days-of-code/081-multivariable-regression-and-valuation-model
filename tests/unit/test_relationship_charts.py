"""@brief Tests for the relationship charts."""

from collections.abc import Callable, Iterator
from typing import NamedTuple

import matplotlib.pyplot as plt
import pandas as pd
import pytest
import seaborn as sns
from matplotlib.colors import to_rgb
from matplotlib.figure import Figure

from boston_valuation import constants
from boston_valuation.presentation import relationship_charts as charts

SUBSET = ["RM", "LSTAT", "PRICE"]
SCATTER_AXES = len(SUBSET) * (len(SUBSET) - 1)
EXPECTED_PANEL_AXES = 6


class JointCase(NamedTuple):
    """@brief What one joint plot of the assignment must look like."""

    draw: Callable[[pd.DataFrame], Figure]
    x: str
    y: str
    colour: str
    height: int
    style: str


JOINT_CASES = {
    "distance_pollution": JointCase(
        charts.distance_pollution_figure, "DIS", "NOX", "deeppink", 8, "darkgrid"
    ),
    "pollution_industry": JointCase(
        charts.pollution_industry_figure, "NOX", "INDUS", "darkgreen", 7, "darkgrid"
    ),
    "poverty_rooms": JointCase(
        charts.poverty_rooms_figure, "LSTAT", "RM", "orange", 7, "darkgrid"
    ),
    "poverty_price": JointCase(
        charts.poverty_price_figure, "LSTAT", "PRICE", "crimson", 7, "darkgrid"
    ),
    "rooms_price": JointCase(
        charts.rooms_price_figure, "RM", "PRICE", "darkblue", 7, "whitegrid"
    ),
}


@pytest.fixture(scope="module")
def joint_figures(boston_data: pd.DataFrame) -> Iterator[dict[str, Figure]]:
    """@brief Draw the five joint plots once and close them afterwards.

    @param boston_data The real table.
    @return The figures by case name.
    """
    figures = {name: case.draw(boston_data) for name, case in JOINT_CASES.items()}
    yield figures
    for fig in figures.values():
        plt.close(fig)


@pytest.mark.parametrize("name", list(JOINT_CASES))
def test_joint_plot_scatter_is_half_transparent(
    joint_figures: dict[str, Figure], name: str
) -> None:
    """@brief The dots have alpha 0.5, as the assignment asks."""
    scatter = joint_figures[name].axes[0].collections[0]
    assert scatter.get_alpha() == constants.JOINT_ALPHA == 0.5


@pytest.mark.parametrize("name", list(JOINT_CASES))
def test_joint_plot_scatter_has_the_assignment_colour(
    joint_figures: dict[str, Figure], name: str
) -> None:
    """@brief The dots are drawn in the colour of the assignment."""
    scatter = joint_figures[name].axes[0].collections[0]
    assert to_rgb(scatter.get_facecolor()[0]) == to_rgb(JOINT_CASES[name].colour)


@pytest.mark.parametrize("name", list(JOINT_CASES))
def test_joint_plot_has_the_assignment_height(
    joint_figures: dict[str, Figure], name: str
) -> None:
    """@brief The figure is as wide and as high as the assignment says."""
    height = JOINT_CASES[name].height
    assert tuple(joint_figures[name].get_size_inches()) == (height, height)


@pytest.mark.parametrize("name", list(JOINT_CASES))
def test_joint_plot_labels_axes_with_the_columns(
    joint_figures: dict[str, Figure], name: str
) -> None:
    """@brief The horizontal axis is x and the vertical axis is y."""
    ax = joint_figures[name].axes[0]
    case = JOINT_CASES[name]
    assert (ax.get_xlabel(), ax.get_ylabel()) == (case.x, case.y)


@pytest.mark.parametrize("name", list(JOINT_CASES))
def test_joint_plot_plots_every_home(
    joint_figures: dict[str, Figure], boston_data: pd.DataFrame, name: str
) -> None:
    """@brief One dot per home, at the values of the two columns."""
    case = JOINT_CASES[name]
    offsets = joint_figures[name].axes[0].collections[0].get_offsets()
    assert len(offsets) == len(boston_data)
    assert list(offsets[:, 0]) == pytest.approx(list(boston_data[case.x]))
    assert list(offsets[:, 1]) == pytest.approx(list(boston_data[case.y]))


@pytest.mark.parametrize("name", list(JOINT_CASES))
def test_joint_plot_has_marginal_histograms(
    joint_figures: dict[str, Figure], name: str
) -> None:
    """@brief A joint plot has the scatter plot and two marginal axes."""
    assert len(joint_figures[name].axes) == 3


@pytest.mark.parametrize("name", list(JOINT_CASES))
def test_joint_plot_uses_the_assignment_style(
    joint_figures: dict[str, Figure], name: str
) -> None:
    """@brief The background is a dark grid, or a white grid for rooms/price."""
    expected = sns.axes_style(JOINT_CASES[name].style)["axes.facecolor"]
    ax = joint_figures[name].axes[0]
    assert to_rgb(ax.get_facecolor()) == to_rgb(expected)


def test_joint_plot_figure_accepts_any_pair_and_style(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The helper works for a pair that is not one of the five."""
    fig = charts.joint_plot_figure(
        boston_data, "AGE", "TAX", "purple", 5, style="whitegrid"
    )
    try:
        assert tuple(fig.get_size_inches()) == (5, 5)
        assert fig.axes[0].get_xlabel() == "AGE"
    finally:
        plt.close(fig)


def test_joint_plot_figure_rejects_unknown_column(boston_data: pd.DataFrame) -> None:
    """@brief A column that is not in the table is an error."""
    with pytest.raises(KeyError):
        charts.joint_plot_figure(boston_data, "nope", "RM", "red", 5)


def test_pair_plot_of_a_subset_draws_a_grid_of_those_columns(
    boston_data: pd.DataFrame,
) -> None:
    """@brief Three columns give six scatter plots, one per ordered pair."""
    fig = charts.pair_plot_figure(boston_data, SUBSET)
    try:
        assert len([ax for ax in fig.axes if ax.collections]) == SCATTER_AXES
        labels = {ax.get_xlabel() for ax in fig.axes if ax.get_xlabel()}
        assert labels == set(SUBSET)
    finally:
        plt.close(fig)


def test_pair_plot_without_regression_has_no_lines(boston_data: pd.DataFrame) -> None:
    """@brief The default pair plot draws dots and histograms only."""
    fig = charts.pair_plot_figure(boston_data, SUBSET)
    try:
        assert all(not ax.lines for ax in fig.axes)
    finally:
        plt.close(fig)


def test_pair_plot_with_regression_line_draws_cyan_lines(
    boston_data: pd.DataFrame,
) -> None:
    """@brief Every scatter plot gets a cyan regression line."""
    fig = charts.pair_plot_figure(boston_data, SUBSET, regression_line=True)
    try:
        lines = [line for ax in fig.axes for line in ax.lines]
        assert len(lines) == len(SUBSET) * (len(SUBSET) - 1)
        assert {to_rgb(line.get_color()) for line in lines} == {to_rgb("cyan")}
    finally:
        plt.close(fig)


def test_pair_plot_rejects_unknown_column(boston_data: pd.DataFrame) -> None:
    """@brief A column that is not in the table is an error."""
    with pytest.raises(KeyError):
        charts.pair_plot_figure(boston_data, ["nope"])


def test_relationship_panel_has_five_scatter_plots_and_a_bar_chart(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The panel holds six axes: five scatter plots and one bar chart."""
    fig = charts.relationship_panel_figure(boston_data)
    try:
        assert len(fig.axes) == EXPECTED_PANEL_AXES
        scatters = [ax for ax in fig.axes if ax.collections]
        assert len(scatters) == len(constants.RELATIONSHIP_PAIRS)
        assert len(fig.axes[-1].patches) == len(constants.FEATURE_COLUMNS)
    finally:
        plt.close(fig)


def test_relationship_panel_titles_carry_the_correlation(
    boston_data: pd.DataFrame,
) -> None:
    """@brief Each scatter plot is titled with its pair and coefficient."""
    fig = charts.relationship_panel_figure(boston_data)
    try:
        titles = [ax.get_title() for ax in fig.axes]
    finally:
        plt.close(fig)
    assert titles[0] == "DIS vs NOX, r = -0.77"
    assert titles[1] == "NOX vs INDUS, r = 0.76"
    assert titles[4] == "RM vs PRICE, r = 0.70"
    assert titles[5] == constants.CORRELATION_BARS_TITLE


def test_relationship_panel_scatter_uses_alpha_and_colours(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The panel uses the colours and the opacity of the joint plots."""
    fig = charts.relationship_panel_figure(boston_data)
    try:
        scatters = [ax.collections[0] for ax in fig.axes[:5]]
        assert {s.get_alpha() for s in scatters} == {constants.JOINT_ALPHA}
        assert [to_rgb(s.get_facecolor()[0]) for s in scatters] == [
            to_rgb(colour) for colour in constants.RELATIONSHIP_COLORS
        ]
    finally:
        plt.close(fig)


def test_relationship_panel_bars_are_sorted_strongest_first(
    boston_data: pd.DataFrame,
) -> None:
    """@brief The bar chart lists the strongest correlation at the top."""
    fig = charts.relationship_panel_figure(boston_data)
    try:
        labels = [tick.get_text() for tick in fig.axes[5].get_yticklabels()]
    finally:
        plt.close(fig)
    assert labels[:2] == [constants.COL_LSTAT, constants.COL_RM]
    assert constants.COL_PRICE not in labels


def test_charts_do_not_change_data(boston_data: pd.DataFrame) -> None:
    """@brief Drawing leaves the table as it was."""
    before = boston_data.copy()
    plt.close(charts.relationship_panel_figure(boston_data))
    plt.close(charts.pair_plot_figure(boston_data, SUBSET))
    pd.testing.assert_frame_equal(boston_data, before)
