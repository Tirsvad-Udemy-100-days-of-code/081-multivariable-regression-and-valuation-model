**English** · [Dansk](Step-2-Distributions-da) · [Bahasa Malaysia](Step-2-Distributions-ms)

# Step 2: Feature distributions

**Question:** How are prices, commutes, rooms and highway access distributed, and how many homes touch the river?

![Step 2: distributions of price, distance, rooms and highway access](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-2-distributions.png)

## What the lecture says

Before you model anything, the notebook asks you to look at the features one at a time. The price, the distance to the five employment centres and the number of rooms get a histogram with a smooth curve on top (a Kernel Density Estimate, KDE) from Seaborn, and the average goes into the title. Highway access is a plain Matplotlib histogram, and the river dummy is a Plotly bar chart with the labels No and Yes. The point is to see the shape of the data: where most homes are, where the tails are and whether anything looks odd.

## What the code does

- `price_distribution_figure` draws the price with a KDE, 50 bins and a wide shape (`aspect=2`); `price_title` puts the average, 22.53 thousand dollars, in the title.
- `distance_distribution_figure` and `rooms_distribution_figure` do the same for `DIS` (average 3.80) and `RM` (average 6.28); `average_distance` and `average_rooms` compute the averages in the domain layer.
- `highway_access_figure` is a Matplotlib histogram of `RAD` with 24 bins, black edges and narrow bars; `highway_access_counts` gives the counts behind it.
- `river_bar_chart` returns a Plotly figure with the two bars No (471 homes) and Yes (35 homes); `river_counts_by_label` gives the counts with those labels.
- `distribution_panel_figure` puts price, distance, rooms and highway access in the picture above.

## What you gained

- The price is skewed to the right: most homes cost around 21 thousand dollars (the median is 21.2), a few cost much more, and 16 tracts sit exactly at the cap of 50.
- The distance to employment centres is skewed to the right as well; the rooms are close to a bell shape around 6.3.
- Highway access is not a smooth variable: it takes the values 1 to 8 and then jumps to 24, which holds 132 of the 506 tracts. A histogram with wide bins would hide that gap.
- Only 35 of 506 tracts border the river, so a bar chart of a dummy variable tells you quickly how rare the group is.
- A KDE curve helps you judge the shape, but only the bars show the real counts; use both.

Previous: [Step-1-Goals-And-Data](Step-1-Goals-And-Data)
