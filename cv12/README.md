# Cvičenie 12 Práce s textem a Bitmapová grafika

- [Práce s textem](https://www.fi.muni.cz/IB111/sbirka/11-text.html#prace-s-textem)
- [Bitmapová grafika](https://www.fi.muni.cz/IB111/sbirka/12-bitmapova_grafika.html#bitmapova-grafika)


## Pokročilá práce s řetězci

```python
# odstraní bile znaky ze zacatku a konce retezce
print('  jablko, hruska, pomeranc \n'.strip())

# rozdeli retezec dle zadaneho oddelovace a vrtati casti v seznamu
print('jablko,hruska,pomeranc'.split(','))

# nahrazeni retezce
print('jablko,hruska,pomeranc'.replace(',', '; '))

# zmena velikosti pismen
print('jABlKo'.lower(), 'jABlKo'.upper())
print()

# specialni znaky se vytvareji pomoci zpetneho lomitka \
print('tohle je \n novy radek')
print('tohle je \t tabulator')
print('tohle je apostrof \'', "a tohle jsou uvozovky \"")
print('takhle se pise zpetne lomitko \\')
```

## Čtení a zápis do souborů

[Oficiální dokumentace](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)



```python
input_file = open("input.txt", "r")   # otevreni souboru pro cteni
content = input_file.read()           # nacteni celeho obsahu souboru do retezce
lines = input_file.readlines()        # nacteni souboru souboru jako seznam radku
output_file = open("output.txt", "w") # otevreni souboru pro zapis
output_file.write("Some sentence.")   # zapis retezce do souboru
some_file.close()                     # uzavreni souboru

# alternativni konstrukce with, 
# ktera zajisti automaticke uzavreni souboru:
with open("input.txt", "r") as input_file:
    pass
```

## [Bitmapová grafika](https://www.fi.muni.cz/IB111/sbirka/12-bitmapova_grafika.html#bitmapova-grafika)

### Základní vytvoření obrázku

__Abyste mohli bez problému pracovat s obrázky, musíte mít nainstalovanou knihovnu `Pillow`. Následně musíte importovat třídu `Image`:__

```python
from PIL import Image

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Zjisti, zda je zadany bod uvnitr kruhu o danem polomeru, jehoz stred
# je uprostred ctvercoveho obrazku.
def in_circle(size, radius, x, y):
    return (x - size / 2) ** 2 + (y - size / 2) ** 2 < radius ** 2


def circle(size=150, radius=50):
    # Vytvorime objekt pro manipulaci s obrazkem
    im = Image.new("RGB", (size, size))
    # Prochazime vsechny pixely naseho obrazku a kontrolujeme, zda lezi
    # v kruhu
    for x in range(size):
        for y in range(size):
            if in_circle(size, radius, x, y):
                # Pixel na souradnicich (x, y) obarvime na cerno.
                im.putpixel((x, y), BLACK)
            else:
                # Pixel na souradnicich (x, y) obarvime na bilo.
                im.putpixel((x, y), WHITE)
    # obrazek si muzeme zobrazit
    im.show()
    # nebo jej muzeme ulozit do souboru
    im.save("demo_circle.png")


# Vykresli kruh o polomeru 50 na bilem ctverci o strane 150.
circle()
```


## Úlohy - Praca s textom

### [11.1.1. Nejčastější slova](https://www.fi.muni.cz/IB111/sbirka/11-text.html#nejcastejsi-slova)
Načtěte soubor [`sherlock-holmes.txt`](https://www.fi.muni.cz/IB111/sbirka/_downloads/1dfa0d128643dc218db043d0c142cf42/sherlock-holmes.txt) 
a vypište 10 nejčastěji se vyskytujících slov v textu. Pro zajímavost se omezte pouze na slova délky 3 a více.

```python
def most_freq_words(filename):
    pass

most_freq_words('sherlock-holmes.txt')
```

### [11.1.2. Průměrný počet slov ve větě](https://www.fi.muni.cz/IB111/sbirka/11-text.html#prumerny-pocet-slov-ve-vete)
Analyzujte text v souboru [`alice-in-wonderland.txt`](https://www.fi.muni.cz/IB111/sbirka/_downloads/ea3b02e7256b29ae9c7323a111d41388/alice-in-wonderland.txt) 
a vraťte průměrný počet slov ve větě.

```python
def average_sentence_len(filename):
    pass

print(average_sentence_len('alice-in-wonderland.txt'))
```

### [11.1.7. Analýza jmen](https://www.fi.muni.cz/IB111/sbirka/11-text.html#analyza-jmen)

Načtěte soubor [`jmena.csv`](https://www.fi.muni.cz/IB111/sbirka/_downloads/da05a19be1aafe3278012ff99f4e1756/jmena.csv). 
Implementujte funkci `most_common_names(filename)`, která ze souboru vypíše `count` nejčastěji užívaných jmen (globálně).

```python
def most_common_names(filename, count):
    pass

most_common_names('jmena.csv', 10)
```

### Jednoducha substitucia na zaklade sablony

Vašou úlohou bude implementovať funkciu, ktora spraví takzvanú substitúciu(expanziu) v dodanom texte, 
funkcia vezme na vstupe dodaný text, cestu k súboru kam uloží výstup a slovník v ktorom budú definované stubstitúcie.

V dodadom texte nahradi vyskit takzvaného substitučného výrazu na konkrétnu hodnotu.
Substitučný výraz vyzerá nasledovne `${premenna}`, kde `${}`, konštrukcia udáva, že ide o miesto kde dôjde k náhrade
a `premenna` udáva kľúč v slovníku.

```python

from datetime import datetime
from typing import Dict

EMAIL_TEXT = """Ahoj,
moje meno je ${name}.
Dnes je ${day} - ${date}.
Ostava ${days_til_christmas} dni do Vianoc.
Krasne sviatky vsetkym!

S pozdravom
${name}
"""

DAYS = ['pondelok', 'utorok', 'streda', 'stvrtok', 'piatok', 'sobota', 'nedela']

def subst_params() -> dict:
    date = datetime.now().date()
    christmas = datetime(date.year, 12, 24).date()

    return {
    'name': 'Jan Mrkva',
    'day': DAYS[date.weekday()],
    'date': date.strftime("%d.%m.%Y"),
    'days_til_christmas': (christmas - date).days 
}

def template_substitute(template: str, output: str, variables: dict):
    pass

template_substitute(EMAIL_TEXT, 'email.out.txt', subst_params())
```

Vystup by mal vyzerat nasledovne:

```
Ahoj,
moje meno je Jan Mrkva.
Dnes je utorok - 03.11.2019.
Ostava 20 dni do Vianoc.
Krasne sviatky vsetkym!

S pozdravom
Jan Mrkva
```


## Úlohy - Kreslenie

### [12.1.1. Čtverec](https://www.fi.muni.cz/IB111/sbirka/12-bitmapova_grafika.html#ctverec)

Na bílé pozadí o zadané velikosti nakreslete černý čtverec o zadané straně, jehož střed bude umístěn do středu obrázku.

```python
from PIL import Image


def square(size=250, a=70):
    pass
```

### [12.1.3. Kruh](https://www.fi.muni.cz/IB111/sbirka/secret/12-bitmapova_grafika.html#kruh)
Na bílé pozadí o zadané velikosti nakreslete černý kruh o zadaném poloměru a se středem na zadaných souřadnicích.


```python
def circle(size=150, center=(75, 75), radius=20):
    pass
```


### [12.1.6 Šachovnice](https://www.fi.muni.cz/IB111/sbirka/12-bitmapova_grafika.html#sachovnice)

Nakreslete šachovnicový vzor o zadané velikosti obrázku a šířce pruhu.

```python
def chessboard(size=150, stripe=30):
    pass
```


### [12.2.3 Stupně šedi](https://www.fi.muni.cz/IB111/sbirka/secret/12-bitmapova_grafika.html#stupne-sedi)

Napište funkci, která převede barevný obrázek na obrázek ve stupních šedi.

`GRAY = (RED + GREEN + BLUE) / 3`

```python
def grayscale(filename):
    pass
```



