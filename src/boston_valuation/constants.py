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
DISTANCE_BINS: Final[int] = 50
RAD_EDGE_COLOR: Final[str] = "black"
RIVER_LABELS: Final[tuple[str, str]] = ("No", "Yes")
RIVER_COLOR_SCALE: Final[str] = "haline"
## @}

## @name Chart text (distributions)
## @{
HOMES_Y_LABEL: Final[str] = "Nr. of Homes"
PRICE_TITLE: Final[str] = "1970s Home Values in Boston. Average: {average:.2f} ($1000s)"
PRICE_X_LABEL: Final[str] = "Price in 000s"
DISTANCE_TITLE: Final[str] = "Distance to Employment Centres. Average: {average:.2f}"
DISTANCE_X_LABEL: Final[str] = "Weighted Distance to 5 Boston Employment Centres"
ROOMS_TITLE: Final[str] = "Distribution of Rooms in Boston. Average: {average:.2f}"
ROOMS_X_LABEL: Final[str] = "Average Number of Rooms"
RAD_TITLE: Final[str] = "Accessibility to Highways"
RAD_X_LABEL: Final[str] = "Accessibility to Highways"
RAD_Y_LABEL: Final[str] = "Nr. of Houses"
RIVER_TITLE: Final[str] = "Next to Charles River?"
RIVER_X_LABEL: Final[str] = "Property Located Next to the River?"
RIVER_Y_LABEL: Final[str] = "Number of Homes"
## @}

## @name Step 2 picture
## @{
PANEL_TITLE: Final[str] = "Distributions of price, distance, rooms and highway access"
PANEL_TITLE_FONT_SIZE: Final[int] = 16
PANEL_AXES_TITLE_FONT_SIZE: Final[int] = 11
PANEL_FIGURE_SIZE: Final[tuple[float, float]] = (13.0, 8.0)
PANEL_ROWS: Final[int] = 2
PANEL_COLUMNS: Final[int] = 2
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
JOINT_KIND: Final[str] = "scatter"
JOINT_STYLE_DARK: Final[str] = "darkgrid"
JOINT_STYLE_LIGHT: Final[str] = "whitegrid"
PAIR_REGRESSION_LINE_COLOR: Final[str] = "cyan"
## @}

## @name Relationships of the assignment
## @{
PAIR_DISTANCE_POLLUTION: Final[tuple[str, str]] = (COL_DIS, COL_NOX)
PAIR_POLLUTION_INDUSTRY: Final[tuple[str, str]] = (COL_NOX, COL_INDUS)
PAIR_POVERTY_ROOMS: Final[tuple[str, str]] = (COL_LSTAT, COL_RM)
PAIR_POVERTY_PRICE: Final[tuple[str, str]] = (COL_LSTAT, COL_PRICE)
PAIR_ROOMS_PRICE: Final[tuple[str, str]] = (COL_RM, COL_PRICE)
RELATIONSHIP_PAIRS: Final[tuple[tuple[str, str], ...]] = (
    PAIR_DISTANCE_POLLUTION,
    PAIR_POLLUTION_INDUSTRY,
    PAIR_POVERTY_ROOMS,
    PAIR_POVERTY_PRICE,
    PAIR_ROOMS_PRICE,
)
RELATIONSHIP_COLORS: Final[tuple[str, ...]] = (
    JOINT_COLOR_DIS,
    JOINT_COLOR_NOX,
    JOINT_COLOR_RM,
    JOINT_COLOR_LSTAT,
    JOINT_COLOR_RM_PRICE,
)
## @}

## @name Step 3 picture
## @{
RELATIONSHIP_PANEL_TITLE: Final[str] = (
    "Relationships between the features and the price"
)
RELATIONSHIP_PANEL_ROWS: Final[int] = 2
RELATIONSHIP_PANEL_COLUMNS: Final[int] = 3
RELATIONSHIP_PANEL_FIGURE_SIZE: Final[tuple[float, float]] = (15.0, 8.5)
RELATIONSHIP_SCATTER_SIZE: Final[int] = 14
RELATIONSHIP_PAIR_TITLE: Final[str] = "{first} vs {second}, r = {value:.2f}"
CORRELATION_BARS_TITLE: Final[str] = "Correlation with PRICE"
CORRELATION_BARS_X_LABEL: Final[str] = "Correlation coefficient (r)"
CORRELATION_COLOR_POSITIVE: Final[str] = "#2e7d32"
CORRELATION_COLOR_NEGATIVE: Final[str] = "#c62828"
CORRELATION_AXIS_LIMIT: Final[float] = 1.0
CORRELATION_ZERO_LINE_COLOR: Final[str] = "black"
CORRELATION_ZERO_LINE_WIDTH: Final[float] = 0.8
## @}

## @name Chart style (regression and residuals)
## @{
COLOR_LINEAR_MODEL: Final[str] = "indigo"
COLOR_LOG_MODEL: Final[str] = "navy"
COLOR_IDENTITY_LINE: Final[str] = "cyan"
RESIDUAL_ALPHA: Final[float] = 0.6
REGRESSION_FIGURE_SIZE: Final[tuple[float, float]] = (6.4, 4.8)
REGRESSION_DPI: Final[int] = 100
REGRESSION_TITLE_FONT_SIZE: Final[int] = 17
REGRESSION_LABEL_FONT_SIZE: Final[int] = 14
## @}

## @name Regression (step 4)
## @{
PERCENT: Final[int] = 100
COEFFICIENT_COLUMN: Final[str] = "Coefficient"
RESIDUAL_DECIMALS: Final[int] = 2
## @}

## @name Chart text (regression and residuals)
## @{
ACTUAL_VS_PREDICTED_TITLE: Final[str] = (
    r"Actual vs Predicted Prices: $y _i$ vs $\hat y_i$"
)
ACTUAL_PRICE_X_LABEL: Final[str] = r"Actual prices 000s $y _i$"
PREDICTED_PRICE_Y_LABEL: Final[str] = r"Predicted prices 000s $\hat y _i$"
RESIDUALS_VS_PREDICTED_TITLE: Final[str] = "Residuals vs Predicted Values"
PREDICTED_PRICE_X_LABEL: Final[str] = r"Predicted Prices $\hat y _i$"
RESIDUALS_LABEL: Final[str] = "Residuals"
RESIDUAL_DISTRIBUTION_TITLE: Final[str] = (
    "{prefix}Residuals Skew ({skew}) Mean ({mean})"
)
RESIDUAL_COUNT_LABEL: Final[str] = "Count"
## @}

## @name Step 4 picture
## @{
REGRESSION_PANEL_TITLE: Final[str] = (
    "Linear regression on the training data: r-squared {r_squared:.2f}, "
    "one extra room adds ${premium:.1f}"
)
REGRESSION_PANEL_COLUMNS: Final[int] = 3
REGRESSION_PANEL_FIGURE_SIZE: Final[tuple[float, float]] = (15.0, 5.5)
## @}

## @name Log transformation (step 5)
## @{
COLOR_PRICE_SKEW: Final[str] = "green"
LOG_MAPPING_DPI: Final[int] = 150
EXPECTED_SIGN_POSITIVE: Final[int] = 1
EXPECTED_SIGN_NEGATIVE: Final[int] = -1
LOG_EXPECTED_SIGNS: Final[tuple[tuple[str, int], ...]] = (
    (COL_CHAS, EXPECTED_SIGN_POSITIVE),
    (COL_RM, EXPECTED_SIGN_POSITIVE),
    (COL_PTRATIO, EXPECTED_SIGN_NEGATIVE),
    (COL_LSTAT, EXPECTED_SIGN_NEGATIVE),
    (COL_NOX, EXPECTED_SIGN_NEGATIVE),
)
LOG_COEFFICIENT_COLUMN: Final[str] = "coef"
## @}

## @name Chart text (log transformation)
## @{
PRICE_SKEW_TITLE: Final[str] = "Normal Prices. Skew is {skew:.2f}"
LOG_PRICE_SKEW_TITLE: Final[str] = "Log Prices. Skew is {skew:.2f}"
LOG_PRICE_X_LABEL: Final[str] = "Log Price"
DISTRIBUTION_COUNT_LABEL: Final[str] = "Count"
LOG_MAPPING_TITLE: Final[str] = "Mapping the Original Price to a Log Price"
LOG_MAPPING_X_LABEL: Final[str] = "Actual $ Price in 000s"
LOG_MAPPING_Y_LABEL: Final[str] = "Log Price"
LOG_ACTUAL_VS_PREDICTED_PANEL_TITLE: Final[str] = (
    r"Actual vs Predicted Log Prices: $y _i$ vs $\hat y_i$"
)
R_SQUARED_TITLE_SUFFIX: Final[str] = " (R-Squared {r_squared:.2f})"
LOG_ACTUAL_VS_PREDICTED_TITLE: Final[str] = (
    LOG_ACTUAL_VS_PREDICTED_PANEL_TITLE + R_SQUARED_TITLE_SUFFIX
)
LOG_ACTUAL_X_LABEL: Final[str] = r"Actual Log Prices $y _i$"
LOG_PREDICTED_Y_LABEL: Final[str] = r"Predicted Log Prices $\hat y _i$"
LOG_RESIDUALS_VS_PREDICTED_TITLE: Final[str] = (
    "Residuals vs Fitted Values for Log Prices"
)
LOG_PREDICTED_X_LABEL: Final[str] = r"Predicted Log Prices $\hat y _i$"
LOG_RESIDUAL_PREFIX: Final[str] = "Log price model: "
ORIGINAL_RESIDUAL_PREFIX: Final[str] = "Original model: "
## @}

## @name Step 5 picture
## @{
COMPARISON_PANEL_TITLE: Final[str] = (
    "Linear vs log price model: training r-squared {linear_train:.2f} vs "
    "{log_train:.2f}, test r-squared {linear_test:.2f} vs {log_test:.2f}"
)
LINEAR_ROW_TITLE: Final[str] = (
    "Linear model on the price (indigo): training r-squared {train:.2f}, "
    "test r-squared {test:.2f}"
)
LOG_ROW_TITLE: Final[str] = (
    "Linear model on the log price (navy): training r-squared {train:.2f}, "
    "test r-squared {test:.2f}"
)
COMPARISON_PANEL_ROWS: Final[int] = 2
COMPARISON_PANEL_COLUMNS: Final[int] = 3
COMPARISON_PANEL_FIGURE_SIZE: Final[tuple[float, float]] = (14.0, 9.0)
COMPARISON_ROW_TITLE_FONT_SIZE: Final[int] = 13
## @}

## @name Valuation scenario
## @{
NEXT_TO_RIVER: Final[bool] = True
NR_ROOMS: Final[int] = 8
STUDENTS_PER_CLASSROOM: Final[int] = 20
DISTANCE_TO_TOWN: Final[int] = 5
POLLUTION_QUANTILE: Final[float] = 0.75
POVERTY_QUANTILE: Final[float] = 0.25
VALUATION_CHANGED_FEATURES: Final[tuple[str, ...]] = (
    COL_RM,
    COL_PTRATIO,
    COL_DIS,
    COL_CHAS,
    COL_NOX,
    COL_LSTAT,
)
VALUATION_FEATURE_LABELS: Final[tuple[str, ...]] = (
    "RM (rooms)",
    "PTRATIO (students per teacher)",
    "DIS (distance to town)",
    "CHAS (next to river)",
    "NOX (pollution)",
    "LSTAT (poverty)",
)
AVERAGE_PROPERTY_LABEL: Final[str] = "Average property"
DESCRIBED_PROPERTY_LABEL: Final[str] = "Described property"
FEATURE_COLUMN_LABEL: Final[str] = "Feature"
## @}

## @name Step 6 picture
## @{
VALUATION_PANEL_TITLE: Final[str] = (
    "Valuation with the log model: log estimate {average_log:.2f} for the "
    "average property, {described_log:.2f} for the described property"
)
VALUATION_PANEL_TITLE_FONT_SIZE: Final[int] = 14
VALUATION_PANEL_FIGURE_SIZE: Final[tuple[float, float]] = (13.0, 6.0)
VALUATION_PANEL_WIDTH_RATIOS: Final[tuple[float, float]] = (1.0, 1.35)
VALUATION_BARS_TITLE: Final[str] = "Estimated value in dollars"
VALUATION_BARS_Y_LABEL: Final[str] = "Estimated value ($)"
VALUATION_DOLLAR_FORMAT: Final[str] = "${value:,.0f}"
VALUATION_AXIS_FORMAT: Final[str] = "${x:,.0f}"
VALUATION_BAR_WIDTH: Final[float] = 0.55
VALUATION_BAR_LABEL_FONT_SIZE: Final[int] = 14
VALUATION_BAR_HEADROOM: Final[float] = 1.12
VALUATION_TABLE_TITLE: Final[str] = "Characteristics that change"
VALUATION_TABLE_FONT_SIZE: Final[int] = 11
VALUATION_TABLE_ROW_SCALE: Final[float] = 1.9
VALUATION_TABLE_DECIMALS: Final[int] = 2
VALUATION_TABLE_COLUMN_WIDTHS: Final[tuple[float, float, float]] = (0.45, 0.26, 0.29)
## @}

## @name Step 7 picture
## @{
SUMMARY_TITLE: Final[str] = (
    "Out of sample: the log model keeps its lead on unseen homes"
)
SUMMARY_SUBTITLE: Final[str] = (
    "Both scores are lower on the test data than on the training data"
)
SUMMARY_GROUP_LABELS: Final[tuple[str, str]] = ("Training data", "Test data")
SUMMARY_LINEAR_LEGEND: Final[str] = "Linear model on the price"
SUMMARY_LOG_LEGEND: Final[str] = "Log model on the log price"
SUMMARY_Y_LABEL: Final[str] = "r-squared"
SUMMARY_Y_LIMITS: Final[tuple[float, float]] = (0.0, 1.0)
SUMMARY_SCORE_FORMAT: Final[str] = "{value:.2f}"
SUMMARY_FIGURE_SIZE: Final[tuple[float, float]] = (9.0, 6.0)
SUMMARY_TITLE_FONT_SIZE: Final[int] = 15
SUMMARY_SUBTITLE_FONT_SIZE: Final[int] = 12
SUMMARY_BAR_WIDTH: Final[float] = 0.36
SUMMARY_BAR_OFFSET: Final[float] = SUMMARY_BAR_WIDTH / 2
SUMMARY_BAR_LABEL_FONT_SIZE: Final[int] = 13
SUMMARY_TICK_FONT_SIZE: Final[int] = 13
SUMMARY_LEGEND_COLUMNS: Final[int] = 2
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
