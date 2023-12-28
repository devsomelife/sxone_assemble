# SXONE ASSEMBLE!

Short python script for people tired of manually calculating their monthly time tracking from SXONE.

## Requirements

You need either Python 3 or Docker

## TL;DR For Windows users

Export all your SXONE timesheet in one xlsx file into your default Downloads/Téléchargements folder and run in a terminal (with Docker running).

_Note: this command works for English & French windows._ 

```bash
docker run -it --rm -v %USERPROFILE%\Downloads\export_everwin.xlsx:/app/export.xlsx devsomelife/sxone_assemble:latest
```


## Usage

### Python

You need Python 3 installed, grab the script, then you just run:

```bash
python sxone_assemble.py /path/export_everwin.xlsx [month] [year]
```

### Docker

You just need docker. Then you run:
Note that the mounted name of the file (/app/export.xlsx) is critical and must not be changed.

```bash
docker run -it --rm -v /path/export_everwin.xlsx:/app/export.xlsx devsomelife/sxone_assemble:latest [month] [year]
```

## Notes

All [month] values default to the current month if not specified  
All [year] values default to the current year if not specified. The [month] parameter is required is you want to specify the [year]

## Examples

```bash
python sxone_assemble.py /path/export_everwin.xlsx

python sxone_assemble.py /path/export_everwin.xlsx 11

python sxone_assemble.py /path/export_everwin.xlsx 5 2021
```

And it's docker equivalent

```bash
docker run -it --rm -v /path/export_everwin.xlsx:/app/export.xlsx devsomelife/sxone_assemble:latest

docker run -it --rm -v /path/export_everwin.xlsx:/app/export.xlsx devsomelife/sxone_assemble:latest 11

docker run -it --rm -v /path/export_everwin.xlsx:/app/export.xlsx devsomelife/sxone_assemble:latest 5 2021
```

## PREPARING THE CSV FILE

### FRENCH

Depuis le menu Temps, choisir Feuilles de temps.

![/images/sxone01.png](images/sxone01.png)


Séléctionnez les feuilles qui vous intéressent (ou toutes, on s'en fiche), puis Exporter et "Exporter les temps saisis des éléments séléctionnés"

![images/sxone02.png](images/sxone02.png)

Et zou, si vous avez votre fichier dans votre répertoire standard de Téléchargements (qui reste quand même Downloads derrière) par exemple

```bash
docker run -it --rm -v %USERPROFILE%\Downloads\export_everwin.xlsx:/app/export.xlsx devsomelife/sxone_assemble:latest
```

## Maintainers

[@somelife_dev](https://github.com/devsomelife).

## Contributing

Feel free to dive in! [Open an issue](https://github.com/devsomelife/sxone_assemble/issues/new/choose) or submit PRs.
