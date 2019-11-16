# [Cvičenie 10 Objekty a Triedy](https://www.fi.muni.cz/IB111/sbirka/09-objekty_a_tridy.html)

Na tomto cvičení sa budeme venovať témam:
- Triedy
- Objekty
- Konstruktor
- Metody


## Teoria

Trieda (`class`) - předpis (šablona) pro vytváření nových objektů nějakého typu.

Triedy iba s atribútami sa nazývajú štruktúry (záznamy) - v jazyku C (`struct`)



```python
class Student:
    def __init__(self, name, points):
        self.name = name
        self.points = points

john = Student('John', 10)
print(john.name)    # John
john.points += 20
print(john.points)  # 30
```

triedy môžu obshovať aj tzv. metódy - funkcie asociované k danému objektu.

_Objekt jde definovaný svojím stavom (atribútmi) a chovaním (metódami/akciami).


```python
class Student:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_points(self, new_points):
        """Pridani bodu studentovi.
        """
        self.points += new_points

    def __str__(self):
        """Vraci informacni retezec. (Viz 'print(student'.))
        """
        return f'<Student {self.name}, points: {self.points}>'

john = Student('John')
print(john)
john.add_points(20)
print(john)
```


## Úlohy

### [9.1.2. Obdélník](https://www.fi.muni.cz/IB111/sbirka/09-objekty_a_tridy.html#obdelnik)

Napište třídu `Rectangle` pro reprezentaci obdélníku o dané _šířce_ a _výšce_ a funkci pro výpočet obsahu předaného obdélníku.

```python
class Rectangle:
    pass

def area(rectangle):
    pass

rectangle = Rectangle(4, 3)
print(rectangle.width)   # 4
print(rectangle.height)  # 3
print(area(rectangle))   # 12
```


### Obĺžnik ako objekt s metódami

Vezmite triedu `Rectangle` z predchádzajúcej úlohy a z funkcie `area` spravte metódu, 
objekt rovnako rozšírte o metódu `perimeter` (obvod).

```python
class Rectangle:
    pass

    def area(self) -> int:
        pass

    def perimeter(self) -> int:
        pass

```


### [9.2.1. Kruh](https://www.fi.muni.cz/IB111/sbirka/09-objekty_a_tridy.html)

Napište třídu pro reprezentaci kruhu s daným středem a poloměrem. 
Implementujte metody pro výpočet obvodu, obsahu a vrácení informačního řetězce (`__str__`).

```python
class Circle:
    def __init__(self, center: float, radius: float):
        """Inicializace objektu
        """
        pass

    def perimeter(self) -> float:
        """Vraci obvod kruhu
        """
        pass

    def area(self) -> float:
        """Vraci obsah kruhu
        """
        pass

    def __str__(self) -> str:
        """Vraci informacni retezec
        """
        pass

circle = Circle((-130, -130), 100)
print(circle)  # Circle at (-130, -130) with radius 100
print(circle.area())  # 31415.926535897932
```

### [9.2.6. Knihovna](https://www.fi.muni.cz/IB111/sbirka/09-objekty_a_tridy.html#knihovna)

Vytvořte třídu `Library` pro reprezentaci kolekce knih s metodami pro přidání knihy, odebrání knihy, 
nalezení knihy podle názvu nebo `ISBN`, nalezení všech knih daného autora, nalezení všech knih s cenu pod zadanou mez.

```python

class Library:
    def __init__(self):
        pass

    def add_book(self, book: 'Book') -> None:
        pass

    def rm_book(self, book: 'Book') -> None:
        pass

    def all_books(self) -> List['Book']:
        pass

    def find_by_name(self, name: str) -> List['Book']:
        pass

    def find_by_author(self, author: str) -> List['Book']:
        pass

    def find_by_isbn(self, isbn: str) -> 'Book':
        pass

    def find_by_price(self, price: int) -> List['Book']:
        pass


class Book:
    def __init__(self, name: str, author: str, isbn: str, price: int):
        pass

library = Library()

library.add_book(Book('Cooking for Geeks', 'Jeff Potter', '0596805888', 22))
library.add_book(Book('Testing book', 'Testing Author', 'TEST-ISO-0001', 1000))
library.add_book(Book('Testing book 2', 'Testing Author', 'TEST-ISO-0002', 2000))
library.add_book(Book('Testing book 3', 'Testing Author', 'TEST-ISO-0003', 200))

print(library.all_books())
print(library.find_by_isbn('TEST-ISO-0003'))

```


### [9.2.4. Zásobník](https://www.fi.muni.cz/IB111/sbirka/09-objekty_a_tridy.html#zasobnik)

Vytvořte třídu pro reprezentaci zásobníku podporující operace přidání prvku, odebrání prvku a test na prázdnost.

```python
class Stack:
    pass

# ukazka fungovani
stack = Stack()
stack.push(5)
stack.push(10)
print(stack.pop())       # 10
print(stack.is_empty())  # False
```

### [9.2.3. Příšera](https://www.fi.muni.cz/IB111/sbirka/09-objekty_a_tridy.html#prisera)

Doplňte následující kostru třídy a vyzkoušejte její funkčnost. 
Poté přidejte příšeře další metody, např. `is_defeated`, která vrací `True`, pokud už příšera nemá žádné životy.

```python
class Creature:

    def __init__(self, name: str, level: int, health_max: int, power: int):
        """Inicialize atributu objektu
        """
        pass

    def __str__(self) -> str:
        """Vraci textovou reprezentaci prisery.
        """
        pass

    def get_level(self) -> int:
        """Vraci level prisery
        """
        pass

    def new_level(self) -> None:
        """Zvysi level o 1
        """
        pass

    def attack(self, enemy: 'Creature'):
        """Provede utok na protivnika.

        Vysledek zavisi na rozdilu meho a protivnikova levelu.
        """
        pass

    def undertake_attack(self, damage: int):
        """Podstoupi utok o dane sile.

        Ubere si prislusny pocet zivotnich bodu.
        """
        pass
```




