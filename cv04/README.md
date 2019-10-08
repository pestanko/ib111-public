# Cvičenie 04 - Náhodné čísla

Na tomto cvičení sa budeme venovať témam:

- Debugger
- Náhodnosť
- Analýza

## Debuger

Je nástroj na ladenie programu, tzn. krokovanie, nahliadanie na aktuálny stav, hľadanie nejasností.

### Príklad
```python
#! /usr/bin/env python

def is_prime(num: int) -> bool:
    if num < 0:
        num *= -1

    if num == 0:
        return False

    for i in range(1, num, 2):
        if num % i == 0:
            return False
    return True

def computeGCD(num1: int, num2: int) -> int:
    smaller = num2

    if num1 < num2: 
        small = num1
    
    for i in range(1, smaller+1): 
        if (num1 % i == 0) and (num2 % i == 0): 
            return i
              
def print_is_prime(num: int):
    result = "is a prime!" if is_prime(num) else "is not a prime!"
    print(f"-> Number {num}", result)


def numbers_stats(num1: int, num2: int):
    print(f"Statistics for numbers {num1} and {num2}:")
    print_is_prime(num1)
    print_is_prime(num2)
    print(f"-> GCD({num1}, {num2}) =", computeGCD(num1, num2))
    print("->", num1, "is", "greater" if num1 > num2 else "smaller", "than", num2)

if __name__ == '__main__':
    numbers_stats(5, 4)
    print()
    numbers_stats(131, 111)


```

## Úlohy

Úlohy na samostatne vypracovanie

### [4.1.1. Šestiboká kostka](https://www.fi.muni.cz/IB111/sbirka/04-nahodna_cisla.html#sestiboka-kostka)
Napište funkci, která bude vracet nově vygenerované náhodné číslo simulující šestistěnnou kostku s čísly 1–6.

```python
from random import randint

def dice():
    pass

print(dice(), dice(), dice())
```

### [4.1.2. Dokud padá sudé číslo](https://www.fi.muni.cz/IB111/sbirka/04-nahodna_cisla.html#dokud-pada-sude-cislo)

Napište funkci, která bude provádět házení obyčejnou šestistěnnou kostkou tak dlouho dokud nepadne liché číslo. 
Poté funkce vrátí celkový součet všech hozených hodů.

```python
from random import randint

def turn():
    pass

print(turn(), turn(), turn())
```

_Tip: Nevieme koľko krát budeme opakovať. Existuje krasne kľúčové slovo `break`._

### [4.1.3. Statistiky](https://www.fi.muni.cz/IB111/sbirka/04-nahodna_cisla.html#statistiky)
Napište funkci, která vygeneruje a vypíše `count` náhodných čísel v intervalu `[lower, upper]` a následně vypíše nejmenší, největší číslo. Vypište také _aritmetický průměr_ ze všech vygenerovnaých čísel.

```python
from random import randint

def statistics(count, lower, upper):
    pass

statistics(10, 1, 100)
```


### [4.2.1. Opilec na cestě domů](https://www.fi.muni.cz/IB111/sbirka/04-nahodna_cisla.html#opilec-na-ceste-domu)

Opilec je na půli cesty mezi domovem a hospodou, každý krok udělá náhodně jedním směrem. Napište funkci, která bude simulovat opilcův pohyb. 
Jejími parametry budou vzdálenost mezi domovem a hospodou a počet kroků do opilcova usnutí (tj. maximální délka simulace). 
Simulace skončí buď tehdy, když opilec dojede domů nebo do hospody, případně po vyčerpání počtu kroků.

### Výstup:

```
>>> drunkman_simulator(10, 100)

home . . . . . * . . . . pub
home . . . . * . . . . . pub
home . . . * . . . . . . pub
home . . . . * . . . . . pub
home . . . * . . . . . . pub
home . . . . * . . . . . pub
home . . . * . . . . . . pub
home . . * . . . . . . . pub
home . * . . . . . . . . pub
home . . * . . . . . . . pub
home . . . * . . . . . . pub
home . . * . . . . . . . pub
home . . . * . . . . . . pub
home . . * . . . . . . . pub
home . . . * . . . . . . pub
home . . . . * . . . . . pub
home . . . . . * . . . . pub
home . . . . * . . . . . pub
home . . . . . * . . . . pub
home . . . . * . . . . . pub
home . . . . . * . . . . pub
home . . . . . . * . . . pub
home . . . . . * . . . . pub
home . . . . . . * . . . pub
home . . . . . . . * . . pub
home . . . . . . . . * . pub
home . . . . . . . . . * pub
home . . . . . . . . * . pub
home . . . . . . . . . * pub
home . . . . . . . . . . pub
Ended in the pub again!
```

#### Kostra:

```python
from random import randint

def drunkman_simulator(size, steps):
    pass

drunkman_simulator(10, 100)
```

_Tip: Optimálne by ste mali mať aspoň 3 a viac samostatných funkcii na riešenie tohoto problému_


### [4.2.2. Analýza opilce](https://www.fi.muni.cz/IB111/sbirka/04-nahodna_cisla.html#analyza-opilce)
Pokud jste se zabývali otázkami položenými v předchozím příkladu, zjistili jste, že to není až tak jednoduché zjistit. 
V tomto příkladu tedy použijeme předchozí program pro jednoduchou analýzu, jak to dopadne, když to zkusíme zopakovat vícekrát za sebou.

Nejprve upravte funkci z předchozí příkladu tak, aby nevypisovala stav opilce (například přidáním _volitelného parametru_ `output` a zapodmínkováním výpisu) 
a aby vracela `True` dojde-li opilec domů a `False` pokud ne.

Následně napište funkci, která provede simulaci opilce `count` krát a vypíše procentuální úspěšnost dojití domů.

```python
from random import randint, random

def drunkman_simulator(size, steps, output=False):
    pass

def drunkman_analysis(size, steps, count):
    pass

drunkman_analysis(10, 100, 100)
# Arriving home in 45.0 % of cases
```

