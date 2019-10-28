# [Cvičenie 06 Binární vyhledávání, testování, typy](https://www.fi.muni.cz/IB111/sbirka/06-binarni_vyhledavani.html)


Na tomto cvičení sa budeme venovať témam:

- Typovanie (opakovanie)
- Testovanie
- Binárne vyhľadávanie


## Typovanie 

S typovaním sme sa už stretli. 

```python
from random import randint
from typing import List

def dice() -> int:
    return randint(1, 6)

def dice_stats(count: int) -> List[int]:
    # 7 numbers, only 6 possible, 
    # index 0 will not be used
    numbers = [0,0,0,0,0,0,0] 

    for _ in range(count):
        roll = dice()
        numbers[roll] += 1

    return numbers
```

Na otestovanie správneho otypovania, pouzijeme nástroj [`mypy`](http://mypy-lang.org/) alebo [online](https://mypy-play.net/?mypy=latest&python=3.7).

Inštalácia _(na školských PC je už `mypy` nainštalované)_ je popísaná v sekcii [návody](https://www.fi.muni.cz/IB111/navody):

Použitie:

```bash
mypy --strict program.py
```

## Testovanie

Jednoduché otestovanie funkcie `factorial`

```python

def factorial(number: int) -> int:
    """Function computes factorial
    Takes an integer number and returns an integer.
    If an input argument is negative or zero, function will return 1
    """
    return 1 if number <= 0 else number * factorial(number - 1)

def test_factorial_zero():
    assert factorial(0) == 1, "Factorial should return 1 for zero"

def test_factorial_negative():
    for i in range(-1, -1000, -1):
        assert factorial(i) == 1, f"Factorial should return 1 for negative number ({i})"

def test_factorial_possitive():
    assert factorial(1) == 1,   "Factorial for 1 should return 1"
    assert factorial(2) == 2,   "Factorial for 2 should return 2"
    assert factorial(3) == 6,   "Factorial for 3 should return 6"
    assert factorial(4) == 24,  "Factorial for 4 should return 24"
    assert factorial(5) == 120, "Factorial for 4 should return 120"


if __name__ == '__main__':
    test_factorial_zero()
    test_factorial_negative()
    test_factorial_possitive()

```

`Assert` je možné používať nielen na testovanie, ale aj na kontrolu vstupných podmienok.
_Pozor: Existujú lepšie riešenia ako na to, avšak pre jednoduchosť si vieme vystačiť s `assert`._

```python
def factorial(number: int) -> int:
    assert isinstance(number, int), "Input parameter should be instance of the integer"
    assert number >= 0, "Input parameter should be possitive"
    
    result = 1
    for i in range(1, number + 1):
        result *= i

    assert result > 0, "Result should never be negative or zero"
    return result
```

## Úlohy


### [6.1.1. Doplnění typů](https://www.fi.muni.cz/IB111/sbirka/06-binarni_vyhledavani.html#doplneni-typu)
Otypujte následující funkce. Funkce `dice_max(count)` vrací _nejvyšší číslo_, které padlo na kostce.

```python
from random import randint

def dice():
    return randint(1, 6)

def dice_max(count):
    maximum = dice()
    for _ in range(count-1):
        roll = dice()
        if roll > maximum:
            maximum = roll
    return maximum
```


### [6.1.2. Doplnění assertu](https://www.fi.muni.cz/IB111/sbirka/06-binarni_vyhledavani.html#doplneni-assertu)

Doplňte do předchozího kódu `assert` tak, aby funkce `dice_max` přijímala pouze `count >= 1`.

Upravte funkci `dice_max` z předchozího příkladu tak, aby umožňovala `count == 0` a v takovém případě vrátila `None`. 
Upravte typy tak, aby `mypy` prošlo!



### [6.1.4. Testování](https://www.fi.muni.cz/IB111/sbirka/06-binarni_vyhledavani.html#testovani)

Napište smysluplné testy (`assert`-y) na funkci `palindrom` a opravte na základě testů její chyby.

```python
def palindrom(text):
    length = len(text)
    for i in range((length-1)//2):
        if text[i] != text[length - 1 - i]:
            return False
    return True
```


### [6.2.4. Binární vyhledávání](https://www.fi.muni.cz/IB111/sbirka/06-binarni_vyhledavani.html#id2)


Napište funkci `binary_search(needle, haystack)`, která zjistí, zda se hodnota `needle` nachází ve _vzestupně uspořádaném_ seznamu `haystack`. 

_Funkce musí mít logaritmickou časovou složitost._

```python
def binary_search(needle, haystack):
    pass

print(binary_search(5, [1, 2, 5, 8])) # True
print(binary_search(4, [1, 2, 5, 8])) # False
```

### [6.2.5. Binární vyhledávání](https://www.fi.muni.cz/IB111/sbirka/06-binarni_vyhledavani.html#binarni-vyhledavani-pozice)


Vylepšete předchozí funkci tak, aby vracela index pozice, kde se hledaný prvek nachází. Pokud prvek v seznamu není, vraťte -1.

```python

def binary_search_position(needle, haystack):
    pass

print(binary_search_position(5, [1, 2, 5, 8])) # 2
print(binary_search_position(4, [1, 2, 5, 8])) # -1
```

### [6.2.7. Umocňování](https://www.fi.muni.cz/IB111/sbirka/06-binarni_vyhledavani.html#umocnovani)

Napište funkci `super_power(base, exp)`, která umocní dané číslo `base` na daný exponent `exp`. 

_Funkce musí mít logaritmickou časovou složitost vzhledem k hodnotě exponentu._

```python
def super_power(base, exp):
    pass

print(super_power(2, 7))  # 128
print(super_power(5, 15)) # 30517578125
```


