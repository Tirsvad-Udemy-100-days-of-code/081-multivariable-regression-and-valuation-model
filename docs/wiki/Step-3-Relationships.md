**English** · [Dansk](Step-3-Relationships-da) · [Bahasa Malaysia](Step-3-Relationships-ms)

# Step 3: Relationships in the data

**Question:** Which features move together, and what do you expect before you model?

![Step 3: five relationships and the correlation of every feature with the price](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-3-relationships.png)

## What the lecture says

Before the model, the notebook asks you to make predictions and then check them. Would you expect pollution to be higher or lower far from the employment centres? What should the number of rooms do to the price, and what should the share of low-income residents do? A Seaborn pair plot draws every feature against every other in one go (it can take a minute or two on all 14 columns), and five joint plots then look at single relationships in detail: distance against pollution, industry against pollution, poverty against rooms, poverty against price and rooms against price. The scatter plots use some transparency (`alpha=0.5`) so that overlapping points can be told apart.

## What the code does

- `pair_plot_figure` draws the pair plot, with an option for a regression line and one for a subset of columns, which keeps tests and experiments fast.
- `joint_plot_figure` is the one helper behind `distance_pollution_figure`, `pollution_industry_figure`, `poverty_rooms_figure`, `poverty_price_figure` and `rooms_price_figure`; each sets the colours, the size and the `alpha` of the assignment.
- `correlation` returns the correlation of two features, and a named helper for each observation backs it with a number: distance and pollution -0.77, pollution and industry 0.76, poverty and rooms -0.61, poverty and price -0.74, rooms and price 0.70.
- `correlation_with_price` ranks all features by how strongly they relate to the price; `step_3_relationships` draws the picture above from these numbers.

## What you gained

- Pollution falls as the distance to the employment centres grows and rises with the share of industry: factories and pollution go together.
- Homes in poorer areas (high `LSTAT`) have fewer rooms and lower prices, and more rooms mean a higher price. These are the signs you expect the regression to give.
- Features can be related to each other as well as to the price (`RAD` and `TAX` have a correlation of 0.91). That is called multicollinearity, and it is a reason to be careful when you read the coefficients later.
- A correlation is only a number for a straight-line relationship; the scatter plot shows whether the shape is really a line, so look at both.

Previous: [Step-2-Distributions](Step-2-Distributions)
