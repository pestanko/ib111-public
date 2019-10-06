# Git

GIT je nástroj pre správu verzii (revízii). V súčasnoti patrí k najpoužívanejším nástrojom z tejto kategórie. Vy sa s ním budete stretávať aj na ďalších predmetoch vyučovaných na fakulte.

## Základný use-case

V podstate mám moje zdrojové kódy - školský projekt, cvičenia, domáci projekt, projekt v práci.

### Problémy:

- Ako tieto súbory co som vytvoril na pracovnom/školskom PC dostanem na domáci PC?
- Ako môžem spolupracovať na projekte s otatnými kolegami/spolužiakmi?
- Mám rozpracované riešenie, ktoré nikam nevedie a potrebujem sa "vrátiť" do predchádzajúceho stavu.

Všetky tieto problémy nástroje na správu verzii riešia. Každý po svojom, my sa však pozrieme na GIT.

## Základná práca 

Nás bude zaujímať len naozaj základná práca, ktorá spočíva:
- Vytvoriť repozitár (lokálne aj na serveri)
- Nahrať zmeny na server
- Stiahnúť si zmeny zo severu.


### Príprava

Vytvoríme si priečinok `demo01` v adresári `ib111` a nastavíme ho ako svoj aktuálny adresár:

```bash
mkdir -p ib111/demo01
cd ib111/demo01
pwd
ls 
```

Ak už adresaŕ máte vytvorený a máte v nom súbor napríklad `hello.py` tak to nie je žiaden problem.
Naopak, ak tam súbor `hello.py` nemáte, vytvorte si ho, v postate stací ak ten súbor len vypíše `hello`,
samotný obsah toho súboru nás zatiaľ zaujímať nebude.

### Vytvorenie lokálneho repozitáru

Vytvorme teraz GIT repozitár, v podstate co my spravíme je, že prehlásime náš priečinok `demo01` za lokálny repozitar.
To znamená, všetko co do neho od teraz dáme, všetky súbory a všetky priečinky budeme mocť verzovať a narať na server.

Vytvorenie GIT repozitára:

```bash
$ git init  # Will initialize an empty git repository in the current directory
```

Po zadaní tohoto príkazu sa nám vytvorí v aktuálnom priečinku prázdny git repozitár.

Pred tým ako budete mocť pridávať vaše zmeny do repozitára, tak je potrebné GIT nastaviť.
Toto nastavenie robíte vždy len prvý krát po tom co GIT nainštalujete.

Nastavenie pri prvom použití:

```bash
git config --global user.name "Jméno Příjmení"
git config --global user.email "<XLOGIN>@fi.muni.cz"
```

## Prvý commit

Po úspešnej inicializácii GIT-u a vytvorení lokálneho prepozitára je čas aby sme sa naučili ako pridať do repozitára naše zmeny.
Spomínate na súbor `hello.py`, ten by sa mal nachádzať v priečinku s náším repozitárom, avšak pozor! Súbor nie je v našom repozirári,
lebo sme ho tam ešte nedali, doslova sme ešte nepovedali GIT-u, že tento súbor by si mal všímať

Ako sa teda k tomuto všetkému dopátrame:

```bash
ls          # should print out the content of the directory, and hello.py should be there
git status  # show status of our repository
```

Výstup git status by mal vyzerat nejak nasledovne:

```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	hello.py

nothing added to commit but untracked files present (use "git add" to track)
```

Postatné informácie: 

- `No commits yet` - zaťiaľ nemamé žiadne `commity` _(zmeny)_.
- `Untracked files:` - bude obsahovať zoznam súborov a priečinkov, ktoré aktualne v priečinku existuju,
ale nie sú v repoziráre.
- `(use "git add" to track)` - rovno nám GIT hovorí čo máme spraviť


### Vytvorenie commitu _(zmeny)_

`Commit` je zmena, snapshot, ktorý si chceme poznamenať do nášho repoziráru.

Vytvorenie commitu sa skladá z dvoch častí:
- Označenie súborov, ktoré majú byť do `commitu` pridané (`git add <subor>`)
- Vytvorenie a pomenovanie _(commit message)_ commitu (`git commit -m "<message>"`)


##### Označenie súboru `hello.py`:
Označiť pomocou `git add` je možné aj viac súborov v našom prípade si vystačíme len s jedným.

```bash
git add hello.py
git status
```

Výstup `git status`:

```
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   hello.py

```

Podstatná informácia: `Changes to be committed:` a `new file:   hello.py`.


##### Vytvorenie commitu ako takého

Vytvorenie commitu (snapshotu) je už teraz jednoduché stačí zavolať `git commit`

```bash
git commit -m "Adding hello.py to my repository"
```

Výstup:

```
[master (root-commit) dbbea67] Adding hello.py to my repository
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 hello.py
```

Práve sa nám podarilo vytvoriť nový commit.

## Nahranie zmien na server

Fakulta ponúka vlastný GIT server, na ktorý si môžete svoje zmeny nahrávať. 

V podstate potrebujete vytvorit vzdialený repozitár _(remote)_ a ten "spárovať" s lokálnym.

### Vytvorenie vzdialeného repozirára

Postup:

1. Prihláste sa do fakultného GitLabu - <https://gitlab.fi.muni.cz/> (fakultné prihlásenie).
2. V ľavom menu vyberte položku `Projects`.
3. Kliknite na zelené tlačítko `New project`.
4. Název projektu zvoľte `ib111-demo01` a viditelnosť ponechajte na `private`.

Po vytvorení nového projektu _(repozitára)_ uvidíte inštrukcie, ako tento prázdny vzdialený repozitár spárovať s vaším lokálnym.

Pozor, spárovanie je jednosmerné a vy chcete len povedať svojmu lokálnemu repozitáre o existencii vzdialeného, čize,
vzdialený repozitár o Vašom lokálnom vedieť nebude, a preto vačšinu operácii budete musieť robiť z Vašich lokálnych kópii.

Prepojenie lokálneho repozitára so vzdialeným:

```bash
git remote add origin https://xlogin@gitlab.fi.muni.cz/xlogin/ib111-demo.git
```

Tento príkaz pridá informáciu o _remote_ (vzdialenom repozitáre do Vášho lokálneho). 
Vzdialenych repozitarov môžete mať niekolko, avšak to nad rámec tohoto dema.

Náš remote sa volá `origin` - možeme ho pomenovať ľubovolne, avšak `origin` je zaužívané meno(neskôr vysvetlím prečo). 

### Nahranie zmien na server

Nahranie zmien spravíme pomocou príkazu `git push`, ktorý vezme aktuálny stav repozitára a nahrá jeho obsah na vzdialený server.

Prikáz:
```bash
# git push <remote> <branch>
# Our for our example:
git push origin master

# In order not to always write the name of origin and branch we can set them `as default`
git push -u origin master 
# After you can just write without name of remote or branch
git push
```

Príkaz `git push` berie ako argumenty meno _remote_ v našom prípade `origin` a meno `branch` ktorú chceme odoslať na server.


_Koncept `branch-ý` je taktiež nad rámec tohoto dema, vy si zatial vystačíte len s jednou branch-ou a to `master`, ktorá je už predvytvorená. Po zadaní tohoto príkazu by ste mali byť požiadaný o zadanie hesla - zadajte fakultné._


Po tom, čo ste úspešne nahrali zmeny na server môžete si ich skontrolovať tým, 
že sa pozriete ci vám pribudli nejake commity na Gitlabe.


## Stiahnutie zmien z repozitára

V prípade, že máte na svojom PC už lokálnu verziu repozitára, pouzite príkaz `git pull`

```bash
# Go to your local repository (in your folder, example: ib111/demo01)
cd ib111/demo01

# call git pull
git pull origin master

# if you set upstream correctly `git push -u origin master`
# you can just call git pull without name of the remote or branch
git pull
```

Ak by ste mali nejake konflikty, to znamená, že zmeny v lokálnom repozitáre sa líšia od tých, čo sú na vzdialenom repozitári,
tak je ich potrebné vyriešiť. Vám by sa to však stat nemalo, minimalne nie zo začiatku. Na to aby ste zistili ako na to, 
je na internete kopec navodov, nejaké sú aj v sekcii odkazy.

### Stiahnutie celého repozitára na svoj PC

V prípade, že na svojom PC nemáte lokálnu verziu (kópiu) repozitára, použite príkaz `git clone`

```bash
# Command will download the repository to the current directory
# It will create new folder named `ib111-demo` in your current directory
git clone https://xlogin@gitlab.fi.muni.cz/xlogin/ib111-demo.git
# To get to the local repository
cd ib111-demo
git status
git log         # will show the list of comits 
```

V prípade, že ste repozitár naklonovali, rovno sa vám nastavila `remote origin` na `https://xlogin@gitlab.fi.muni.cz/xlogin/ib111-demo.git`. 
Odital vôbec pochádza názov `origin` = z ktorého serveru ste si stiahli zmeny a voci ktorému serveru sa synchronizujete.

**POZOR:** `git clone` používate len vtedy ked chcete stiahnúť celý repozitár, ktorý nemáte na svojom PC. 
Ak repozitár existuje, používajte `git pull`.


## Úlohy:

1. Pomocou `git clone` si vytvorte novú variantu lokálneho repozitára (budete mat jak `demo01` tak `ib111-demo01`)
Pozor: musia to byť separátne priečinky - `demo01` nesmie obsahovať `ib111-demo01` a naopak.
2. Zmente súbor `hello.py` a vytvorte `world.txt` v `demo01`, oba nahrajte na vzdialený server. 
3. Zmente adresár do `ib111-demo01` a pomocou `git pull` si stiahnite najnovšie zmeny


## Odkazy

- <https://www.fi.muni.cz/pb071/man/#git>
- <https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf>
- <https://git-scm.com/book/en/v2>


