"""@brief Constants used by the Day 81 analysis.

@details Every file name, column name, colour, modelling setting and scenario
value that the lectures use is defined here once, so no module repeats a magic
value.
"""

from typing import Final

## @name Data file
## @{
DATA_DIR: Final[str] = "data"
DATA_FILE: Final[str] = "boston.csv"
INDEX_COLUMN: Final[int] = 0
## @}

## @name Column names
## @{
COL_CRIM: Final[str] = "CRIM"
COL_ZN: Final[str] = "ZN"
COL_INDUS: Final[str] = "INDUS"
COL_CHAS: Final[str] = "CHAS"
COL_NOX: Final[str] = "NOX"
COL_RM: Final[str] = "RM"
COL_AGE: Final[str] = "AGE"
COL_DIS: Final[str] = "DIS"
COL_RAD: Final[str] = "RAD"
COL_TAX: Final[str] = "TAX"
COL_PTRATIO: Final[str] = "PTRATIO"
COL_B: Final[str] = "B"
COL_LSTAT: Final[str] = "LSTAT"
COL_PRICE: Final[str] = "PRICE"
FEATURE_COLUMNS: Final[tuple[str, ...]] = (
    COL_CRIM,
    COL_ZN,
    COL_INDUS,
    COL_CHAS,
    COL_NOX,
    COL_RM,
    COL_AGE,
    COL_DIS,
    COL_RAD,
    COL_TAX,
    COL_PTRATIO,
    COL_B,
    COL_LSTAT,
)
ALL_COLUMNS: Final[tuple[str, ...]] = (*FEATURE_COLUMNS, COL_PRICE)
## @}

## @name Expected shape of the data
## @{
EXPECTED_ROWS: Final[int] = 506
EXPECTED_COLUMNS: Final[int] = 14
## @}

## @name Data exploration
## @{
PREVIEW_ROWS: Final[int] = 5
RIVER_NO: Final[int] = 0
RIVER_YES: Final[int] = 1
RIVER_VALUES: Final[tuple[int, int]] = (RIVER_NO, RIVER_YES)
## @}

## @name Modelling
## @{
TEST_SIZE: Final[float] = 0.2
RANDOM_STATE: Final[int] = 10
THOUSANDS: Final[int] = 1000
## @}

## @name Chart style (descriptive table)
## @{
DESCRIPTIVE_TITLE: Final[str] = "Descriptive statistics of the Boston house price data"
DESCRIPTIVE_TITLE_FONT_SIZE: Final[int] = 16
DESCRIPTIVE_FIGURE_SIZE: Final[tuple[float, float]] = (13.0, 7.0)
DESCRIPTIVE_COLUMNS_PER_PANEL: Final[int] = 7
DESCRIPTIVE_DECIMALS: Final[int] = 2
DESCRIPTIVE_FONT_SIZE: Final[int] = 12
DESCRIPTIVE_ROW_SCALE: Final[float] = 1.7
DESCRIPTIVE_HEADER_COLOR: Final[str] = "#e3f2fd"
DESCRIPTIVE_HEADER_FONT_WEIGHT: Final[str] = "bold"
DESCRIPTIVE_EDGE_COLOR: Final[str] = "#90a4ae"
## @}

## @name Chart style (distributions)
## @{
HISTOGRAM_FIGURE_SIZE: Final[tuple[int, int]] = (10, 5)
HISTOGRAM_DPI: Final[int] = 200
COLOR_PRICE: Final[str] = "#2196f3"
PRICE_BINS: Final[int] = 50
COLOR_DIS: Final[str] = "darkblue"
COLOR_RM: Final[str] = "#00796b"
COLOR_RAD: Final[str] = "#7b1fa2"
RAD_BINS: Final[int] = 24
RAD_BAR_WIDTH: Final[float] = 0.5
DISPLOT_ASPECT: Final[int] = 2
RIVER_LABELS: Final[tuple[str, str]] = ("No", "Yes")
## @}

## @name Chart style (relationships)
## @{
JOINT_COLOR_DIS: Final[str] = "deeppink"
JOINT_COLOR_NOX: Final[str] = "darkgreen"
JOINT_COLOR_RM: Final[str] = "orange"
JOINT_COLOR_LSTAT: Final[str] = "crimson"
JOINT_COLOR_RM_PRICE: Final[str] = "darkblue"
JOINT_ALPHA: Final[float] = 0.5
JOINT_HEIGHT: Final[int] = 8
JOINT_HEIGHT_SMALL: Final[int] = 7
## @}

## @name Chart style (regression and residuals)
## @{
COLOR_LINEAR_MODEL: Final[str] = "indigo"
COLOR_LOG_MODEL: Final[str] = "navy"
COLOR_IDENTITY_LINE: Final[str] = "cyan"
RESIDUAL_ALPHA: Final[float] = 0.6
## @}

## @name Valuation scenario
## @{
NEXT_TO_RIVER: Final[bool] = True
NR_ROOMS: Final[int] = 8
STUDENTS_PER_CLASSROOM: Final[int] = 20
DISTANCE_TO_TOWN: Final[int] = 5
POLLUTION_QUANTILE: Final[float] = 0.75
POVERTY_QUANTILE: Final[float] = 0.25
## @}

## @name Step pictures
## @{
IMAGES_DIR: Final[tuple[str, str]] = ("docs", "images")
STEP_PICTURES: Final[tuple[str, ...]] = (
    "step-0-overview.png",
    "step-1-goals.png",
    "step-2-distributions.png",
    "step-3-relationships.png",
    "step-4-regression.png",
    "step-5-log-model.png",
    "step-6-valuation.png",
    "step-7-summary.png",
)
OVERVIEW_PICTURE: Final[str] = STEP_PICTURES[0]
PICTURE_DPI: Final[int] = 150
## @}

## @name Overview picture
## @{
OVERVIEW_TITLE: Final[str] = "Day 81: from data to a house valuation"
OVERVIEW_TITLE_FONT_SIZE: Final[int] = 18
OVERVIEW_FIGURE_SIZE: Final[tuple[float, float]] = (13.0, 6.0)
OVERVIEW_STEPS: Final[tuple[str, ...]] = (
    "Goals and data",
    "Distributions",
    "Relationships",
    "Split and regression",
    "Log model",
    "Valuation",
    "Summary",
)
OVERVIEW_ROW_SIZES: Final[tuple[int, int]] = (4, 3)
OVERVIEW_WRAP_WIDTH: Final[int] = 14
OVERVIEW_BOX_WIDTH: Final[float] = 2.2
OVERVIEW_BOX_HEIGHT: Final[float] = 1.3
OVERVIEW_BOX_GAP: Final[float] = 0.8
OVERVIEW_ROW_GAP: Final[float] = 2.4
OVERVIEW_BOX_PAD: Final[float] = 0.12
OVERVIEW_BOX_FACE_COLOR: Final[str] = "#e3f2fd"
OVERVIEW_BOX_EDGE_COLOR: Final[str] = COLOR_PRICE
OVERVIEW_BOX_LINEWIDTH: Final[float] = 2.0
OVERVIEW_NUMBER_FONT_SIZE: Final[int] = 20
OVERVIEW_LABEL_FONT_SIZE: Final[int] = 14
OVERVIEW_TEXT_COLOR: Final[str] = "#0d47a1"
OVERVIEW_ARROW_COLOR: Final[str] = "#455a64"
OVERVIEW_ARROW_STYLE: Final[str] = "-|>"
OVERVIEW_ARROW_SCALE: Final[int] = 22
OVERVIEW_ARROW_LINEWIDTH: Final[float] = 2.0
OVERVIEW_MARGIN: Final[float] = 0.6
OVERVIEW_TITLE_GAP: Final[float] = 0.9
## @}
