[English](Step-5-Log-Model) · **Dansk** · [Bahasa Malaysia](Step-5-Log-Model-ms)

# Trin 5: Log-transformationen

**Spørgsmål:** Kan en log-transformation af prisen give en bedre tilpasning, og hvordan sammenligner vi modeller på data, de ikke har set?

![Trin 5: den lineære model og log-prismodellen side om side](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-5-log-model.png)

## Hvad forelæsningen siger

Den første models residualer var skæve mod højre, og selve prisen er skæv (1,11). Forelæsningens idé er at transformere målet: tag den naturlige logaritme af prisen, tilpas den samme regression på den, og se, om residualerne ligner støj mere. Notebooken viser, hvordan logaritmen presser de store priser sammen, og genbruger derefter den samme 80/20-opdeling, så de to modeller bedømmes på de samme huse. Log-modellen passer bedre til træningsdata (r-kvadrat 0,79 mod 0,75), og residualerne er næsten symmetriske. Den sidste kontrol er testdata: begge modeller scorer lavere der end på træningsdata, og log-modellen er stadig bedst.

## Hvad koden gør

- `price_skew`, `log_price` og `log_price_skew` giver skævheden af prisen (1,11) og af logprisen (-0,33). `price_skew_figure`, `log_price_skew_figure` og `log_mapping_figure` tegner de to fordelinger og kurven, der afbilder en pris på dens logaritme.
- `fit_linear_model` og `fit_log_model` tilpasser de to modeller på samme opdeling (de samme 404 og 102 rækker, fordi `random_state` er fast) og gemmer trænings- og test-r-kvadrat, forudsigelser og residualer sammen.
- `log_coefficient_table` giver log-modellens koefficienter, og `has_expected_signs` kontrollerer dem: `CHAS` +0,080, `RM` +0,073, `PTRATIO` -0,035, `LSTAT` -0,031 og `NOX` -0,704.
- `compare_test_r_squared` giver test-r-kvadrat for begge modeller: 0,67 for den lineære model og 0,74 for log-modellen.
- `log_actual_vs_predicted_figure`, `log_residuals_vs_predicted_figure` og `log_residual_distribution_figure` tegner log-modellen i marineblå; `model_comparison_panel_figure` samler den indigofarvede lineære model og den marineblå log-model i billedet ovenfor.

## Det får du ud af det

- Et skævt mål kan transformeres. Prisens skævhed falder fra 1,11 til -0,33 med en logaritme, og residualernes skævhed falder fra 1,46 til 0,09, så fejlene ligger meget tættere på en klokkekurve.
- Koefficienterne i en log-model er relative ændringer: én ekstra elev pr. lærer (`PTRATIO`, -0,035) sænker prisen med cirka 3,5 %, og et hus ved floden (`CHAS`, +0,080) er cirka 8 % mere værd, alt andet lige.
- Trænings-r-kvadrat ser altid bedre ud, end det bør. Sammenlign modeller på testdata: her 0,67 mod 0,74, så den bedre tilpasning er ikke en illusion.
- En forudsigelse fra log-modellen er en logpris. Omregn den til dollar med eksponentialfunktionen, hvilket næste trin gør.

Forrige: [Step-4-Regression-da](Step-4-Regression-da)
