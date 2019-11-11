# [Cvičenie 09 Algoritmy nad seznamy](https://www.fi.muni.cz/IB111/sbirka/08-datove_struktury.html)

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
print(queue) # deque(["Petr", "Zdenek", "Filip", "Kuba"])

queue.append("Roman") # Roman prisel na konec fronty
print(queue) # deque(["Petr", "Zdenek", "Filip", "Kuba", "Roman"])

student = queue.popleft() # prvni student ve fronte (Petr) dostal obed
print(queue, student) # deque(["Zdenek", "Filip", "Kuba", "Roman"]), student: "Petr"

student = queue.popleft() # dalsi student ve fronte (Zdenek) dostal obed
print(queue, student) # deque(["Filip", "Kuba", "Roman"]), student: "Zdenek"
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
print(points) # {"Jack":66, "Peter":0, "Denis":0, "Tom":60}

points["Peter"] += 60 # zmena hodnoty pod nejakym klicem
print(points) # {"Jack":66, "Peter":60, "Denis":0, "Tom":60}

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

Úlohy na zásobníky

### [8.1.1. Interpretace výrazu v postfixu](https://www.fi.muni.cz/IB111/sbirka/08-datove_struktury.html#interpretace-vyrazu-v-postfixu)


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

Úlohy na fronty

### [8.2.1. Má mě rád, nemá mě rád](https://www.fi.muni.cz/IB111/sbirka/08-datove_struktury.html#ma-me-rad-nema-me-rad)

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

Úlohy na množiny

### [8.4.1. Kontrola unikátnosti seznamu](https://www.fi.muni.cz/IB111/sbirka/08-datove_struktury.html#kontrola-unikatnosti-seznamu)

Napište funkci, která zkontroluje, zda předaný seznam obsahuje jen unikátní položky.

```python
def unique_check(temp):
    pass

print(unique_check([1, 5, 6, 5, 4, 9])) # False
print(unique_check([1, 5, 6, 3, 9])) # True
```


---

Úlohy na asociatívne pole

### [8.3.2. Frekvenční analýza písmen]

Napište funkci `freq_analysis(text)`, která spočítá výskyt jednotlivých písmen (znaků) ve vstupním textu a následně tento seznam vypíše setříděný sestupně podle počtu výskytů.

```python
dummy = """Monty Python and Monty Python all over here."""

def freq_analysis(text):
    pass

freq_analysis(dummy)
```


---

Všeobencné úlohy

### [8.5.3. Kontrola uzávorkování](https://www.fi.muni.cz/IB111/sbirka/08-datove_struktury.html#kontrola-uzavorkovani)

Napište funkci, která pro zadaný řetězec složený pouze ze závorek `[](){}` ověří, že jde o korektní uzávorkování.

```python
def parenthesis_check(value):
    pass

print(parenthesis_check('([]({()}))[]{[()]}')) # True
print(parenthesis_check('([)]')) # False
```

### Pokročilejšie úlohy na precvičenie práce so slovníkmi.


#### Advanced filter 

Funkcia `advanced_filter(dictlist: List[dict], params: dict)`, ktora odfiltruje prvky zoznamu slovnikov na základe viacerých parametrov.

Jednotlivé hodnoty atribútov v `params` sa budú porovnávať s hodnotami atribútov v slovníku.

Záznam je vrátený právevtedy ak su všetky hodnoty rovnajú (`and`).


```python
PERSONS = [
    {'name': 'Peter', 'age': 26, 'id': 55, email: 'peter@example.com', gender: 'm'},
    {'name': 'Thomas', 'age': 18, 'id': 26, email: 'thomas@example.com', gender: 'm'},
    {'name': 'Jane', 'age': 30, 'id': 92, email: 'jane@example.com', gender: 'f'},
    {'name': 'Page', 'age': 18, 'id': 93, email: 'page@example.com', gender: 'f'},
    {'name': 'Dalek', 'age': 10000, 'id': 0, email: 'dalek.kaan@example.com', gender: 'u'},
]


def advanced_filter(dictlist: List[dict], params: dict) -> List[dict]:
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

Funkcia `blacklisted_attributes(dictlist: List[dict], params: List[str])` 
odstrani zo zoznamu všetky atribúty, ktoré sú vymenované v zozname `params`.

```python
PERSONS = [
    {'name': 'Peter', 'age': 26, 'pass': 'Password123', email: 'peter@example.com'},
    {'name': 'Thomas', 'age': 18, 'pass': 'He$$lo', email: 'thomas@example.com'},
    {'name': 'Jane', 'age': 30, 'pass': 'Dovolenka', email: 'jane@example.com'},
    {'name': 'Page', 'age': 18, 'pass': 'BookIsAwesome', email: 'page@example.com'},
    {'name': 'Dalek', 'age': 10000, 'pass': 'Exterminate', email: 'dalek.kaan@example.com'},
]

def blacklisted_attributes(dictlist: List[dict], params: List[str]) -> List[dict]:
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




