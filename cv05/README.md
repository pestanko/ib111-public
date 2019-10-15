# [Cvičenie 05 - Řetězce a seznamy](https://www.fi.muni.cz/IB111/sbirka/05-retezce_a_seznamy.html)


Na tomto cvičení sa budeme venovať témam:

- Pass by reference
- Zoznamy
- Retazce

## Pass by reference


###  Opakovanie:

Operátor rovná sa `=` - ako funguje, preco funguje tak, ako funguje a co to ma spoločné s volaním funkcii.
[Python tutor odkaz](http://pythontutor.com/visualize.html#code=a%20%3D%2010%20%2B%201%0Ab%20%3D%2010%20%2B%201%0Ac%20%3D%20a%0Ad%20%3D%2010%20%2B%202%0A&cumulative=false&curInstr=4&heapPrimitives=true&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).

```python

a = 10 + 1
b = 10 + 1
c = a
d = 10 + 2

print(f"id(a) == id(b) ~> {id(a)} == {id(b)} ~> {id(a) == id(b)}")

```

### Predavanie zoznamov:


```python

def simple_add(a, b):
  a += b
  return a


def print_simple_add(a, b):
  print(f"BEFORE: a={a}; b={b}")
  print(f"simple_add({a}, {b}) = {simple_add(a, b)}")
  print(f"AFTER: a={a}; b={b}")


# EXECUTE:

print_simple_add(1, 2)
print()
print_simple_add([1], [2])

```

### Kopírovanie zoznamov:

```python
def inc_list_same(input: list) -> list:
    for i in range(len(list)):
        input[i] += 1

    return input


def inc_list_new(input: list) > list:
    new_list = []
    for i in input:
        new_list.append(i + 1)
    return new_list

def inc_list_new2(input: list) -> list:
    return [i + 1 for i in input]
```

Tretia varianta je zápis pomocou tzv. [List Comprehensions in Python](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python).

### List Comprehensions _(Advanced)_

Veľmi užitočný zápis, ktorý budete používať aj na Haskell-y.

```python
# Standard Way:
new_list = []
for i in old_list:
    if filter(i):
        new_list.append(expressions(i))

# Comprehension Way:
new_list = [expression(i) for i in old_list if filter(i)]

```

#### Syntax:

```python
[ expression for item in list if conditional ]
```

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


## Odkazy
- [How do I pass a variable by reference?](https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference)
- [How do I write a function with output parameters](https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference)
- [Python Tutor](http://pythontutor.com/visualize.html#mode=edit)