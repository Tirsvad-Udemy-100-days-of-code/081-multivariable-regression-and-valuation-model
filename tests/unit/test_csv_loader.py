"""@brief Tests for the CSV loader."""

from pathlib import Path

import pytest

from boston_valuation import constants
from boston_valuation.infrastructure import csv_loader

SMALL_CSV = "idx,CRIM,PRICE\n0,0.1,24.0\n1,0.2,21.6\n"


def test_load_data_has_expected_shape() -> None:
    """@brief The packaged file has 506 rows and 14 columns."""
    data = csv_loader.load_data()
    assert data.shape == (constants.EXPECTED_ROWS, constants.EXPECTED_COLUMNS)


def test_load_data_has_columns_in_file_order() -> None:
    """@brief The index column is dropped and the others keep their order."""
    data = csv_loader.load_data()
    assert tuple(data.columns) == constants.ALL_COLUMNS


def test_load_data_from_reads_given_file(tmp_path: Path) -> None:
    """@brief A file chosen by the caller is read with its first column as index."""
    path = tmp_path / "small.csv"
    path.write_text(SMALL_CSV, encoding="utf-8")
    data = csv_loader.load_data_from(path)
    assert list(data.columns) == ["CRIM", "PRICE"]


def test_load_data_from_keeps_values(tmp_path: Path) -> None:
    """@brief The values of the file are not changed."""
    path = tmp_path / "small.csv"
    path.write_text(SMALL_CSV, encoding="utf-8")
    data = csv_loader.load_data_from(path)
    assert data["PRICE"].tolist() == pytest.approx([24.0, 21.6])


def test_load_data_from_raises_for_missing_file(tmp_path: Path) -> None:
    """@brief A path that does not exist is reported, not hidden."""
    with pytest.raises(FileNotFoundError):
        csv_loader.load_data_from(tmp_path / "missing.csv")
