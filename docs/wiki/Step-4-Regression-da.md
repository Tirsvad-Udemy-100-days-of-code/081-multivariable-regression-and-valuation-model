[English](Step-4-Regression) · **Dansk** · [Bahasa Malaysia](Step-4-Regression-ms)

# Trin 4: Opdeling og multivariabel regression

**Spørgsmål:** Hvorfor deler vi data, hvordan tilpasser vi en regression, og hvordan læser vi koefficienterne og residualerne?

![Trin 4: faktiske mod forudsagte priser, residualer mod forudsagte priser og residualernes fordeling](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-4-regression.png)

## Hvad forelæsningen siger

Forelæsningen giver de første læringspunkter om modellen: læg nogle data til side, før du tilpasser, så du kan bedømme modellen på huse, den aldrig har set. Notebooken deler tabellen 80/20 med en fast random state, så de samme huse altid havner i den samme del: 404 til træning og 102 til test (79,8 % og 20,2 %). En multivariabel regression tilpasser derefter én koefficient pr. variabel, og forelæsningen læser resultatet på tre måder: r-kvadrat på 0,75 på træningsdata, hver koefficients fortegn holdt op mod det, du forventede, og residualerne, forskellene mellem faktiske og forudsagte priser.

## Hvad koden gør

- `split_features_and_target` adskiller de 13 variabler fra `PRICE`, `split_train_test` laver 80/20-opdelingen med `random_state=10`, og `split_percentages` angiver andelene.
- `fit_linear_regression` tilpasser `LinearRegression` på træningsdata, og `r_squared` scorer den: 0,75 på træningsdata (og 0,67 på testdata, som trin 5 sammenligner med log-modellen).
- `coefficient_table` giver én koefficient pr. variabel. `room_premium` ganger koefficienten for `RM` (3,11) med 1000: ét ekstra værelse lægger cirka 3.108,5 dollar til prisen.
- `predictions`, `residuals`, `residual_mean` og `residual_skew` udfører residualanalysen: middelværdien er praktisk talt 0, og skævheden er 1,46.
- `actual_vs_predicted_figure`, `residuals_vs_predicted_figure` og `residual_distribution_figure` tegner diagrammerne i indigo med en cyan linje, hvor forudsagt er lig faktisk; `regression_panel_figure` samler dem i billedet ovenfor.

## Det får du ud af det

- En model skal bedømmes på data, den ikke har set. Den faste `random_state` gør opdelingen gentagelig, og andelen, der holdes tilbage, er et valg, du kan forsvare.
- Koefficienter fortæller en historie, du kan kontrollere: `RM` er positiv (+3,11, flere værelser koster mere), `CHAS` er positiv (+1,98, floden giver værdi), mens `LSTAT` (-0,58), `NOX` (-16,27), `DIS` (-1,48) og `PTRATIO` (-0,82) er negative. En koefficient er i enheden for sin egen variabel, så sammenlign fortegn før størrelser.
- Residualer skal ligne tilfældig støj omkring nul. Her er de centreret om 0, men skæve mod højre: modellen undervurderer nogle få dyre huse, og de afskårne priser ved 50 ses som en række punkter i det første diagram. Det er et vink om, at prisen kan transformeres, hvilket er næste trin.

Forrige: [Step-3-Relationships-da](Step-3-Relationships-da)
