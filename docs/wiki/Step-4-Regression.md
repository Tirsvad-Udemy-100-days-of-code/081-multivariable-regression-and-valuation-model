**English** · [Dansk](Step-4-Regression-da) · [Bahasa Malaysia](Step-4-Regression-ms)

# Step 4: Split and multivariable regression

**Question:** Why do we split the data, how do we fit a regression, and how do we read the coefficients and the residuals?

![Step 4: actual against predicted prices, residuals against predicted prices and the residual distribution](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-4-regression.png)

## What the lecture says

The lecture gives the first learning points of the model: set some data aside before you fit, so that you can judge the model on homes it has never seen. The notebook splits the table 80/20 with a fixed random state, so the same homes always land in the same part: 404 for training and 102 for testing (79.8 % and 20.2 %). A multivariable regression then fits one coefficient per feature, and the lecture reads the result in three ways: the r-squared of 0.75 on the training data, the sign of each coefficient against what you expected, and the residuals, the gaps between actual and predicted prices.

## What the code does

- `split_features_and_target` separates the 13 features from `PRICE`, `split_train_test` does the 80/20 split with `random_state=10`, and `split_percentages` reports the shares.
- `fit_linear_regression` fits `LinearRegression` on the training data and `r_squared` scores it: 0.75 on the training data (and 0.67 on the test data, which step 5 compares with the log model).
- `coefficient_table` returns one coefficient per feature. `room_premium` multiplies the coefficient of `RM` (3.11) by 1000: one extra room adds about $3,108.5 to the price.
- `predictions`, `residuals`, `residual_mean` and `residual_skew` do the residual analysis: the mean is practically 0 and the skew is 1.46.
- `actual_vs_predicted_figure`, `residuals_vs_predicted_figure` and `residual_distribution_figure` draw the charts in indigo with a cyan line where predicted equals actual; `regression_panel_figure` puts them in the picture above.

## What you gained

- A model must be judged on data it has not seen. The fixed `random_state` makes the split repeatable, and the share held back is a choice you can defend.
- Coefficients tell a story you can check: `RM` is positive (+3.11, more rooms cost more), `CHAS` is positive (+1.98, the river adds value), while `LSTAT` (-0.58), `NOX` (-16.27), `DIS` (-1.48) and `PTRATIO` (-0.82) are negative. A coefficient is in the unit of its own feature, so compare signs before sizes.
- Residuals should look like random noise around zero. Here they are centred on 0 but skewed to the right: the model underestimates a few expensive homes, and the capped prices at 50 show up as a row of points in the first chart. That is the hint that the price might be transformed, which is the next step.

Previous: [Step-3-Relationships](Step-3-Relationships)
