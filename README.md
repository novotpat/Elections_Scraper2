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
Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
574724,Barchov,170,113,113,5,0,0,9,0,12,7,0,3,1,0,0,14,0,3,40,0,1,3,0,0,0,15,0
574741,Bezděkov,262,164,163,18,0,0,5,0,14,9,7,1,2,0,0,20,0,7,58,0,1,3,4,2,0,11,1
574783,Borek,226,161,159,30,0,1,12,1,12,9,2,1,3,2,0,11,0,6,34,0,0,8,1,0,1,25,0
![image](https://user-images.githubusercontent.com/71101156/178426390-fe9e47bc-8c95-4a4e-908a-bd194bed8ed9.png)

```
