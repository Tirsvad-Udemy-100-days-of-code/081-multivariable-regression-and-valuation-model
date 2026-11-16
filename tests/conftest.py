"""@brief Shared pytest set-up: charts are drawn without a window."""

import matplotlib
import pandas as pd
import pytest

matplotlib.use("Agg")

from boston_valuation.infrastructure.csv_loader import load_data  # noqa: E402


@pytest.fixture(scope="session")
def boston_data() -> pd.DataFrame:
    """@brief Read the shipped house price table once for the whole run.

    @return The real table; tests must not change it.
    """
    return load_data()
