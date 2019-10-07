# Git

GIT je nástroj pre správu verzií (revízií). V súčasnoti patrí k najpoužívanejším nástrojom svojho druhu. Vy sa s ním budete stretávať aj na ďalších predmetoch vyučovaných na fakulte.

## Základný prípad použitia

Máme zdrojové kódy / niekoľko súborov, ktoré chceme bezpečne uložiť´- školský projekt, cvičenia, domáci projekt, projekt v práci.

### Problémy:

- Ako súbory, ktoré som vytvoril na pracovnom/školskom PC dostanem na domáci PC?
- Ako môžem spolupracovať na projekte s mojimi kolegami/spolužiakmi?
- Potrebujem súbory vrátiť do nejakého predchádzajúceho stavu, pretože najnovšie úpravy nevedú správnym smerom

Všetky tieto problémy nástroje na správu verzií riešia. Každý nástroj trochu inak, my sa pozrieme na GIT.

## Základná práca 

Bude nás zaujímať len nazaj základná práca s GITom, takže:
- Vytvorenie repozitára (lokálne aj na serveri)
- Nahratie zmien na server
- Získanie zmien zo severu.

### Príprava

Vytvoríme si priečinok `demo01` v adresári `ib111` a nastavíme ho ako svoj aktuálny adresár:

```bash
mkdir -p ib111/demo01
cd ib111/demo01
pwd
ls 
```

Ak už adresár máte vytvorený a máte v nom súbor napríklad `hello.py`, tak to nie je žiaden problém.
Naopak, ak tam súbor `hello.py` nemáte, vytvorte si ho. Pre naše účely stačí, aby súbor existoval,
jeho obsah zatiaľ zaujímať nebude.


Pred ďalšou prácou potrebujeme GIT nastaviť. Toto nastavenie robíte vždy len prvý krát po tom co GIT nainštalujete.

Nastavenie pri prvom použití:

```bash
git config --global user.name "Jméno Příjmení"
git config --global user.email "<xlogin>@fi.muni.cz"
```

### Vytvorenie lokálneho repozitára

Vytvorme si ďalej lokálny GIT repozitár. V podstate len GITu povieme, že náš priečinok `demo01` má považovať za lokálny repozitár.
Potom všetko čo do neho odvtedy dáme, všetky súbory a všetky priečinky, budeme mocť verzovať a nahrávať na server.

Vytvorenie GIT repozitára:

```bash
$ git init  # Will initialize an empty git repository in the current directory
```

## Prvý commit

Po úspešnej inicializácii GIT-u a vytvorení lokálneho prepozitára môžeme do repozitára začať pridávať naše zmeny.

Hlavným aktérom bude súbor `hello.py` v priečinku s naším repozitárom. Zatiaľ ho ale ešte GIT neregistruje ako súčasť nášho repozitára.
GIT má totiž vlastný spôsob sledovania súborov, nepoužíva len súborový systém. Najskôr teda musíme GITu povedať, že by si mal všímať súbor `hello.py`.

Ako sa k tomuto všetkému dopátrame:

```bash
ls          # prints out the content of the directory, hello.py should be there
git status  # shows status of our repository
```

Výstup prákazu `git status` by mal vyzerať približne takto:

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
- `Untracked files:` - zoznam súborov a priečinkov, ktoré aktualne v priečinku existujú, ale nie sú v repozitári.
- `(use "git add" to track)` - GIT nám napovedá, čo môžeme spraviť


### Vytvorenie commitu _(zmeny)_

`Commit` je zmena, snapshot, ktorý si chceme poznamenať do nášho repoziráru. Commity (a nejaké ďalšie metadáta, nateraz nepodstatné)
sú jediné, čo si GIT pamätá.

Vytvorenie commitu sa skladá z dvoch častí:
- Označenie súborov, ktoré majú byť do `commitu` pridané (`git add <subor>`)
- Vytvorenie a pomenovanie _(commit message)_ commitu (`git commit -m "<message>"`)


##### Označenie súboru `hello.py`:

Označiť pomocou `git add` je možné aj viac súborov, v našom prípade si vystačíme len s jedným.

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


##### Vytvorenie commitu

Vytvorenie commitu (snapshotu) je už teraz jednoduché - stačí zavolať `git commit`

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

Potrebujete vytvorit vzdialený repozitár _(remote)_ (na serveri) a ten "spárovať" s vaším lokálnym repozitárom.

### Vytvorenie vzdialeného repozitára

Postup:

1. Prihláste sa do fakultného GitLabu - <https://gitlab.fi.muni.cz/> (xlogin + sekundárne heslo).
2. V ľavom menu vyberte položku `Projects`.
3. Kliknite na zelené tlačítko `New project`.
4. Název projektu zvoľte `ib111-demo01` a viditelnosť ponechajte na `private`.

Po vytvorení nového projektu _(repozitára)_ uvidíte inštrukcie ako tento prázdny vzdialený repozitár spárovať s vaším lokálnym.

Pozor, spárovanie je jednosmerné, chcete len povedať svojmu lokálnemu repozitáru o existencii vzdialeného.
Vzdialený repozitár o Vašom lokálnom vedieť nebude, a preto vačšinu operácii budete robiť z Vašich lokálnych kópií.

Prepojenie lokálneho repozitára so vzdialeným:

```bash
# namiesto <xlogin> zadajte Váš xlogin
git remote add origin https://<xlogin>@gitlab.fi.muni.cz/<xlogin>/ib111-demo.git
```

Tento príkaz pridá informáciu o _remote_ (vzdialenom repozitári) do Vášho lokálneho. 
Vzdialenych repozitarov môžete mať niekolko, avšak to je nad rámec tohoto dema.

Náš remote sa volá `origin` - možeme ho pomenovať ľubovolne, `origin` je zaužívané meno. 

### Nahranie zmien na server

Nahranie zmien spravíme pomocou príkazu `git push`, ktorý vezme aktuálny stav repozitára ("históriu commitov") a nahrá jeho obsah na vzdialený server.

Prikáz:
```bash
# git push <remote> <branch>
# For our example:
git push origin master

# In order not to always write the name of origin and branch we can set them as `default`
git push -u origin master 
# After you can just write without name of remote or branch
git push
```

Príkaz `git push` berie ako argumenty meno _remote_, v našom prípade `origin`, a meno `branch` ktorú chceme odoslať na server.


_Koncept `branch-í` je taktiež nad rámec tohoto dema, zatiaľ si vystačíte len s jednou branch-ou (`master`), ktorá je už predvytvorená. Po zadaní tohoto príkazu by ste mali byť požiadaní o zadanie hesla - zadajte sekundárne._


Po tom, čo ste úspešne nahrali zmeny na server si ich môžete skontrolovať na webe GitLabu.

## Stiahnutie zmien z repozitára

V prípade, že máte na svojom PC lokálnu verziu repozitára, použite príkaz `git pull`

```bash
# Go to your local repository (in your folder, like: ib111/demo01)
cd ib111/demo01

# call git pull
git pull origin master

# if you set upstream correctly (`git push -u origin master`)
# you can just call git pull without name of the remote or branch
git pull
```

Ak sa GIT bude sťažovať na nejaké konflikty znamená to, že zmeny v lokálnom repozitáre sa líšia od tých, čo sú na vzdialenom repozitáre
a je ich potrebné vyriešiť rućne. Vám by sa to však stať nemalo, minimálne nie zo začiatku. Na to aby ste zistili ako na riešenie konfliktov 
je na internete kopec návodov, nejaké sú aj v sekcii `odkazy`.

### Stiahnutie celého repozitára na svoj PC

V prípade, že na svojom PC nemáte lokálnu verziu (kópiu) repozitára, použite príkaz `git clone`

```bash
# Command will download the repository to the current directory
# It will create new folder named `ib111-demo` in your current directory
git clone https://<xlogin>@gitlab.fi.muni.cz/<xlogin>/ib111-demo.git
# To get to the local repository
cd ib111-demo
git status
git log         # will show the list of commits 
```

V prípade, že ste repozitár naklonovali, rovno sa vám nastavila `remote origin` na `https://xlogin@gitlab.fi.muni.cz/xlogin/ib111-demo.git`. 
Odital vôbec pochádza názov `origin` = z ktorého serveru ste si stiahli zmeny a voči ktorému serveru sa synchronizujete.

**POZOR:** `git clone` používate len vtedy ked chcete stiahnúť celý repozitár, ktorý nemáte na svojom PC. 
Ak repozitár existuje, používajte `git pull`.


## Úlohy:

1. Pomocou `git clone` si vytvorte novú variantu lokálneho repozitára (budete mat jak `demo01` tak `ib111-demo01`)
Pozor: musia to byť separátne priečinky - `demo01` nesmie obsahovať `ib111-demo01` a naopak.
2. Zmeňte súbor `hello.py` a vytvorte `world.txt` v `demo01`, oba nahrajte na vzdialený server. 
3. Zmeňte aktuálny adresár do `ib111-demo01` a pomocou `git pull` si stiahnite najnovšie zmeny


## Odkazy

- <https://www.fi.muni.cz/pb071/man/#git>
- <https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf>
- <https://git-scm.com/book/en/v2>


