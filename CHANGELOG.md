# Changelog

All notable changes to this project are written here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the versions follow
[Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.0.0] - 2026-11-16

Day 81 of Udemy's 100 Days of Code, "Predict House Prices": a tested, documented Python 3.13+ project that builds a multivariable regression on the Boston house price data and values a property.

### Added

- The `boston_valuation` package with a domain layer, an infrastructure layer and a presentation layer, all constants in `constants.py` and Doxygen comments.
- Step 1: the CSV loader, the exploration checks (shape, columns, `NaN` values, duplicates) and the descriptive statistics.
- Step 2: the price, distance, rooms and highway access distribution charts and the Plotly river bar chart.
- Step 3: the pair plot, the five joint plots and the correlation helpers.
- Step 4: the 80/20 split, the linear regression, the coefficient table, the room premium and the residual analysis with charts.
- Step 5: the log transformation, the log model on the same split and the comparison of both models on the test data.
- Step 6: the average property, `value_property` and the valuation chart.
- Step 7: the lecture 598 learning points and the summary chart.
- A picture for every step, generated from the project's own output by `python -m boston_valuation.presentation.screenshots`.
- The notebook `notebooks/boston_valuation.ipynb`, stored with its outputs.
- A wiki in English, Danish and Bahasa Malaysia with a Getting Started guide for Linux and Windows and one page for each step.
- Project documents under `docs/` (Business Case, Stakeholder Analysis, Project Plan, milestones, review records and traceability matrix) made with the SQA and QC framework.
- 364 pytest tests.
