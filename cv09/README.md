# [Cvičenie 09 Datové struktury](https://www.fi.muni.cz/IB111/sbirka/08-datove_struktury.html)

Na tomto cvičení sa budeme venovať témam:
- Dátové štruktúry
- Zásobník  `list`  _(LIFO)_ 
- Fronta `deque` _(FIFO)_
- Množina `set`
- Asociatívne pole `dict` _(Dictionary, map)_


## Zhrnutie a príklady


### [Zásobník](https://www.fi.muni.cz/IB111/sbirka/08-datove_struktury.html#zasobniky)

```python
stack = [1, 2, 3] # vytvoreni zasobniku

stack.append(4) # pridani do zasobniku
print(stack) # [1, 2, 3, 4]

top = stack.pop() # odebrani ze zasobniku
print(stack, top) # [1, 2, 3], top: 4

top = stack.pop() # dalsi odebrani ze zasobniku
print(stack, top) # [1, 2], top: 3
```


### [Fronta](https://www.fi.muni.cz/IB111/sbirka/08-datove_struktury.html#fronty)

```python
from collections import deque

queue = deque(["Petr", "Zdenek", "Filip"]) # 3 studenti cekaji ve fronte na obed


queue.append("Kuba") # Kuba prisel na konec fronty
print(queue) 
# deque(["Petr", "Zdenek", "Filip", "Kuba"])

queue.append("Roman") # Roman prisel na konec fronty
print(queue) 
# deque(["Petr", "Zdenek", "Filip", "Kuba", "Roman"])

student = queue.popleft() # prvni ve fronte (Petr) dostal obed
print(queue, student) 
# deque(["Zdenek", "Filip", "Kuba", "Roman"]), student: "Petr"

student = queue.popleft() # dalsi ve fronte (Zdenek) dostal obed
print(queue, student) 
# deque(["Filip", "Kuba", "Roman"]), student: "Zdenek"
```

### [Množina](https://www.fi.muni.cz/IB111/sbirka/08-datove_struktury.html#mnoziny)

```python
# vytvoreni prazdne mnoziny
my_set = set()

my_set.add(5) # pridani prvku do mnoziny
print(my_set) # set([5])

# pridani stejneho prvku do mnoziny vickrat
my_set.add(6)
my_set.add(6)
print(my_set) # set([5, 6])

# pridani kolekce prvku do mnoziny
my_set.update([1, 3, 10, 15])
print(my_set) # set([1, 3, 5, 6, 10, 15])

my_set.remove(5) # odebrani prvku z mnoziny
print(my_set) # set([1, 3, 6, 10, 15])

cardinality = len(mnozina) # zjisteni velikosti mnoziny
print(cardinality) # 5

# test vyskytu
if 10 in my_set:
    print('10 is member of my_set')

# iterovani pres prvky mnoziny
for x in my_set:
    print(x, x * x)

# Operace:

# vytvoreni 2 mnozin
a = set([1, 3, 5, 7])
b = set([2, 3, 4, 5])

# sjednoceni mnozin
print(a | b) # set([1, 2, 3, 4, 5, 7])

# prunik mnozin
print(a & b) # set([3, 5])

# mnozinovy rozdil
print(a - b) # set([1, 7])
```

### [Asociatívne pole](https://www.fi.muni.cz/IB111/sbirka/08-datove_struktury.html#slovniky)

```python
points = {"Jack":66, "Peter":0, "Denis":0} # vytvoreni slovniku

# Alternativny zapis:
points_alt = dict(Jack=66, Peter=0, Denis=0)
	
# pristup k hodnote pod klicem "Jack"
print(points["Jack"]) # 66

points["Tom"] = 60 # pridani nove hodnoty do slovniku
print(points) 
# {"Jack":66, "Peter":0, "Denis":0, "Tom":60}

points["Peter"] += 60 # zmena hodnoty pod nejakym klicem
print(points) 
# {"Jack":66, "Peter":60, "Denis":0, "Tom":60}

del points["Denis"] # smazani zaznamu s klicem "Denis"
# body: {"Jack":66, "Peter":60, "Tom":60}

# iterace pres klice slovniku
for name in points:
    print(name)

# iterace pres hodnoty ve slovniku:
for value in points.values():
    print(value)

# iterace pres klice a hodnoty soucasne
for key, value in points.items():
    print(name, ':', value)

# zjisteni, zda uz je nejaky klic ve slovniku
if "Sam" in points:
    print("Sam's record present.")
else:
    print("No record for Sam")
```

## Úlohy

### Úlohy na zásobníky

#### [8.1.1. Interpretace výrazu v postfixu](https://www.fi.muni.cz/IB111/sbirka/08-datove_struktury.html#interpretace-vyrazu-v-postfixu)


Při běžném počítání s aritmetickými výrazy `6 + 5` používáme takzvanou infixovou notaci s operátorem mezi operandy. 
V tomto příkladě budeme pracovat s takzvaně reverzní polskou notací, 
kdy operátor následuje po operandech, například `6 5 *`.

Vyzkoušejte si převést `7 * 8 + 2 * 6 + 5` do _postfixu_ a následně si ho zkuste spolu s `5 7 * 3 - 4 +` vyhodnotit.

Napište funkci, která obdrží řetězec v _postfixové notaci_ a ta výraz za pomocí **zásobníku** vyhodnotí. Implementuje operace `+, -, / a *` v plovoucí čárce.

Tip: může se vám hodit metoda `split`, která je použitelná na řetězcích: `"a b c".split()`


```python
def evaluate_postfix(expr):
    pass

print(evaluate_postfix("8 7 * 6 5 + 2 * +")) # 78
print(evaluate_postfix("6 5 -")) # 1
print(evaluate_postfix("15 7 1 1 + - / 3 * 2 1 1 + + -")) # 5
```

---

### Úlohy na fronty

#### [8.2.1. Má mě rád, nemá mě rád](https://www.fi.muni.cz/IB111/sbirka/08-datove_struktury.html#ma-me-rad-nema-me-rad)

Nejprve si vygenerujeme _(náhodne)_ kytici lineárně uspořádaných `n` květin, každou o 1 až 4 okvětních lístcích. 
Poté vezmeme první květinu a utrhneme z ní právě jeden lístek a _zařadíme ji nakonec_. 
Postup opakujeme dokud nejsou všechny květiny otrhané. Má vás rád?

```python
from random import randint

def game(n):
   pass

print(game(1))
print(game(10))
```

---

### Úlohy na množiny

#### [8.4.1. Kontrola unikátnosti seznamu](https://www.fi.muni.cz/IB111/sbirka/08-datove_struktury.html#kontrola-unikatnosti-seznamu)

Napište funkci, která zkontroluje, zda předaný seznam obsahuje jen unikátní položky.

```python
def unique_check(temp):
    pass

print(unique_check([1, 5, 6, 5, 4, 9])) # False
print(unique_check([1, 5, 6, 3, 9])) # True
```


---

### Úlohy na asociatívne pole

#### [8.3.2. Frekvenční analýza písmen](https://www.fi.muni.cz/IB111/sbirka/08-datove_struktury.html#frekvencni-analyza-pismen)

Napište funkci `freq_analysis(text)`, která spočítá výskyt jednotlivých písmen (znaků) ve vstupním textu a následně tento seznam vypíše setříděný sestupně podle počtu výskytů.

```python
dummy = """Monty Python and Monty Python all over here."""

def freq_analysis(text):
    pass

freq_analysis(dummy)
```

### Random Person

Funcia vygeneruje záznam reprezentujúci náhodnú osobu.

Osoba bude mať atribúty `name, age, password, email`

`Password` bude náhodne generovane zo znakov: `A..Za..z0-1,.$!`.
`Email` bude zložený z pouzitého mena _(lowercase)_ a domény `example.com`.
`Age` bude z rozsahu `10 - 99`.

```python
from typing import Dict, List, Any

def random_person(names: List[str]) -> Dict[str, Any]:
    pass


print(random_person(["Bill","David","Susan","Jane","Kent","Brad","Sam"]))
# {'name': 'David', 'age': 45, 'email': 'david@example.com'}
```



---

### Všeobecné úlohy

#### [8.5.3. Kontrola uzávorkování](https://www.fi.muni.cz/IB111/sbirka/08-datove_struktury.html#kontrola-uzavorkovani)

Napište funkci, která pro zadaný řetězec složený pouze ze závorek `[](){}` ověří, že jde o korektní uzávorkování.

```python
def parenthesis_check(value: str) -> bool:
    pass

print(parenthesis_check('([]({()}))[]{[()]}')) # True
print(parenthesis_check('([)]')) # False
```

---

### Pokročilejšie úlohy na precvičenie práce so slovníkmi.


#### Advanced filter 

Funkcia `advanced_filter(dictlist: List[Dict[str, Any]], params: Dict[str, Any])`, 
ktorá odfiltruje prvky zoznamu slovníkov na základe viacerých parametrov.

Jednotlivé hodnoty atribútov v `params` sa budú porovnávať s hodnotami atribútov v slovníku.

Záznam je vrátený právevtedy ak su všetky hodnoty rovnajú (`and`).


```python

from typing import Dict, List, Any

# Type Alias
Person = Dict[str, Any]

PERSONS = [
    {'name': 'Peter','age': 26, email: 'peter@example.com', gender: 'm'},
    {'name': 'Thomas', 'age': 5, email: 'thomas@example.com', gender: 'm'},
    {'name': 'Jane', 'age': 30, email: 'jane@example.com', gender: 'f'},
    {'name': 'Page', 'age': 18, email: 'page@example.com', gender: 'f'},
    {'name': 'Dalek', 'age': 10000, email: 'dalek@example.com', gender: 'u'},
]


def advanced_filter(dictlist: List[Person], params: Dict[str, Any]) -> List[Person]:
    pass


# will return all the persons
print(advanced_filter(PERSONS, None)) 

# will return record with name: 'Thomas' and 'Page'
print(advanced_filter(PERSONS, {'age': 18}))

# will return just Page
print(advanced_filter(PERSONS, {'age': 18, gender: 'f'}))

# will return None
print(advanced_filter(PERSONS, {'age': 99, gender: 'f'}))
```


#### Blacklisted attributes

Funkcia `blacklisted_attributes(dictlist: List[Dict[str, Any]], params: List[str])` 
odstrani zo zoznamu všetky atribúty, ktoré sú vymenované v zozname `params`.

```python

from typing import Dict, List, Any

# Type Alias
Person = Dict[str, Any]


PERSONS = [
    {'name': 'Peter', 'age': 26, 'pass': 'Password123'},
    {'name': 'Thomas', 'age': 18, 'pass': 'He$$lo'},
    {'name': 'Jane', 'age': 30, 'pass': 'Dovolenka'},
    {'name': 'Page', 'age': 18, 'pass': 'BookIsAwesome'},
    {'name': 'Dalek', 'age': 10000, 'pass': 'Exterminate'},
]

def blacklisted_attributes(dictlist: List[Person], 
                           params: List[str]) -> List[Person]:
    pass


# Will not change the list of records
print(blacklisted_attributes(PERSONS, None)) 

# Will remove from all the records the attribute pass
print(blacklisted_attributes(PERSONS, {'pass'})) 

# Will remove from all the records the attributes pass and age 
print(blacklisted_attributes(PERSONS, ['pass', 'age'])) 

# Will remove from all the records the attributes pass and age,
# but it will ignore the attribute height
print(blacklisted_attributes(PERSONS, ['pass', 'age', 'height'])) 

```


#### Statistics per attribute

Funkcia `dict_attribute_statistics(dictlist: List[Dict[str, Any]], attr: str) -> Dict[str]:`,
ktorá spočíta nad zadaným atribútom základné štatistiky. Záznamy, u ktorých daný atribút chýba budú preskočené.

Štatistiky:
- `size` - počet hodnôt v štatistickej množine _(vo väčšine prípadov bude rovný `len(dictlist)`)_.
- `median` - Medián daných hodnôt _(usporiadajte hodnoty atributov a vyberte stredný prvok)_
- `min` - najmenší prvok
- `max` - najväčší prvok
- `average` - Priemer, iba ak je atribút čiselného typu `isinstance(attr_value, int) or isinstance(attr_value, float)` 

```python

PERSONS = [
    {'name': 'Peter', 'age': 26, email: 'peter@example.com'},
    {'name': 'Thomas', 'age': 18, 'score': 15, email: 'thomas@example.com'},
    {'name': 'Jane', 'age': 30, 'score': 12, email: 'jane@example.com'},
    {'name': 'Page', 'age': 18, 'score': 18, email: 'page@example.com'},
    {'name': 'Dalek', 'age': 10000, email: 'dalek.kaan@example.com'},
]

def dict_attribute_statistics(dictlist: List[Dict[str, Any]], 
                              attr: str) -> Dict[str]:
    pass



print(dict_attribute_statistics(PERSONS, 'width'))
# Result: {'size': 0, 'median': None, 'min': None, 'max': None}

print(dict_attribute_statistics(PERSONS, 'age'))
# Result: {'size': 5, 'median': 26, 'min': 18, 'max': 10000, 'average': 2018.4}

print(dict_attribute_statistics(PERSONS, 'score'))
# Result: {'size': 3, 'median': 15, 'min': 12, 'max': 18, 'average': 15}

print(dict_attribute_statistics(PERSONS, 'name'))
# Result: {'size': 5, 'median': 'Page', 'min': 'Dalek', 'max': 'Thomas'}
```
