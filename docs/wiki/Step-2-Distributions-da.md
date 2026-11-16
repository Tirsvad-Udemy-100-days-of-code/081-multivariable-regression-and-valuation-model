[English](Step-2-Distributions) · **Dansk** · [Bahasa Malaysia](Step-2-Distributions-ms)

# Trin 2: Fordelinger af variablerne

**Spørgsmål:** Hvordan fordeler priser, pendling, værelser og motorvejsadgang sig, og hvor mange huse ligger ved floden?

![Trin 2: fordelinger af pris, afstand, værelser og motorvejsadgang](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-2-distributions.png)

## Hvad forelæsningen siger

Før du modellerer noget, beder notebooken dig om at se på variablerne én ad gangen. Prisen, afstanden til de fem arbejdspladsområder og antallet af værelser får et histogram med en glat kurve oven på (et Kernel Density Estimate, KDE) fra Seaborn, og gennemsnittet står i titlen. Motorvejsadgang er et almindeligt Matplotlib-histogram, og flod-dummyen er et Plotly-søjlediagram med etiketterne No og Yes. Pointen er at se dataenes form: hvor de fleste huse ligger, hvor halerne er, og om noget ser mærkeligt ud.

## Hvad koden gør

- `price_distribution_figure` tegner prisen med en KDE, 50 intervaller og en bred form (`aspect=2`); `price_title` sætter gennemsnittet, 22,53 tusind dollar, i titlen.
- `distance_distribution_figure` og `rooms_distribution_figure` gør det samme for `DIS` (gennemsnit 3,80) og `RM` (gennemsnit 6,28); `average_distance` og `average_rooms` beregner gennemsnittene i domænelaget.
- `highway_access_figure` er et Matplotlib-histogram af `RAD` med 24 intervaller, sorte kanter og smalle søjler; `highway_access_counts` giver tallene bag.
- `river_bar_chart` returnerer en Plotly-figur med de to søjler No (471 huse) og Yes (35 huse); `river_counts_by_label` giver antallene med de etiketter.
- `distribution_panel_figure` samler pris, afstand, værelser og motorvejsadgang i billedet ovenfor.

## Det får du ud af det

- Prisen er skæv mod højre: de fleste huse koster omkring 21 tusind dollar (medianen er 21,2), nogle få koster langt mere, og 16 områder ligger præcis på loftet på 50.
- Afstanden til arbejdspladsområder er også skæv mod højre; værelserne ligner en klokkeform omkring 6,3.
- Motorvejsadgang er ikke en glat variabel: den antager værdierne 1 til 8 og springer derefter til 24, som rummer 132 af de 506 områder. Et histogram med brede intervaller ville skjule det hul.
- Kun 35 af 506 områder grænser op til floden, så et søjlediagram af en dummyvariabel fortæller hurtigt, hvor sjælden gruppen er.
- En KDE-kurve hjælper dig med at bedømme formen, men kun søjlerne viser de rigtige antal; brug begge.

Forrige: [Step-1-Goals-And-Data-da](Step-1-Goals-And-Data-da)
