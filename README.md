# Elections_Scraper2
Tento program byl vytvořen jako poslední projekt Python Akademie od Engeto. Projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017. Odkaz k prohlédnutí najdete [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

## Instalace knihoven
Knihovny, které jsou použity v kódu jsou uložené v souboru `requirements.txt`. Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spustit v příkazové řádce ve složce projektu:
```
pip3 --version                          # ověří verzi manažeru
pip3 install -r requirements.txt        # nainstaluje knihovny
```

## Spuštění projektu
Spuštění souboru `scraper2.py` v rámci příkazového řádku požaduje dva povinné argumenty v přesném pořadí:
  1. Odkaz na výběr obce v uvozovkách
  2. Název výsledného souboru `csv`
```
python scraper2.py <"odkaz_vyber_obce"> <vysledny_soubor>
```
Následně se vám stáhnou výsledky a uloží do složky projektu jako soubor csv.

## Ukázka projektu
Výsledky hlasování pro obec Pardubice:
  1. argument: `"https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5302"`
  2. argument: `vysledky_Pardubice.csv`

Spuštění programu:

  `python scraper2.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5302" vysledky_Pardubice.csv`

Průběh stahování:
```
Run the file scraper2.py.
Save to file vysledky_Pardubice2.csv.
Termination the election-scraper.
```
Částečný výstup:
```

```
