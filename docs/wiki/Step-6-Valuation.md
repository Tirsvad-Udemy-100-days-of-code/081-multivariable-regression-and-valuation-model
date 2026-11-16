**English** · [Dansk](Step-6-Valuation-da) · [Bahasa Malaysia](Step-6-Valuation-ms)

# Step 6: Valuing a property

**Question:** How do you use the model to value an average house and a house you describe?

![Step 6: the estimated value of the average property and of the described property](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-6-valuation.png)

## What the lecture says

Now the model answers the business question. The notebook starts from the average property, a row that holds the mean of every feature, and asks the log model for an estimate: a log price of 3.03. The exponential function turns that back into a price in thousands of dollars, and times 1000 it is about $20,703. Then the notebook describes a property: next to the river, 8 rooms, 20 students per teacher, 5 units from the employment centres, high pollution (the 75th percentile of `NOX`) and low poverty (the 25th percentile of `LSTAT`). All other features keep their averages. The log estimate is 3.25, which is about $25,792.

## What the code does

- `average_property` builds the one-row table with the mean of the 13 features.
- `estimate_value` asks the model for the log estimate and turns it into dollars with `exp` and the factor 1000; it returns both numbers in a `ValueEstimate`.
- `described_property` starts from the average property and sets the six characteristics: the river (`CHAS`), the rooms (`RM`), the students per teacher (`PTRATIO`), the distance (`DIS`), the pollution (`NOX`) and the poverty (`LSTAT`).
- `value_property` is the function of the assignment: the characteristics are parameters with the values of the lecture as defaults, it fits the log model when you do not pass one, and it returns the estimate. It rejects values that cannot be real, such as zero rooms.
- `property_characteristics` lists what changes against the average, and `valuation_figure` draws the picture above.

## What you gained

- A model is only useful when you can ask it a question: you describe a property in the feature columns and get a price back. The features you do not know stay at the average, which is a reasonable default.
- A log model predicts a log price. Reverse the transformation with `exp` before you talk about dollars, and remember the unit: the price is in thousands.
- The described property is worth about 25 % more than the average one ($25,792 against $20,703), because the extra rooms, the river and the low poverty outweigh the higher pollution and the larger classes.
- The dollars are 1970s dollars and the model is trained on 506 tracts; the estimate is a starting point for a conversation, not a price tag. Remember also that the column `B` encodes a racial proportion, so this model should never be used in practice.

Previous: [Step-5-Log-Model](Step-5-Log-Model)
