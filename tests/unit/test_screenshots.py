"""@brief Tests for the picture generator."""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import pytest
from matplotlib.figure import Figure

from boston_valuation import constants
from boston_valuation.presentation import screenshots

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_PICTURE_BYTES = 400_000
MAX_STEP_5_PICTURE_BYTES = 450_000


def _fake_figure() -> Figure:
    """@brief Build a tiny figure that needs no data.

    @return An empty figure.
    """
    return Figure(figsize=(1, 1))


@pytest.fixture
def fake_pictures(monkeypatch: pytest.MonkeyPatch) -> list[str]:
    """@brief Replace the registry with two cheap pictures.

    @param monkeypatch Pytest helper that restores the registry afterwards.
    @return The names of the fake pictures.
    """
    fakes = {"first.png": _fake_figure, "second.png": _fake_figure}
    monkeypatch.setattr(screenshots, "PICTURES", fakes)
    return list(fakes)


def test_backend_is_agg_so_no_window_opens() -> None:
    """@brief Pictures are drawn off screen."""
    assert matplotlib.get_backend().lower() == "agg"


def test_pictures_include_overview() -> None:
    """@brief The overview is registered under its picture name."""
    assert constants.STEP_PICTURES[0] in screenshots.PICTURES


def test_pictures_include_step_1_goals() -> None:
    """@brief The descriptive table is registered under its picture name."""
    assert constants.STEP_PICTURES[1] in screenshots.PICTURES


def test_step_1_goals_draws_descriptive_title() -> None:
    """@brief The step 1 picture is the descriptive statistics table."""
    fig = screenshots.step_1_goals()
    assert fig.get_suptitle() == constants.DESCRIPTIVE_TITLE


def test_pictures_include_step_2_distributions() -> None:
    """@brief The distribution panel is registered under its picture name."""
    assert constants.STEP_PICTURES[2] in screenshots.PICTURES
    assert constants.STEP_PICTURES[2] == "step-2-distributions.png"


def test_step_2_distributions_draws_panel_of_four_charts() -> None:
    """@brief The step 2 picture is a panel titled after the four charts."""
    fig = screenshots.step_2_distributions()
    try:
        assert len(fig.axes) == 4
        assert fig.get_suptitle() == constants.PANEL_TITLE
    finally:
        plt.close(fig)


def test_step_2_distributions_is_written_as_png(tmp_path: Path) -> None:
    """@brief The step 2 picture is saved as a real, reasonably small PNG."""
    path = screenshots.render_picture(constants.STEP_PICTURES[2], tmp_path)
    assert path.read_bytes().startswith(PNG_SIGNATURE)
    assert path.stat().st_size < MAX_PICTURE_BYTES


def test_pictures_include_step_3_relationships() -> None:
    """@brief The relationship panel is registered under its picture name."""
    assert constants.STEP_PICTURES[3] in screenshots.PICTURES
    assert constants.STEP_PICTURES[3] == "step-3-relationships.png"
    assert screenshots.PICTURES[constants.STEP_PICTURES[3]] is (
        screenshots.step_3_relationships
    )


def test_step_3_relationships_draws_five_scatter_plots_and_bars() -> None:
    """@brief The step 3 picture is a panel of six charts with a title."""
    fig = screenshots.step_3_relationships()
    try:
        assert len(fig.axes) == 6
        assert fig.get_suptitle() == constants.RELATIONSHIP_PANEL_TITLE
    finally:
        plt.close(fig)


def test_step_3_relationships_is_written_as_png(tmp_path: Path) -> None:
    """@brief The step 3 picture is saved as a real, reasonably small PNG."""
    path = screenshots.render_picture(constants.STEP_PICTURES[3], tmp_path)
    assert path.read_bytes().startswith(PNG_SIGNATURE)
    assert path.stat().st_size < MAX_PICTURE_BYTES


def test_pictures_include_step_4_regression() -> None:
    """@brief The regression panel is registered under its picture name."""
    assert constants.STEP_PICTURES[4] in screenshots.PICTURES
    assert constants.STEP_PICTURES[4] == "step-4-regression.png"
    assert screenshots.PICTURES[constants.STEP_PICTURES[4]] is (
        screenshots.step_4_regression
    )


def test_step_4_regression_draws_three_charts_with_the_r_squared() -> None:
    """@brief The step 4 picture is a panel of three charts."""
    fig = screenshots.step_4_regression()
    try:
        assert len(fig.axes) == 3
        assert "r-squared 0.75" in fig.get_suptitle()
    finally:
        plt.close(fig)


def test_step_4_regression_is_written_as_png(tmp_path: Path) -> None:
    """@brief The step 4 picture is saved as a real, reasonably small PNG."""
    path = screenshots.render_picture(constants.STEP_PICTURES[4], tmp_path)
    assert path.read_bytes().startswith(PNG_SIGNATURE)
    assert path.stat().st_size < MAX_PICTURE_BYTES


def test_pictures_include_step_5_log_model() -> None:
    """@brief The model comparison panel is registered under its picture name."""
    assert constants.STEP_PICTURES[5] in screenshots.PICTURES
    assert constants.STEP_PICTURES[5] == "step-5-log-model.png"
    assert screenshots.PICTURES[constants.STEP_PICTURES[5]] is (
        screenshots.step_5_log_model
    )


def test_step_5_log_model_draws_six_charts_with_both_r_squared() -> None:
    """@brief The step 5 picture is a panel of two rows of three charts."""
    fig = screenshots.step_5_log_model()
    try:
        assert len(fig.axes) == 6
        title = fig.get_suptitle()
        assert "training r-squared 0.75 vs 0.79" in title
        assert "test r-squared 0.67 vs 0.74" in title
    finally:
        plt.close(fig)


def test_step_5_log_model_is_written_as_png(tmp_path: Path) -> None:
    """@brief The step 5 picture is saved as a real, reasonably small PNG."""
    path = screenshots.render_picture(constants.STEP_PICTURES[5], tmp_path)
    assert path.read_bytes().startswith(PNG_SIGNATURE)
    assert path.stat().st_size < MAX_STEP_5_PICTURE_BYTES


def test_overview_figure_has_one_axis() -> None:
    """@brief The overview is drawn on a single axis."""
    fig = screenshots.overview_figure()
    assert len(fig.axes) == 1


def test_overview_figure_shows_title() -> None:
    """@brief The overview carries the project title."""
    fig = screenshots.overview_figure()
    assert fig.axes[0].get_title() == constants.OVERVIEW_TITLE


def test_overview_figure_has_one_arrow_between_steps() -> None:
    """@brief Seven boxes are joined by six arrows."""
    fig = screenshots.overview_figure()
    arrows = [p for p in fig.axes[0].patches if type(p).__name__ == "FancyArrowPatch"]
    assert len(arrows) == len(constants.OVERVIEW_STEPS) - 1


def test_render_picture_writes_png_signature(tmp_path: Path) -> None:
    """@brief The overview is saved as a real PNG file."""
    path = screenshots.render_picture(constants.OVERVIEW_PICTURE, tmp_path)
    assert path.read_bytes().startswith(PNG_SIGNATURE)


def test_render_picture_returns_path_in_output_dir(tmp_path: Path) -> None:
    """@brief The file is named after the picture and sits in the folder."""
    path = screenshots.render_picture(constants.OVERVIEW_PICTURE, tmp_path)
    assert path == tmp_path / constants.OVERVIEW_PICTURE


def test_render_picture_creates_missing_folder(tmp_path: Path) -> None:
    """@brief A missing output folder is created."""
    target = tmp_path / "nested" / "images"
    path = screenshots.render_picture(constants.OVERVIEW_PICTURE, target)
    assert path.is_file()


def test_render_picture_rejects_unknown_name(tmp_path: Path) -> None:
    """@brief An unregistered name raises a specific error."""
    with pytest.raises(screenshots.UnknownPictureError):
        screenshots.render_picture("missing.png", tmp_path)


def test_render_all_returns_registry_files(
    tmp_path: Path, fake_pictures: list[str]
) -> None:
    """@brief render_all writes one file per registered picture."""
    written = screenshots.render_all(tmp_path)
    assert [p.name for p in written] == fake_pictures


def test_render_all_writes_only_requested_names(
    tmp_path: Path, fake_pictures: list[str]
) -> None:
    """@brief A name list limits what is drawn."""
    written = screenshots.render_all(tmp_path, [fake_pictures[1]])
    assert [p.name for p in written] == [fake_pictures[1]]


def test_render_all_draws_every_real_picture(tmp_path: Path) -> None:
    """@brief Every picture of the real registry becomes a non-empty file."""
    written = screenshots.render_all(tmp_path)
    assert {p.name for p in written} == set(screenshots.PICTURES)
    assert all(p.stat().st_size > 0 for p in written)


def test_main_returns_zero_with_output_dir(tmp_path: Path) -> None:
    """@brief A normal run succeeds."""
    assert screenshots.main(["--output-dir", str(tmp_path)]) == 0


def test_main_writes_overview_to_output_dir(tmp_path: Path) -> None:
    """@brief A normal run leaves the overview in the folder."""
    screenshots.main(["--output-dir", str(tmp_path)])
    assert (tmp_path / constants.OVERVIEW_PICTURE).is_file()


def test_main_returns_nonzero_for_unknown_only_name(tmp_path: Path) -> None:
    """@brief A name that is not registered fails the run."""
    assert screenshots.main(["--output-dir", str(tmp_path), "--only", "no.png"]) != 0


def test_main_writes_nothing_for_unknown_only_name(tmp_path: Path) -> None:
    """@brief A failed run leaves no picture behind."""
    screenshots.main(["--output-dir", str(tmp_path), "--only", "no.png"])
    assert list(tmp_path.iterdir()) == []


def test_main_draws_only_named_picture(
    tmp_path: Path, fake_pictures: list[str]
) -> None:
    """@brief --only limits the files written."""
    screenshots.main(["--output-dir", str(tmp_path), "--only", fake_pictures[0]])
    assert [p.name for p in tmp_path.iterdir()] == [fake_pictures[0]]
