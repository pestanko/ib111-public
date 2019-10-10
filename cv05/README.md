# [Cvičenie 04 - Řetězce a seznamy](https://www.fi.muni.cz/IB111/sbirka/05-retezce_a_seznamy.html)


Na tomto cvičení sa budeme venovať témam:

- Debugger
- Náhodnosť
- Analýza

## Úlohy na Zoznamy

Úlohy na samostatne vypracovanie.

### [5.1.1. Součet, maximum a hledání](https://www.fi.muni.cz/IB111/sbirka/05-retezce_a_seznamy.html#soucet-maximum-a-hledani)

Napište funkce nad seznamem čísel, které zjistí:

- součet všech čísel v seznamu,
- nejvyšší číslo v seznamu,
- zda se určitá hodnota vyskytuje v seznamu,

tedy ekvivalenty operací `max`, `sum` a `in` (ale s použitím pouze základních operací nad seznamy).


```python
def my_sum(numbers: list) -> int:
    pass

def my_max(numbers: list) -> int:
    pass

def my_in(x: int, array: list) -> bool:
    pass

print(my_sum([6, 5, 11, 8]))    # 30
print(my_max([6, 5, 11, 8]))    # 11
print(my_max([-10, -3, -5]))    # -3
print(my_in(5, [6, 5, 11, 8]))  # True
print(my_in(4, [6, 5, 11, 8]))  # False
```


### [5.1.3. Modifikace vs. vytváření nového seznamu](https://www.fi.muni.cz/IB111/sbirka/05-retezce_a_seznamy.html#modifikace-vs-vytvareni-noveho-seznamu)

Napište funkci `double_all`, která dostane na vstupu seznam čísel a každý jeho prvek vynásobí dvěma. 

Dále napište funkci `create_doubled`, která dostane na vstupu seznam čísel a vrátí nový seznam získaný ze vstupního tak, že každý prvek vynásobí dvěma. Na rozdíl od předchozí funkce však **nemění předaný seznam**.

```python
def double_all(numbers: list) -> list:
    pass

def create_doubled(numbers: list) -> list:
    pass

a = [1, 4, 2, 5]
double_all(a)
print(a)  # [2, 8, 4, 10]

a = [1, 4, 2, 5]
b = create_doubled(a)
print(a)  # [1, 4, 2, 5]
print(b)  # [2, 8, 4, 10]
```


### [5.1.4. Zploštění](https://www.fi.muni.cz/IB111/sbirka/05-retezce_a_seznamy.html#zplosteni) (Bonus)

Napište funkci, jejímž vstupem je seznam seznamů a výstupem je seznam, který obsahuje prvky všech jednotlivých seznamů.

```python
def flatten(lists: list) -> list:
    pass

print(flatten([[0, 2, 3], [1, 2, 3], [9, 10]]))
# [0, 2, 3, 1, 2, 3, 9, 10]
```


## Úlohy na Reťazce

### [5.2.1. Prokládání textu textem](https://www.fi.muni.cz/IB111/sbirka/05-retezce_a_seznamy.html#prokladani-textu-textem)

Napište funkci, která mezi každá dvě písmena daného textu vloží dodaný text.

```python
def dummy(text: str, rubbish: str) -> str:
    pass

print(dummy('pampeliska', 'XX'))
# 'pXXaXXmXXpXXeXXlXXiXXsXXkXXa'
```

### [5.2.3. Pozpátku](https://www.fi.muni.cz/IB111/sbirka/05-retezce_a_seznamy.html#pozpatku)

Napište funkci, která vám vrátí řetězec s písmeny uspořádanými pozpátku.

```python
def reverse(text: str) -> str:
    pass

print(reverse('ONMEJATEJOLSEH'))
# H E S L O J E T A J E M N O
```

### [5.2.5-1. Počet zadaného písmena](https://www.fi.muni.cz/IB111/sbirka/05-retezce_a_seznamy.html#pocet-a)

_Varianta na zadanie co je v zbierke, my sa však neobmedzíme len na `A`, ale na ľubovolné písmeno_

Napíšte funkciu, která spočíta počet výskytov písmena (znaku), pozor na veľkosti písmena nezáleží.
V prípade, že je vstupom znak `a` tak funkcia počíta aj veľké `A` a naopak.

```python
def count_char(text: str, character: str) -> int:
    pass

print(count_char('Liska Adelka', 'a'))
# 3
```

### [5.2.6. Znaky na stejných pozicích](https://www.fi.muni.cz/IB111/sbirka/05-retezce_a_seznamy.html#znaky-na-stejnych-pozicich)

Napište funkci, která dostane dva řetězce a vypíše ty znaky, které jsou na shodných pozicích stejné.


```python
def string_intersection(left, right):
    pass

string_intersection('ZIRAFA', 'KARAFA')
# R A F A
string_intersection('PES', 'KOCKA')
# (prazdny retezec)
```

### [5.2.9. Hodnota slova](https://www.fi.muni.cz/IB111/sbirka/05-retezce_a_seznamy.html#hodnota-slova)

Každý znak A-Z má hodnotu 1-26 (diakritiku a velikost písmen pro tento příklad ignorujte). Napište funkci, která spočítá a vrátí hodnotu vloženého řetězce (slova).


```python
def word_value(text):
    pass

print(word_value("AHOJ"))
# 34
```

### [5.2.12. Náhodný řetězec](https://www.fi.muni.cz/IB111/sbirka/05-retezce_a_seznamy.html#nahodny-retezec)

```python
from random import randint

def random_string(length, chars):
    pass

print(random_string(10, "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"))
```

### [5.2.8. Palindrom](https://www.fi.muni.cz/IB111/sbirka/05-retezce_a_seznamy.html#palindrom)

Napište funkci, která vrátí, zda je řetězec palindromem. Palindromem je takové slovo či věta, která má při čtení v libovolném směru stejný význam, například `nepotopen` či jelenovi pivo nelej (mezery můžete ignorovat).


```python
def palindrom(text):
    pass

print(palindrom("JELENOVIPIVONELEJ"))
# True
```

### [5.3.1. Caesarova šifra](https://www.fi.muni.cz/IB111/sbirka/05-retezce_a_seznamy.html#caesarova-sifra)
Napište funkci, která zašifruje text tak, že posune všechna jeho písmena v abecedě o n dopředu (cyklicky), můžete se inspirovat popisem Caesarovy šifry.

```python
def caesar(text, klic):
    pass

print(caesar('zirafa', 3))
# CLUDID
```

