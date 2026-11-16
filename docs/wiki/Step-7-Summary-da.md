[English](Step-7-Summary) · **Dansk** · [Bahasa Malaysia](Step-7-Summary-ms)

# Trin 7: Læringspunkter og resumé

**Spørgsmål:** Hvad lærte dag 81 dig, og hvor findes hvert læringspunkt i koden?

![Trin 7: r-kvadrat for begge modeller på træningsdata og på testdata](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-7-summary.png)

## Hvad forelæsningen siger

Forelæsning 598, "Solution & Learning Points", giver den færdige notebook og syv læringspunkter. Hvert punkt er en færdighed, du kan bruge igen på næste datasæt. Tabellen viser, hvor projektet lærer det.

| # | Læringspunkt | Trin | Hvor i koden |
| --- | --- | --- | --- |
| 1 | Find sammenhænge i data med et pairplot | [Trin 3](Step-3-Relationships-da) | `pair_plot_figure`, `correlation` |
| 2 | Del data for at bedømme en model på data, den ikke har set | [Trin 4](Step-4-Regression-da) | `split_train_test` |
| 3 | Kør en multivariabel regression | [Trin 4](Step-4-Regression-da) | `fit_linear_regression`, `r_squared` |
| 4 | Kontroller, at koefficienterne har det fortegn, du forventer | [Trin 4](Step-4-Regression-da) og [Trin 5](Step-5-Log-Model-da) | `coefficient_table`, `has_expected_signs` |
| 5 | Analyser residualerne: middelværdi, skævhed og diagrammer | [Trin 4](Step-4-Regression-da) | `residuals`, `residual_mean`, `residual_skew` |
| 6 | Forbedr modellen med en log-transformation af målet | [Trin 5](Step-5-Log-Model-da) | `fit_log_model`, `compare_test_r_squared` |
| 7 | Brug modellen til at forudsige en pris for valgte egenskaber | [Trin 6](Step-6-Valuation-da) | `value_property` |

## Hvad koden gør

`model_scores_figure` tegner billedet ovenfor ud fra koden: r-kvadrat for den lineære model (0,75 på træningsdata, 0,67 på testdata) og for log-modellen (0,79 og 0,74). Log-modellen vinder begge steder, og begge mister noget af deres tilpasning på de huse, de ikke har set. `value_property` afslutter dagen: en beskrevet ejendom er cirka 25.792 dollar værd mod 20.703 dollar for den gennemsnitlige. Notebooken `notebooks/boston_valuation.ipynb` gennemgår alle seks trin og er gemt med sine resultater.

## Det får du ud af det

- En hel arbejdsgang fra et spørgsmål til et svar: udforsk, visualiser, del, tilpas, kontroller, forbedr og brug. Hvert trin er en lille funktion med en test, så du kan ændre én og se, hvad der går i stykker.
- En vane, der betyder mere end noget enkelt tal: bedøm en model på data, den ikke har set, læs dens koefficienter og se på dens residualer, før du stoler på en forudsigelse.
- Grænser, du bør kende. Data er fra 1970'erne og fra 506 områder, én variabel (`B`) koder en racemæssig andel, og en regression viser sammenhæng, ikke årsag. Se vurderingen som en øvelse.
- Videre herfra: prøv flere eller færre variabler, en anden opdeling, krydsvalidering, regularisering (Ridge eller Lasso) eller en træbaseret model, og sammenlign dem på testdata på samme måde.

Forrige: [Step-6-Valuation-da](Step-6-Valuation-da)
