# 2. nodarbība. Ievads Python, pirmās programmas

## 1. uzdevums

Nosaki tipu šādiem mainīgajiem:

```python
b=3.14
c=7/2
d=7//2
s="teksts"
z=2+3j
```

## 2. uzdevums

Vairāki mainīgie reizē.

Uzraksti programmu, kas samaina x un y vietām.

```python
x, y = 2, 3
print(x, y)
```

## 3. uzdevums

Skaitļi binārajā un heksadecimālajā sistēmā

**Kādas ir mainīgo vērtības decimālajā sistēmā?**

```python
n=0b10001111
m=0x8f
```

**Papildus uzdevumi prasmju nostiprināšanai.  
_Izpilde nav obligāta, bet ir vēlama!_**

1. Definēt trīs veselu skaitļu mainīgos. Veikt ar tiem 5 dažādas aritmētisku darbību kombinācijas pēc izvēles un izvadīt rezultātu uz ekrāna. Izvadam uz ekrāna ir pievienots arī teksts ar atšifrējumu, piemēram, ja a=2, b=3 un c=5 uz ekrāna izvada: a+b\*\*c = 245, kā arī (a + b)/c = 1 un vēl trīs darbības.
2. Spiediena mērvienības. Izveidojiet programmu, kas lietotāja ievadīto spiedienu kPa pārveidos uz PSI, mmHg un atmosfērās. Uz ekrāna jāizvada spiediens visās vienībās, Koeficientus un nepieciešamās formulas nepieciešams atrast internetā.
3. Izveidot programmu, kas prasa ievadīt planētas masu un blīvumu. Pēc šo lielumu ievades, programma uz ekrāna parāda tekstu, kur pateikts, kāds ir planētas rādiuss.
4. Skaitļu formatēšana ([špikeris](https://mkaz.blog/working-with-python/string-formatting)). Izveidot programmu, kurā ir definēts mainīgais ar skaitlisku vērtību: daļskaitli starp 1 un 10 miljoniem (piemēram, 3412352.6234). Programma izvada uz ekrāna šī mainīgā vērtību noformētu trīs dažādos veidos:
    * normālformā ar trīs zīmīgajiem cipariem un vienmēr parādītu zīmi (piemēram, +3.4e+06),
    * ar tūkstošiem atdalītiem ar komatu (piemēram, 3,412,352.6234) un
    * ar diviem cipariem aiz komata (piemēram, 3412352.62).
