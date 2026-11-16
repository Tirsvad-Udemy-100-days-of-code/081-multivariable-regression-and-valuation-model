[English](Step-6-Valuation) · **Dansk** · [Bahasa Malaysia](Step-6-Valuation-ms)

# Trin 6: Vurdering af en ejendom

**Spørgsmål:** Hvordan bruger du modellen til at vurdere et gennemsnitligt hus og et hus, du selv beskriver?

![Trin 6: den estimerede værdi af den gennemsnitlige ejendom og af den beskrevne ejendom](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-6-valuation.png)

## Hvad forelæsningen siger

Nu besvarer modellen det forretningsmæssige spørgsmål. Notebooken starter med den gennemsnitlige ejendom, en række med middelværdien af hver variabel, og beder log-modellen om et estimat: en logpris på 3,03. Eksponentialfunktionen omregner det til en pris i tusind dollar, og gange 1000 er det cirka 20.703 dollar. Derefter beskriver notebooken en ejendom: ved floden, 8 værelser, 20 elever pr. lærer, 5 enheder fra arbejdspladsområderne, høj forurening (75. percentil af `NOX`) og lav fattigdom (25. percentil af `LSTAT`). Alle andre variabler beholder deres gennemsnit. Logestimatet er 3,25, hvilket er cirka 25.792 dollar.

## Hvad koden gør

- `average_property` bygger tabellen med én række og middelværdien af de 13 variabler.
- `estimate_value` beder modellen om logestimatet og omregner det til dollar med `exp` og faktoren 1000; den returnerer begge tal i en `ValueEstimate`.
- `described_property` starter fra den gennemsnitlige ejendom og sætter de seks egenskaber: floden (`CHAS`), værelserne (`RM`), eleverne pr. lærer (`PTRATIO`), afstanden (`DIS`), forureningen (`NOX`) og fattigdommen (`LSTAT`).
- `value_property` er opgavens funktion: egenskaberne er parametre med forelæsningens værdier som standard, den tilpasser log-modellen, hvis du ikke giver en med, og returnerer estimatet. Den afviser værdier, der ikke kan være rigtige, som nul værelser.
- `property_characteristics` viser, hvad der ændres i forhold til gennemsnittet, og `valuation_figure` tegner billedet ovenfor.

## Det får du ud af det

- En model er først nyttig, når du kan stille den et spørgsmål: du beskriver en ejendom i variabelkolonnerne og får en pris tilbage. De variabler, du ikke kender, forbliver på gennemsnittet, hvilket er en rimelig standard.
- En log-model forudsiger en logpris. Vend transformationen om med `exp`, før du taler om dollar, og husk enheden: prisen er i tusinder.
- Den beskrevne ejendom er cirka 25 % mere værd end den gennemsnitlige (25.792 mod 20.703 dollar), fordi de ekstra værelser, floden og den lave fattigdom opvejer den højere forurening og de større klasser.
- Dollarbeløbene er dollar fra 1970'erne, og modellen er trænet på 506 områder; estimatet er et udgangspunkt for en samtale, ikke en prismærkat. Husk også, at kolonnen `B` koder en racemæssig andel, så denne model bør aldrig bruges i praksis.

Forrige: [Step-5-Log-Model-da](Step-5-Log-Model-da)
