**English** · [Dansk](Step-7-Summary-da) · [Bahasa Malaysia](Step-7-Summary-ms)

# Step 7: Learning points and summary

**Question:** What did Day 81 teach, and where does each learning point live in the code?

![Step 7: the r-squared of both models on the training data and on the test data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-7-summary.png)

## What the lecture says

Lecture 598, "Solution & Learning Points", gives the completed notebook and seven learning points. Each one is a skill you can reuse on the next data set. The table shows where the project teaches it.

| # | Learning point | Step | Where in the code |
| --- | --- | --- | --- |
| 1 | Spot relationships in the data with a pair plot | [Step 3](Step-3-Relationships) | `pair_plot_figure`, `correlation` |
| 2 | Split the data to judge a model on data it has not seen | [Step 4](Step-4-Regression) | `split_train_test` |
| 3 | Run a multivariable regression | [Step 4](Step-4-Regression) | `fit_linear_regression`, `r_squared` |
| 4 | Check that the coefficients have the sign you expect | [Step 4](Step-4-Regression) and [Step 5](Step-5-Log-Model) | `coefficient_table`, `has_expected_signs` |
| 5 | Analyse the residuals: mean, skew and plots | [Step 4](Step-4-Regression) | `residuals`, `residual_mean`, `residual_skew` |
| 6 | Improve the model with a log transformation of the target | [Step 5](Step-5-Log-Model) | `fit_log_model`, `compare_test_r_squared` |
| 7 | Use the model to predict a price for chosen features | [Step 6](Step-6-Valuation) | `value_property` |

## What the code does

`model_scores_figure` draws the picture above from the code: the r-squared of the linear model (0.75 on the training data, 0.67 on the test data) and of the log model (0.79 and 0.74). The log model wins on both, and both lose some of their fit on the homes they have not seen. `value_property` closes the day: a described property is worth about $25,792 against $20,703 for the average one. The notebook `notebooks/boston_valuation.ipynb` walks through all six steps and is stored with its outputs.

## What you gained

- A whole workflow from a question to an answer: explore, visualise, split, fit, check, improve and use. Each stage is a small function with a test, so you can change one and see what breaks.
- A habit that matters more than any single number: judge a model on unseen data, read its coefficients and look at its residuals before you trust a prediction.
- Limits you should know. The data is from the 1970s and from 506 tracts, one feature (`B`) encodes a racial proportion, and a regression shows association, not cause. Treat the valuation as an exercise.
- Where to go next: try more features or fewer, a different split, cross-validation, regularisation (Ridge or Lasso) or a tree-based model, and compare them on the test data in the same way.

Previous: [Step-6-Valuation](Step-6-Valuation)
