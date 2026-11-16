"""@brief Tests for the summary chart of step 7."""

from collections.abc import Iterator

import matplotlib.pyplot as plt
import pandas as pd
import pytest
from matplotlib.colors import to_rgb
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
from matplotlib.text import Annotation

from boston_valuation import constants
from boston_valuation.domain import log_model
from boston_valuation.presentation import summary_charts

INDIGO = to_rgb(constants.COLOR_LINEAR_MODEL)
NAVY = to_rgb(constants.COLOR_LOG_MODEL)
TOLERANCE = 0.01


@pytest.fixture(scope="module")
def figure(boston_data: pd.DataFrame) -> Iterator[Figure]:
    """@brief Draw the summary figure once for several tests.

    @param boston_data The real table.
    @return The figure, closed after the last test of the module.
    """
    fig = summary_charts.model_scores_figure(boston_data)
    yield fig
    plt.close(fig)


def _bars(fig: Figure) -> list[Rectangle]:
    """@brief Return the four bars of the figure, left to right.

    @param fig The summary figure.
    @return Linear training, log training, linear test, log test.
    """
    bars = sorted(fig.axes[0].patches, key=lambda bar: bar.get_x())
    assert all(isinstance(bar, Rectangle) for bar in bars)
    return bars


def test_figure_has_four_bars(figure: Figure) -> None:
    """@brief Two models on two data sets make four bars."""
    assert len(_bars(figure)) == 4


def test_bars_show_the_four_r_squared_values(figure: Figure) -> None:
    """@brief The bars are 0.75, 0.79, 0.67 and 0.74 high."""
    heights = [bar.get_height() for bar in _bars(figure)]
    assert heights == pytest.approx([0.75, 0.79, 0.67, 0.74], abs=TOLERANCE)


def test_bar_heights_come_from_the_fitted_models(
    figure: Figure, boston_data: pd.DataFrame
) -> None:
    """@brief The bars are the scores of the models of the domain."""
    linear = log_model.fit_linear_model(boston_data)
    log = log_model.fit_log_model(boston_data)
    heights = [bar.get_height() for bar in _bars(figure)]
    assert heights == pytest.approx(
        [
            linear.train_r_squared,
            log.train_r_squared,
            linear.test_r_squared,
            log.test_r_squared,
        ]
    )


def test_bars_use_indigo_for_linear_and_navy_for_log(figure: Figure) -> None:
    """@brief Each model keeps its colour in both groups."""
    colours = [tuple(bar.get_facecolor()[:3]) for bar in _bars(figure)]
    assert colours == [
        pytest.approx(INDIGO),
        pytest.approx(NAVY),
        pytest.approx(INDIGO),
        pytest.approx(NAVY),
    ]


def test_test_bars_are_lower_than_training_bars(figure: Figure) -> None:
    """@brief Both models score lower on the rows they never saw."""
    linear_train, log_train, linear_test, log_test = (
        bar.get_height() for bar in _bars(figure)
    )
    assert linear_test < linear_train
    assert log_test < log_train


def test_log_model_beats_linear_model_in_both_groups(figure: Figure) -> None:
    """@brief The log bar is higher than the linear bar on both data sets."""
    linear_train, log_train, linear_test, log_test = (
        bar.get_height() for bar in _bars(figure)
    )
    assert log_train > linear_train
    assert log_test > linear_test


def test_bars_carry_the_scores_with_two_decimals(figure: Figure) -> None:
    """@brief The labels read 0.75, 0.79, 0.67 and 0.74."""
    labels = [text for text in figure.axes[0].texts if isinstance(text, Annotation)]
    labels.sort(key=lambda label: label.xy[0])
    assert [label.get_text() for label in labels] == ["0.75", "0.79", "0.67", "0.74"]


def test_groups_are_named_training_and_test_data(figure: Figure) -> None:
    """@brief The ticks name the two data sets."""
    ticks = [tick.get_text() for tick in figure.axes[0].get_xticklabels()]
    assert ticks == ["Training data", "Test data"]


def test_legend_names_both_models(figure: Figure) -> None:
    """@brief The legend has one entry per model."""
    legend = figure.axes[0].get_legend()
    assert legend is not None
    assert [text.get_text() for text in legend.get_texts()] == [
        "Linear model on the price",
        "Log model on the log price",
    ]


def test_y_axis_is_r_squared_from_zero_to_one(figure: Figure) -> None:
    """@brief The axis is labelled and spans the whole r-squared range."""
    ax = figure.axes[0]
    assert ax.get_ylabel() == "r-squared"
    assert ax.get_ylim() == (0.0, 1.0)


def test_title_says_the_log_model_keeps_its_lead(figure: Figure) -> None:
    """@brief The title is the message of the chart."""
    assert figure.get_suptitle() == (
        "Out of sample: the log model keeps its lead on unseen homes"
    )


def test_subtitle_says_both_scores_are_lower_on_test_data(figure: Figure) -> None:
    """@brief The caption states what the lower bars mean."""
    assert "lower on the test data" in figure.axes[0].get_title()


def test_figure_uses_the_picture_resolution_and_size(figure: Figure) -> None:
    """@brief The figure has the size and dpi set in the constants."""
    assert figure.dpi == constants.PICTURE_DPI
    assert tuple(figure.get_size_inches()) == pytest.approx(
        constants.SUMMARY_FIGURE_SIZE
    )
