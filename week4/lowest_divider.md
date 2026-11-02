# Algoritmus pro hledani nejmensiho delitele

## Pametova slozitost:

Vzhledem k tomu, ze lookup dotazu musi byt v O(1), musim mit predem vytvoreny seznam s odpovedmi pro kazdy mozny dotaz, kde pomoci indexu ihned najdu odpoved. Tento seznam -> nejvetsi cast pametove slozitosti, ktera roste s input size.

Nez budu cokoli pocitat, zvazim, ze polovina vsech dotazu jsou suda cisla. Nejmensim delitelem vsech sudych cisel je 2.
Na kazdy dotaz muzu proto prvni odpovedet if x % 2 == 0, return 2.

Z tohoto duvodu nepotrebuji suda cisla mezi 2 a n vubec ukladat v pameti a potrebny **seznam se mi zkrati na polovinu.**

**Odtud plyne splneni podminky: "program během celého běhu (včetně předvýpočtu) použije nejvýše N/2+C paměťových buněk"**

- C bude konstanta, do ktere se vejdou pomocne promenne pro vypocet apod.

- Abych ukladala pouze licha cisla zacinajici od trojky, vyuziju posloupnosti na principu $a_{n} = (2n + 1) + 2$... inverzne z indexu dostanu hodnotu pomoci $(a - 3) / 2$.

## Casova slozitost:

Jelikoz ziskat delitele vypoctem primo z x je slozite, pomuzu si algoritmem Eratosthenova sita, ktery v sobe ma zabudouvanou iteraci po nasobcich. Ale namisto toho, abych si zapisovala hodnoty True/False pro prvocisla, budu chtit zapsat hodnotu p ke vsem jejim nasobkum, kterymi iteruje (vcetne aktualni iterace).

Jedine, na co si musime dat pozor, je, aby vyssi hodnoty neprepisovaly nejmensiho delitele. (Napr. 45: i kdyz zacnu od p \* p, se 3 prepise na 5). Zvolim proto pocatecni seznam, kde jsou vsechny hodnoty None. Aktualni hodnotu p zapisu do seznamu pouze tehdy, kdyz je ta predchozi None.

(Volnejsi) casovou slozitost sita jsme si ukazovali na cviceni u prvocisel -> Toto funguje v podstate stejne slozite, vnejsi cyklus n \* vnitrni cyklus n/1 + n/2 + n/3... co se zjednodusi/zvolni na (n/2 + n/2) + (n/4...) -> log n. Provadi stejny pocet vypoctu, jenom zapisuje misto True/False hodnoty p.

**Proto mohu odvodit, ze tento algoritmus pro pripravu lookup hodnot ma slozitost O(N log N).**

## Reseni / pseudokod:

```
# Helper functions pro seznam s lichymi cisly od 3

def to_index(c):
    return (c - 3) // 2

def from_index(i):
    return 2 * i + 3

n = int(input())

min_div = [None] * (to_index(n) + 1)
for p in range(3, n + 1, 2):
    if not min_div[to_index(p)]:
        min_div[to_index(p)] = p
        for k in range(p * p, n + 1, 2 * p):
            min_div[to_index(k)] = p

# While loop, kde uzivatel zadava dotazy + nejaka podminka, ze musi byt mezi 2 a n

# Pro kazdy zadany dotaz:
    # Pokud sude -> vratim 2
    # Pokud liche -> vratim hodnotu pod danym indexem: print(min_div[to_index(x)])
```
