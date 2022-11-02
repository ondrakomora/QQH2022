## Úvod do sportovního sázení

Sportovní sázení je hra dvou hráčů: bookmakera a sázkaře.
Úlohou bookmakera je nabízet sázkařům příležitosti k sázkám s cílem maximalizovat svůj vlastní získ.
Blíží-li se tedy například nějaké hokejové utkání dvou týmů, bookmaker vypíše tzv. kurzy na možné výsledky.
Sázkař si může zvolit, na které zápasy a výsledky by si chtěl vsadit.
V případě, že si sázkař vsadí na výsledek, který nastane, vyhrává sázkař vloženou sázku vynásobenou kurzem bookmakera.
Pokud daný výsledek nenastane, sázkař svou sázku prohrál.
Příklad: pro zápas Slavia - Sparta vypíše bookmaker kurzy 1.6 na výhru domácích (Slavia), 3.75 na remízu a 6.6 na vítězství Sparty.
Sázkař, který má k dispozici 1000 Kč, se rozhodne vsadit 100 Kč na vítězství Slavie a 40 Kč na remízu.
Po vsazení vkladů má na svém kontě 860 Kč.
Předpokládejmě, že utkání skončí remízou.
Sázkař vyhrává 3.75 x 40 = 150 Kč.
Jeho sázka na výhru domácích propadá bookmakerovi.
Ve finále má sázkař na kontě 1010 Kč. 

## Zadání

Vaším úkolem bude naprogramovat co nejúspešnějšího sázkaře.
V naší soutěži však nebude rozhodovat počet shédnutých zápasů, nýbrž vaše schopnost navrhnout, implementovat a otestovat model, který se naučí predikovat výsledky nadcházejících zápasů z historických dat. 

Jelikož jednotlivé ročníky soutěží (sezóny) trvají několik měsíců, bude se váš model v průběhu sezóny adaptovat na nová data. 

Každý den, kdy jsou na trhu nějaké sázkařské příležitosti, obdržíte inkrement dat, sázkařské příležitosti a shrnutí.
Od vás budeme očekávat sázky, které si přejete uskutečnit.

### DataFrame se shrnutím

Ve shrnutí se dozvíte aktuální datum a jaké prostředky máte k dispozici.

|    |   Bankroll | Date                |   min_bet |   max_bet |
|---:|-----------:|:--------------------|----------:|----------:|
|  0 |    1000    | 2003-09-14 00:00:00 |         5 |       100 |

- bankroll - Aktuální stav vašeho konta
- date - Aktuální datum 
- min_bet - Minimální možná nenulová sázka
- max_bet - Maximální možná sázka

### DataFrame inkrementálních dat

Inkrementální data obsahují výsledky a statistiky, které jste doposud neviděli (jedná se o nově odehrané zápasy).
Počítejte s tím, že první inkrement který uvidíte, bude obsahovat i zápasy staršího data (z předcházejících sezón). 

|    |   Sea | Date                |   HID |   AID | Open                |   OddsH |   OddsA |   HSC |   ASC | H     | A     |   S_H |   PPG_H |   PIM_H |   FOW_H |   S_A |   PPG_A |   PIM_A |   FOW_A |   BetH |   BetA |
|---:|------:|:--------------------|------:|------:|:--------------------|--------:|--------:|------:|------:|:------|:------|------:|--------:|--------:|--------:|------:|--------:|--------:|--------:|-------:|-------:|
|  0 |  2000 | 2000-10-04 00:00:00 |     9 |     7 | 2000-10-03 00:00:00 |       0 |       0 |     2 |     2 | False | False |    21 |       1 |      20 |      41 |    28 |       1 |      18 |      38 |      0 |      0 |
|  1 |  2000 | 2000-10-05 00:00:00 |     4 |    10 | 2000-10-04 00:00:00 |       0 |       0 |     3 |     4 | False | True  |    21 |       0 |      20 |      39 |    28 |       1 |      32 |      35 |      0 |      0 |
|  2 |  2000 | 2000-10-05 00:00:00 |    21 |    27 | 2000-10-04 00:00:00 |       0 |       0 |     6 |     3 | True  | False |    33 |       3 |       8 |      34 |    29 |       0 |      16 |      27 |      0 |      0 |
|  3 |  2000 | 2000-10-05 00:00:00 |     3 |     6 | 2000-10-04 00:00:00 |       0 |       0 |     4 |     2 | True  | False |    30 |       0 |      21 |      35 |    21 |       1 |      24 |      36 |      0 |      0 |
|  4 |  2000 | 2000-10-05 00:00:00 |     2 |    20 | 2000-10-04 00:00:00 |       0 |       0 |     4 |     4 | False | False |    38 |       2 |      10 |      30 |    33 |       2 |      20 |      45 |      0 |      0 |

- MatchID - Unikátní identifikátor zápasu (MatchID je index DataFramu)
- Date - Den kdy bude zápas odehrán 
- HID - Unikátní identifikátor domácího týmu
- AID - Unikátní identifikátor týmu hostí
- OddsH/A - Bookmakerovy kurzy pro daný výsledek
- HSC - Výsledné skóre domácích
- ASC - Výsledné skóre hostí
- H/A - Binární indikátor výhry domácích/hostí
- S_H/A - Střely na bránu daného týmu
- PIM_H/A - Trestné minuty daného týmu
- PPG_H/A - Góly v přesilovkách daného týmu
- FOW_H/A - Vyhraná vhazování daného týmu
- BetH/A - Celkový objem Tvých sázek na daný výsledek

### DataFrame sázkařských příležitostí

Sázkařské příležitosti obsahují zápasy hrané v nadcházejících dnech.
Příležitosti jsou platné do data konání zápasu (včetně).
Je tedy možné vsadit na danou příležitost vícekrát.

|   MatchID |   Sea | Date       |   HID |   AID |   OddsH |   OddsA |     BetH |     BetA |
|----------:|------:|:-----------|------:|------:|--------:|--------:|---------:|---------:|
|     27435 |  2003 | 2003-09-16 |     8 |    31 |    3.56 |    2.17 | 0 | 0 |
|     27444 |  2003 | 2003-09-16 |    41 |    42 |    6.5  |    1.57 | 0 | 0 |
|     27437 |  2003 | 2003-09-16 |    14 |     6 |    1.77 |    4.96 | 0 | 0 |
|     27438 |  2003 | 2003-09-16 |    18 |    30 |    2.8  |    2.65 | 0 | 0 |
|     27439 |  2003 | 2003-09-16 |    21 |    45 |    1.8  |    4.83 | 0 | 0 |

### DataFrame sázek

Tento DataFrame očekáváme jako vaší odpověď.
I pokud nechcete pokládat žádné sázky, musíte poslat (alespoň prázdný) DataFrame.

|   MatchID |     BetH |     BetA |
|----------:|---------:|---------:|
|     27435 | 5.5 | 0 |
|     27444 | 0 | 21.7 |
|     27437 | 23.7 | 0 |
|     27438 | 0 | 0 |
|     27439 | 0 | 7.91 |

### Technické náležitosti

- Veškerá data kolující mezi vaším modelem a bookmakerem jsou uložená v pandas.DataFrame.
- Komunikace mezi vámi a bookmakerem probíhá přes std in/out, avšak nemusíte se ničeho obávat, serializaci jsme vyřešili za vás.
- Pokud bookmakerovi pošlete sázky na jiné příležitosti, než které vám přisly, budou ignorovány.
- Pokud nebudete mít dostatek prostředků pro vaše sázky, budou ignorovány.
- Sázky > max_bet a sázky < min_bet budou ignorovány.

### Časté problémy

- Nejčastější chyba v upload systému je spojena s tím, že se váš kód v evaluační smyčce na hyperionu dostane do stavu, na který není připraven.
  - Například "RTE: KeyError" - zkontrolujte si zda je váš kód připravený na prázdný Dataframe příležitostí, nově se vyskytující ID týmu, apod.

Veškeré dotazy, problémy a náměty směřujte na qminers.quant.hackathon@gmail.com
