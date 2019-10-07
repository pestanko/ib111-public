# Základné git workflows

Cheat-sheet základných postupov práce a príkazov pre `GIT`.

## Inicializácia GIT-u

```bash
git config --global user.name "Jméno Příjmení"
git config --global user.email "<XLOGIN>@fi.muni.cz"
```

## Vytvorenie alebo stiahnutie repozitáru

```bash
# Creates new empty local repository
git init 
# Clones existing repository from the remote
git clone https://xlogin@gitlab.fi.muni.cz/xlogin/ib111-demo.git
```

## Stiahnutie zmien z existujúceho repozitára

```bash
git pull origin master
# or just 
git pull
```

## Vytvorenite zmien a nahranie zmien na vzdialený repozitár

```bash
git add <files or directories>
git commit -m "message"
git push
```

## Pomocné príkazy

```bash
git status      # Show status of the repository
git log         # Show all the commits in the repository
git help        # Show help
```
