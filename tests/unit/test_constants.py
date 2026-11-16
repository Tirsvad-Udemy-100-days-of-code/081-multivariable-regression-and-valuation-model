"""@brief Tests for the constants and the shipped data file."""

from pathlib import Path

import pandas as pd

import boston_valuation
from boston_valuation import constants


def _data_file() -> Path:
    """@brief Locate the shipped CSV file.

    @return The data file inside the package.
    """
    package_root = Path(boston_valuation.__file__).resolve().parent
    return package_root / constants.DATA_DIR / constants.DATA_FILE


def _read_data() -> pd.DataFrame:
    """@brief Read the shipped CSV file the way the project does.

    @return The raw table with its index column.
    """
    return pd.read_csv(_data_file(), index_col=constants.INDEX_COLUMN)


def test_feature_columns_count_is_thirteen() -> None:
    """@brief The model uses thirteen features."""
    assert len(constants.FEATURE_COLUMNS) == 13


def test_feature_columns_follow_file_order() -> None:
    """@brief The features are listed in the order of the file."""
    assert constants.FEATURE_COLUMNS == (
        "CRIM",
        "ZN",
        "INDUS",
        "CHAS",
        "NOX",
        "RM",
        "AGE",
        "DIS",
        "RAD",
        "TAX",
        "PTRATIO",
        "B",
        "LSTAT",
    )


def test_all_columns_count_is_fourteen() -> None:
    """@brief The table has thirteen features and the price."""
    assert len(constants.ALL_COLUMNS) == constants.EXPECTED_COLUMNS == 14


def test_all_columns_end_with_price() -> None:
    """@brief The price is the last column."""
    assert constants.ALL_COLUMNS[-1] == constants.COL_PRICE


def test_test_size_is_twenty_percent() -> None:
    """@brief A fifth of the rows is held back for testing."""
    assert constants.TEST_SIZE == 0.2


def test_random_state_is_ten() -> None:
    """@brief The split is reproducible with the course seed."""
    assert constants.RANDOM_STATE == 10


def test_step_pictures_count_is_eight() -> None:
    """@brief There is one picture for the overview and one per step."""
    assert len(constants.STEP_PICTURES) == 8


def test_step_pictures_are_unique() -> None:
    """@brief No two steps share a file name."""
    assert len(set(constants.STEP_PICTURES)) == len(constants.STEP_PICTURES)


def test_step_pictures_are_png_files() -> None:
    """@brief Every picture name ends in .png."""
    assert all(name.endswith(".png") for name in constants.STEP_PICTURES)


def test_data_file_exists_in_package() -> None:
    """@brief The CSV file ships inside the package."""
    assert _data_file().is_file()


def test_data_has_expected_row_count() -> None:
    """@brief The file holds one row per house."""
    assert len(_read_data()) == constants.EXPECTED_ROWS


def test_data_has_expected_column_order() -> None:
    """@brief The file columns match the constants, in order."""
    assert tuple(_read_data().columns) == constants.ALL_COLUMNS


def test_data_has_expected_column_count() -> None:
    """@brief The file has as many columns as the constants state."""
    assert _read_data().shape[1] == constants.EXPECTED_COLUMNS
