**English** · [Dansk](Step-5-Log-Model-da) · [Bahasa Malaysia](Step-5-Log-Model-ms)

# Step 5: The log transformation

**Question:** Can a log transformation of the price give a better fit, and how do we compare models on unseen data?

![Step 5: the linear model and the log price model side by side](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-5-log-model.png)

## What the lecture says

The residuals of the first model were skewed to the right, and the price itself is skewed (1.11). The lecture's idea is to transform the target: take the natural logarithm of the price, fit the same regression on it, and see whether the residuals look more like noise. The notebook shows how the log squeezes the large prices, then re-uses the same 80/20 split so the two models are judged on the same homes. The log model fits the training data better (r-squared 0.79 against 0.75), and the residuals are almost symmetric. The final check is the test data: both models score lower there than on the training data, and the log model is still better.

## What the code does

- `price_skew`, `log_price` and `log_price_skew` give the skew of the price (1.11) and of the log price (-0.33). `price_skew_figure`, `log_price_skew_figure` and `log_mapping_figure` draw the two distributions and the curve that maps a price to its log.
- `fit_linear_model` and `fit_log_model` fit the two models on the same split (the same 404 and 102 rows because `random_state` is fixed) and keep the training and test r-squared, the predictions and the residuals together.
- `log_coefficient_table` returns the coefficients of the log model, and `has_expected_signs` checks them: `CHAS` +0.080, `RM` +0.073, `PTRATIO` -0.035, `LSTAT` -0.031 and `NOX` -0.704.
- `compare_test_r_squared` returns the test-set r-squared of both models: 0.67 for the linear model and 0.74 for the log model.
- `log_actual_vs_predicted_figure`, `log_residuals_vs_predicted_figure` and `log_residual_distribution_figure` draw the log model in navy; `model_comparison_panel_figure` puts the indigo linear model and the navy log model in the picture above.

## What you gained

- A skewed target can be transformed. The skew of the price falls from 1.11 to -0.33 with a log, and the skew of the residuals falls from 1.46 to 0.09, so the errors are much closer to a bell curve.
- Coefficients of a log model are relative changes: one extra student per teacher (`PTRATIO`, -0.035) lowers the price by roughly 3.5 %, and a home next to the river (`CHAS`, +0.080) is worth about 8 % more, other things equal.
- The training r-squared always looks better than it should. Compare models on the test data: here 0.67 against 0.74, so the better fit is not an illusion.
- A prediction from the log model is a log price. Turn it back into dollars with the exponential function, which is what the next step does.

Previous: [Step-4-Regression](Step-4-Regression)
