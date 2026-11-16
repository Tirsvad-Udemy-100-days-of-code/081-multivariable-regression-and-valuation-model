"""@brief Read the Boston house price table from a CSV file."""

from pathlib import Path

import pandas as pd

from boston_valuation import constants


def load_data_from(path: Path) -> pd.DataFrame:
    """@brief Read a house price table from a CSV file.

    @param path CSV file whose first column is the unnamed row index.
    @return The table, one row per census tract, without the index column.
    """
    return pd.read_csv(path, index_col=constants.INDEX_COLUMN)


def load_data() -> pd.DataFrame:
    """@brief Read the house price table that ships with the package.

    @return The 506 rows and 14 columns of the Boston data.
    """
    package_root = Path(__file__).resolve().parents[1]
    return load_data_from(package_root / constants.DATA_DIR / constants.DATA_FILE)
