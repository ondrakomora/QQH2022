Vítej na Qminers Quant Hackathonu!

Tvým úkolem bude naprogramovat model, který dokáže vydělávat na sázkařském trhu. Co přesně to obnáší, najdeš v zadání.

Aktuálně běží kvalifikační fáze, ze které postoupí prvních 20 týmů do finále. Kvalifikace končí 24.11.2022 v 23:59:59.

Vše potřebné pro úspěšný start najdeš na: https://github.com/IDA-CTU/QQH2022/

V systému pak najdeš dva problémy. "Beat the Bookie Qualification" je soutěžní úloha, kde se tvůj model vyhodnotí na skrytých validačních datech. "Beat the Bookie Debug" vyhodnotí tvůj model na zápasech mezi daty 2005-08-01 a 2006-08-01. Tato úloha slouží pro ověření, že se tvůj kód chová stejně zde jako na tvém stroji. Debug úloha nemá žádný vliv na celkové pořadí.

Ve finále Tě pak budou čekat nová, testovací data. Počítej s tím, že nemusí být úplně přesně stejná jako ta validační, a snaž se úlohu řešit dostatečně obecně.

Pár technických informací a pravidel, než začneš:

K dispozici budeš mít 1 cpu (1 vlákno) a 5 GB RAM. V jednom čase může běžet pouze jedna evaluce tvého řešení.

Počet odevzdání je omezen, doporučujeme tedy kód pečlivě odladit na lokálním stroji.

V případě neúspěšného doběhnutí tvého programu se odevzdávací sytém pokouší napovědět příčinu pádu.

1. RTE = Runtime Error. Nejčastěji kód spadnul na vyjímku, jejíž jméno ti odevzdávací systém (po rozkliknutí testcasu) ukáže. 
2. MLE = Memory Limit Exceeded. Překročil jsi  pamětový limit. (Může být rozpoznáno jako RTE)
3. TLE = Time Limit Exceeded. Překročil jsi časový limit.

**Je zákázáno:**

1. Používat k ladění modelů jakákoliv jiná než námi dodaná data.
2. Spolupracovat s jinými týmy.
3. Manipulovat s odevzdávacím systémem.
4. Jakkoliv dolovat data z odevzdávacího systému.
5. Spouštět procesy, komunikovat přes síť a vytvářet soubory v odevzdávacím systému.


Porušení pravidel bude vést k vyloučení ze soutěže. Všechna odeslaná řešení se ukládají a mohou být podrobena kontrole.

**Vyhrazujeme si právo tato pravidla měnit. Naším cílem je férová challenge.**
