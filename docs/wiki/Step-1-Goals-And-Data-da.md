[English](Step-1-Goals-And-Data) · **Dansk** · [Bahasa Malaysia](Step-1-Goals-And-Data-ms)

# Trin 1: Mål og dataudforskning

**Spørgsmål:** Hvad er opgaven, hvad indeholder Boston-boligdata, er de rene, og hvad siger de beskrivende statistikker?

![Trin 1: beskrivende statistik for Boston-boligdata](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-1-goals.png)

## Hvad forelæsningen siger

Forelæsning 597, "Day 81 Goals", sætter dig i Boston i 1970'erne. Et ejendomsudviklingsselskab vil vurdere et boligprojekt, før det starter, og du bygger modellen: fra antal værelser, afstand til arbejdspladsområder, hvor rigt eller fattigt området er, antal elever pr. lærer og lignende egenskaber til et prisoverslag. Dagens plan er at udforske data, dele dem i trænings- og testdata, køre en multivariabel regression, vurdere koefficienter og residualer, forbedre modellen med en datatransformation og vurdere en ejendom.

## Hvad koden gør

- `load_data` læser `boston.csv`; første kolonne indeholder rækkenumre, så den bliver indekset.
- `table_shape`, `column_names`, `has_nan_values` og `has_duplicates` besvarer de indledende spørgsmål: 506 rækker og 14 kolonner (13 variabler og målet `PRICE`), ingen `NaN`-værdier og ingen dubletter.
- `average_students_per_teacher` giver cirka 18,46 elever pr. lærer (`PTRATIO`), og `average_price` cirka 22,53, altså cirka 22.533 dollar, fordi `PRICE` er i tusinde dollar.
- `river_value_range` viser, at `CHAS` kun indeholder 0 og 1: det er en dummyvariabel, som er 1, når området grænser op til Charles River. `river_counts` viser 471 huse væk fra floden og 35 ved floden.
- `room_range` giver det mindste og det største antal værelser pr. bolig: cirka 3,56 og 8,78.
- `descriptive_table_figure` tegner tabellen med beskrivende statistik i billedet ovenfor.

## Det får du ud af det

- `.shape`, `.head()`, `.tail()`, `.info()`, `.isna()` og `.duplicated()` giver et første billede af enhver DataFrame, før du modellerer.
- `.describe()` viser antal, gennemsnit, spredning og kvartiler for alle kolonner på én gang; et minimum og et maksimum fortæller allerede, hvad en dummyvariabel er.
- En model har brug for rene data og et klart mål: her er målet `PRICE`, og alt andet er variabler.

Forrige: [Getting-Started-da](Getting-Started-da)
