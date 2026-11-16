"""@brief Tests for the picture generator."""

from pathlib import Path

import matplotlib
import pytest
from matplotlib.figure import Figure

from boston_valuation import constants
from boston_valuation.presentation import screenshots

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


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
