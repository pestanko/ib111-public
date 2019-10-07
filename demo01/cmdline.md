# Základné príkazy
V tomto dokumente si prestavime niektoré základné príkazy a ukážky ako s nimi pracovať.

# Anatómia príkazov

Príkaz _(command)_ sa skľadá z niekolých častí:
1. meno príkazu (napr. `ls`)
2. argumenty
    - prepínače (modifikujú ako sa príkaz správa), začínajú zvyčajne znakom pomlčka `-`
        - jednopísmenkové prepínače (`-l -p -r`)
        - jednopísmenkové prepínače s hodnotou (`-l 10 -f ahoj.txt`)
        - dlhé prepínače (dve pomlčky na začiatku) (`--long --long-one arg --verbose`)
    - všeobencé argumenty (`ahoj svet ako sa mas`)
    
```bash

ls -l       # command ls and option `-l`
ls -l -a    # command ls and options `-l` and `-a`
ls -la      # same as above, `-la` is a shorthand for `-l -a` 
ls --help   # command ls with long option `--help`
ls -la Documents  # `Documents` is an argument
```


## Ukážky:

Základné ukážky a používanie príkazov na prácu so súbormi

```bash
mkdir school  # create directory `school`
ls            # print out content of the current directory
cd school     # change directory to `school`
mkdir -p ib111/demo01   # create inner directories (create ib111 first, then demo01)
cd ib111/demo01  # change directory to ib111/demo01
pwd              # Print working directory (where am I?)
touch hello.py   # create empty file `hello.py` without any content
ls               # hello.py should be there
echo "Hello!"    # Print string "Hello!" to the console
echo 'print("Hello!")' > hello.py # write content "print(...)" to the file hello.py
cat hello.py     # print out content of the file `hello.py`
nano hello.py    # launch the command line editor (nano, vim)
rm hello.py      # remove file hello.py 
```

Vytvorme súbor `hello.py` znova, tentokrát bude o nieco zložitejší.

```bash
nano hello.py
```

A obsah súboru bude nasledovný:

```python
#! /usr/bin/env python3

def print_hello(name: str):
    """Will print "Hello {name} !" for a given name.
    """
    print("Hello", name, "!")

if __name__ == '__main__':
    print_hello("Peter")
```

Obsah môžeme vložiť do súboru otvoreného v editore `nano` pomocou klávesovej skratky `CTRL + SHIFT + V`.
Súbor uložíme pomocou `CTRL-O` _(overwrite)_ a ukončíme editovanie pomocou `CTRL-X` _(close)_.

Teraz môžeme súbor spustiť pomocou príkazu:

```bash
python3 hello.py
```

Ak chceme súbor spustiť samostatne bez nutnosti písať pred ním `python3`, je potrebné spraviť súbor spustiteľným.
Na to sa v Unix svete používa príkaz na zmenu oprávnení `chmod`:

```bash
chmod +x hello.py
```

Všimnime si tiež prvým riadok skriptu (`#! /usr/bin/env python3`) - ten určuje, pomocou čoho sa náš skript bude spúšťať.

Teraz môžeme súbor `hello.py` spustiť priamo z príkazového riadka:

```bash
./hello.py   # leading ./ is required on Linux (not on Windows, hint: $PATH)
```


# Odkazy:
- <https://www.fi.muni.cz/pb071/man/#linux-bash-commands>
- <https://www.tecmint.com/linux-commands-cheat-sheet/>
- <https://www.howtoforge.com/linux-commands/>





