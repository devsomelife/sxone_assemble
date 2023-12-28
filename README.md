# SXONE ASSEMBLE!

Petit script Python pour récupérer en 30 secondes son cumul mensuel de temps par affaire depuis un export SXONE.

## Pré-requis

Vous avez besoin de Docker (Docker engine sur Windows) ou de Python 3

## TL;DR Pour les utilisateurs Windows


* Exporter vos temps SXONE comme expliqué ici : [Préparer le fichier CSV](#préparer-le-fichier-csv)
* Lancez la commande suivante depuis un terminal standard Windows (pas Powershell ou WSL mais une invite de commande classique).

```bash
docker run -it --rm -v %USERPROFILE%\Downloads\export_everwin.xlsx:/app/export.xlsx devsomelife/sxone_assemble:latest
```


## Utilisation

### Python

Installez Python 3.x, chopez le script sxone_assemble.py, exportez vos temps et lancez : 

```bash
python sxone_assemble.py /path/export_everwin.xlsx [month] [year]
```

### Docker

Encore plus simple, exportez vos temps et lancez la commande suivante, en remplacant "/path/export_everwin.xlsx" avec le chemin de votre fichier d'export. 

NE PAS CHANGER /app/export.xlsx DANS LA COMMANDE, le nom du fichier dans le conteneur est important.

```bash
docker run -it --rm -v /path/export_everwin.xlsx:/app/export.xlsx devsomelife/sxone_assemble:latest [month] [year]
```

## Notes

Le paramêtre [month] prend le mois en cours par défaut si pas spécifié  
Le paramêtre [year] prend l'année en cours par défaut si pas spécifiée. Le paramêtre [mois] est requis si vous spécifiez [year]

## Exemples

```bash
python sxone_assemble.py /path/export_everwin.xlsx

python sxone_assemble.py /path/export_everwin.xlsx 11

python sxone_assemble.py /path/export_everwin.xlsx 5 2021
```

La même chose pour Docker

```bash
docker run -it --rm -v /path/export_everwin.xlsx:/app/export.xlsx devsomelife/sxone_assemble:latest

docker run -it --rm -v /path/export_everwin.xlsx:/app/export.xlsx devsomelife/sxone_assemble:latest 11

docker run -it --rm -v /path/export_everwin.xlsx:/app/export.xlsx devsomelife/sxone_assemble:latest 5 2021
```

## Préparer le fichier CSV

Depuis le menu Temps, choisir Feuilles de temps.

![/images/sxone01.png](images/sxone01.png)


Séléctionnez les feuilles qui vous intéressent (ou toutes, on s'en fiche), puis Exporter et "Exporter les temps saisis des éléments séléctionnés".

Note : Si vous choisissez toutes les feuilles, attention, ce sont en fait seulement les feuilles affichées (et donc paginées).

![images/sxone02.png](images/sxone02.png)

Et zou, si vous avez votre fichier dans votre répertoire standard de Téléchargements (qui reste quand même Downloads derrière) par exemple, depuis une invite de commande (et non Powershell ou WSL) : 

```bash
docker run -it --rm -v %USERPROFILE%\Downloads\export_everwin.xlsx:/app/export.xlsx devsomelife/sxone_assemble:latest
```

## Maintainers

[@somelife_dev](https://github.com/devsomelife).

## Contributing

Feel free to dive in! [Open an issue](https://github.com/devsomelife/sxone_assemble/issues/new/choose) or submit PRs.
