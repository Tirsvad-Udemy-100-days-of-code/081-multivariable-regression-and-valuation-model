"""@brief Generate the pictures for the README and the wiki.

@details Run from the repository root::

    python -m boston_valuation.presentation.screenshots

Each picture is drawn by the code of this project, so it always matches the
code. To add a picture, write a function that returns a figure and add one
line to ::PICTURES.
"""

import argparse
import logging
import textwrap
from collections.abc import Callable, Sequence
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.axes import Axes  # noqa: E402
from matplotlib.figure import Figure  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

from boston_valuation import constants  # noqa: E402
from boston_valuation.infrastructure.csv_loader import load_data  # noqa: E402
from boston_valuation.presentation.charts import (  # noqa: E402
    descriptive_table_figure,
)
from boston_valuation.presentation.distribution_charts import (  # noqa: E402
    distribution_panel_figure,
)

_LOG = logging.getLogger(__name__)
DEFAULT_OUTPUT_DIR = Path(*constants.IMAGES_DIR)
_EXIT_OK = 0
_EXIT_UNKNOWN_PICTURE = 2

type Point = tuple[float, float]


class UnknownPictureError(KeyError):
    """@brief Raised when a picture name is not in the registry."""


def _row_origins() -> list[Point]:
    """@brief Compute the bottom-left corner of every workflow box.

    @return One corner per step, left to right, the first row on top and each
        row centred under the widest one.
    """
    pitch = constants.OVERVIEW_BOX_WIDTH + constants.OVERVIEW_BOX_GAP
    widest = max(constants.OVERVIEW_ROW_SIZES)
    full_width = widest * pitch - constants.OVERVIEW_BOX_GAP
    rows = len(constants.OVERVIEW_ROW_SIZES)
    corners: list[Point] = []
    for row, size in enumerate(constants.OVERVIEW_ROW_SIZES):
        row_width = size * pitch - constants.OVERVIEW_BOX_GAP
        left = (full_width - row_width) / 2
        bottom = (rows - 1 - row) * constants.OVERVIEW_ROW_GAP
        corners.extend((left + i * pitch, bottom) for i in range(size))
    return corners


def _draw_box(ax: Axes, corner: Point, number: int, label: str) -> None:
    """@brief Draw one rounded workflow box with its number and label.

    @param ax Axis to draw on.
    @param corner Bottom-left corner of the box.
    @param number Step number shown in the box.
    @param label Short step name shown under the number.
    """
    x, y = corner
    width = constants.OVERVIEW_BOX_WIDTH
    height = constants.OVERVIEW_BOX_HEIGHT
    ax.add_patch(
        FancyBboxPatch(
            corner,
            width,
            height,
            boxstyle=f"round,pad={constants.OVERVIEW_BOX_PAD}",
            facecolor=constants.OVERVIEW_BOX_FACE_COLOR,
            edgecolor=constants.OVERVIEW_BOX_EDGE_COLOR,
            linewidth=constants.OVERVIEW_BOX_LINEWIDTH,
        )
    )
    centre_x = x + width / 2
    ax.text(
        centre_x,
        y + height * 0.72,
        str(number),
        ha="center",
        va="center",
        fontsize=constants.OVERVIEW_NUMBER_FONT_SIZE,
        fontweight="bold",
        color=constants.OVERVIEW_TEXT_COLOR,
    )
    ax.text(
        centre_x,
        y + height * 0.32,
        textwrap.fill(label, width=constants.OVERVIEW_WRAP_WIDTH),
        ha="center",
        va="center",
        fontsize=constants.OVERVIEW_LABEL_FONT_SIZE,
        color=constants.OVERVIEW_TEXT_COLOR,
    )


def _draw_arrow(ax: Axes, start: Point, end: Point) -> None:
    """@brief Draw an arrow between two points.

    @param ax Axis to draw on.
    @param start Where the arrow leaves.
    @param end Where the arrow head points.
    """
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle=constants.OVERVIEW_ARROW_STYLE,
            mutation_scale=constants.OVERVIEW_ARROW_SCALE,
            linewidth=constants.OVERVIEW_ARROW_LINEWIDTH,
            color=constants.OVERVIEW_ARROW_COLOR,
            shrinkA=0,
            shrinkB=0,
        )
    )


def _draw_arrows(ax: Axes, corners: list[Point]) -> None:
    """@brief Join every box to the next one.

    @param ax Axis to draw on.
    @param corners The bottom-left corner of every box, in step order.
    """
    width = constants.OVERVIEW_BOX_WIDTH
    height = constants.OVERVIEW_BOX_HEIGHT
    pad = constants.OVERVIEW_BOX_PAD
    for (x1, y1), (x2, y2) in zip(corners, corners[1:], strict=False):
        if y1 == y2:
            middle = y1 + height / 2
            _draw_arrow(ax, (x1 + width + pad, middle), (x2 - pad, middle))
        else:
            _draw_arrow(
                ax, (x1 + width / 2, y1 - pad), (x2 + width / 2, y2 + height + pad)
            )


def overview_figure() -> Figure:
    """@brief Draw the seven steps of the project as a flow of boxes.

    @return A figure with one rounded box per step and an arrow between steps.
    """
    corners = _row_origins()
    fig, ax = plt.subplots(
        figsize=constants.OVERVIEW_FIGURE_SIZE, dpi=constants.PICTURE_DPI
    )
    for number, (corner, label) in enumerate(
        zip(corners, constants.OVERVIEW_STEPS, strict=True), start=1
    ):
        _draw_box(ax, corner, number, label)
    _draw_arrows(ax, corners)
    margin = constants.OVERVIEW_MARGIN
    right = max(x for x, _ in corners) + constants.OVERVIEW_BOX_WIDTH
    top = max(y for _, y in corners) + constants.OVERVIEW_BOX_HEIGHT
    ax.set_xlim(-margin, right + margin)
    ax.set_ylim(-margin, top + constants.OVERVIEW_TITLE_GAP)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(
        constants.OVERVIEW_TITLE,
        fontsize=constants.OVERVIEW_TITLE_FONT_SIZE,
        fontweight="bold",
    )
    fig.tight_layout()
    return fig


def step_1_goals() -> Figure:
    """@brief Draw the descriptive statistics of the data (lecture 597).

    @return The tables of count, mean, spread and quartiles of every column.
    """
    return descriptive_table_figure(load_data())


def step_2_distributions() -> Figure:
    """@brief Draw the distributions of price, distance, rooms and highways.

    @return A panel of four histograms made from the project's own data.
    """
    return distribution_panel_figure(load_data())


PICTURES: dict[str, Callable[[], Figure]] = {
    constants.OVERVIEW_PICTURE: overview_figure,
    constants.STEP_PICTURES[1]: step_1_goals,
    constants.STEP_PICTURES[2]: step_2_distributions,
}


def render_picture(name: str, output_dir: Path = DEFAULT_OUTPUT_DIR) -> Path:
    """@brief Draw one picture and save it as a PNG file.

    @param name File name of the picture, a key of ::PICTURES.
    @param output_dir Folder for the picture; it is created when missing.
    @return The path of the file written.
    @throws UnknownPictureError When the name is not in the registry.
    """
    try:
        draw = PICTURES[name]
    except KeyError as err:
        raise UnknownPictureError(name) from err
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / name
    fig = draw()
    try:
        fig.savefig(path)
    finally:
        plt.close(fig)
    return path


def render_all(
    output_dir: Path = DEFAULT_OUTPUT_DIR, names: Sequence[str] | None = None
) -> list[Path]:
    """@brief Draw the registered pictures and save them as PNG files.

    @param output_dir Folder for the pictures; it is created when missing.
    @param names Pictures to draw; every registered picture when omitted.
    @return The paths of the files written.
    """
    selected = list(PICTURES) if names is None else list(names)
    return [render_picture(name, output_dir) for name in selected]


def _parse_args(argv: Sequence[str] | None) -> argparse.Namespace:
    """@brief Read the command line.

    @param argv Arguments without the program name; the process arguments when
        omitted.
    @return The parsed options.
    """
    parser = argparse.ArgumentParser(description="Generate the project pictures.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--only",
        nargs="+",
        metavar="NAME",
        help="draw only these pictures (file names)",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    """@brief Command line entry point: write the pictures.

    @param argv Arguments without the program name; the process arguments when
        omitted.
    @return 0 on success, 2 when a requested picture does not exist.
    """
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    args = _parse_args(argv)
    try:
        written = render_all(args.output_dir, args.only)
    except UnknownPictureError as err:
        _LOG.error("Unknown picture %s; known: %s", err, ", ".join(PICTURES))
        return _EXIT_UNKNOWN_PICTURE
    for path in written:
        _LOG.info("%s", path)
    return _EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
