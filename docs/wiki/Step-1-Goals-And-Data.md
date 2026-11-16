**English** · [Dansk](Step-1-Goals-And-Data-da) · [Bahasa Malaysia](Step-1-Goals-And-Data-ms)

# Step 1: Goals and data exploration

**Question:** What is the task, what does the Boston house price data hold, is it clean, and what do the descriptive statistics say?

![Step 1: descriptive statistics of the Boston house price data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-1-goals.png)

## What the lecture says

Lecture 597, "Day 81 Goals", puts you in Boston in the 1970s. A real estate development company wants to value a residential project before it starts, and you build the model: from the number of rooms, the distance to employment centres, how rich or poor the area is, the number of students per teacher and similar characteristics to a price estimate. The plan for the day is to explore the data, split it into training and test data, run a multivariable regression, evaluate the coefficients and the residuals, improve the model with a data transformation and value a property.

## What the code does

- `load_data` reads `boston.csv`; the first column holds the row numbers, so it becomes the index.
- `table_shape`, `column_names`, `has_nan_values` and `has_duplicates` answer the preliminary questions: 506 rows and 14 columns (13 features and the target `PRICE`), no `NaN` values and no duplicates.
- `average_students_per_teacher` gives about 18.46 pupils per teacher (`PTRATIO`), and `average_price` about 22.53, that is about $22,533, because `PRICE` is in thousands of dollars.
- `river_value_range` shows that `CHAS` only holds 0 and 1: it is a dummy variable that is 1 when the tract borders the Charles River. `river_counts` shows 471 homes away from the river and 35 next to it.
- `room_range` gives the smallest and the largest number of rooms per dwelling: about 3.56 and 8.78.
- `descriptive_table_figure` draws the descriptive statistics table in the picture above.

## What you gained

- `.shape`, `.head()`, `.tail()`, `.info()`, `.isna()` and `.duplicated()` give a first picture of any DataFrame before you model it.
- `.describe()` shows count, mean, spread and quartiles of every column at once; a minimum and a maximum already tell you what a dummy variable is.
- A model needs clean data and a clear target: here the target is `PRICE` and everything else is a feature.

Previous: [Getting-Started](Getting-Started)
