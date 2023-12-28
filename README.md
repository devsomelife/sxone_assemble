# SXONE ASSEMBLE!

Short python script for people tired of manually calculating their time tracking on SXONE.

# HOW TO

## Python

You need Python 3 installed, then you just run:

```bash
python sxone_assemble.py /path/export.csv [month] [year]
```

## Docker

You just need docker. Then you run:
Note that the mounted name of the file (/app/data.csv) is critical and must not be changed.

```bash
docker run -it --rm -v /path/export.csv:/app/data.csv sxone_assemble:latest [month] [year]
```

# Notes

All [month] values default to the current month if not specified  
All [year] values default to the current year if not specified. The [month] parameter is required is you want to specify the [year]

# Examples

```bash
python sxone_assemble.py /path/export.csv

python sxone_assemble.py /path/export.csv 11

python sxone_assemble.py /path/export.csv 5 2021
```

And it's docker equivalent

```bash
docker run -it --rm -v /path/export.csv:/app/data.csv sxone_assemble:latest

docker run -it --rm -v /path/export.csv:/app/data.csv sxone_assemble:latest 11

docker run -it --rm -v /path/export.csv:/app/data.csv sxone_assemble:latest 5 2021
```

# PREPARING THE CSV FILE

## FRENCH

Depuis le menu Temps, choisir Feuilles de temps.

![/images/sxone01.png](images/sxone01.png)


Séléctionnez les feuilles qui vous intéressent (ou toutes, on s'en fiche), puis Exporter et "Exporter les temps saisis des éléments séléctionnés"

![images/sxone02.png](images/sxone02.png)
