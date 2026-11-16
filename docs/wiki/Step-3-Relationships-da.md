[English](Step-3-Relationships) · **Dansk** · [Bahasa Malaysia](Step-3-Relationships-ms)

# Trin 3: Sammenhænge i data

**Spørgsmål:** Hvilke variabler hænger sammen, og hvad forventer du, før du modellerer?

![Trin 3: fem sammenhænge og hver variabels korrelation med prisen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-3-relationships.png)

## Hvad forelæsningen siger

Før modellen beder notebooken dig om at gætte og derefter kontrollere. Forventer du, at forureningen er højere eller lavere langt fra arbejdspladsområderne? Hvad skal antallet af værelser gøre ved prisen, og hvad skal andelen af lavindkomstbeboere gøre? Et Seaborn-pairplot tegner alle variabler mod hinanden på én gang (det kan tage et minut eller to med alle 14 kolonner), og fem jointplots ser derefter på enkelte sammenhænge i detaljer: afstand mod forurening, industri mod forurening, fattigdom mod værelser, fattigdom mod pris og værelser mod pris. Punktdiagrammerne bruger lidt gennemsigtighed (`alpha=0.5`), så overlappende punkter kan skelnes.

## Hvad koden gør

- `pair_plot_figure` tegner pairplottet med mulighed for en regressionslinje og for et udsnit af kolonner, så test og forsøg bliver hurtige.
- `joint_plot_figure` er den ene hjælpefunktion bag `distance_pollution_figure`, `pollution_industry_figure`, `poverty_rooms_figure`, `poverty_price_figure` og `rooms_price_figure`; hver sætter opgavens farver, størrelse og `alpha`.
- `correlation` returnerer korrelationen mellem to variabler, og en navngiven hjælpefunktion for hver iagttagelse understøtter den med et tal: afstand og forurening -0,77, forurening og industri 0,76, fattigdom og værelser -0,61, fattigdom og pris -0,74, værelser og pris 0,70.
- `correlation_with_price` rangerer alle variabler efter, hvor stærkt de hænger sammen med prisen; `step_3_relationships` tegner billedet ovenfor ud fra disse tal.

## Det får du ud af det

- Forureningen falder, når afstanden til arbejdspladsområderne vokser, og stiger med andelen af industri: fabrikker og forurening hører sammen.
- Boliger i fattigere områder (høj `LSTAT`) har færre værelser og lavere priser, og flere værelser betyder højere pris. Det er de fortegn, du forventer, at regressionen giver.
- Variabler kan hænge sammen med hinanden og ikke kun med prisen (`RAD` og `TAX` har en korrelation på 0,91). Det kaldes multikollinearitet og er en grund til at være forsigtig, når du senere læser koefficienterne.
- En korrelation er kun et tal for en retlinet sammenhæng; punktdiagrammet viser, om formen virkelig er en linje, så se på begge dele.

Forrige: [Step-2-Distributions-da](Step-2-Distributions-da)
