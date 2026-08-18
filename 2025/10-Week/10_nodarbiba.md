# 10. nodarbība. Funkcijas, moduļi, paketes

## 1. uzdevums. Vienkāršu funkciju izveide

**Mērķis: apgūt funkciju izveidi.**

Izveido funkciju `add`, kas pieņem divus skaitļus kā parametrus un atgriež to summu. Tāpat izveido funkcijas `subtract`, `multiply` un `divide`.

Neaizmirsti par datu validāciju! Pārliecinies, ka funkcijām tiek nodoti tikai skaitļi. Ja tiek nodoti nederīgi dati (piemēram, teksts), funkcija atgriež atbilstošu kļūdas ziņojumu. Validācijai var noderēt funkcija `isinstance()`.

*Papildus:* Izveido funkciju `power(a, b)`, kas atgriež pirmā skaitļa pakāpi ar otro, un funkciju `modulus(a, b)`, kas atgriež pirmā skaitļa dalījuma atlikumu ar otro.

Koda pārbaudei drīkst izmantot:

```python
print(add(5, 3))
print(subtract(10, 2))
print(multiply(4, 3))
print(divide(10, 2))
print(power(2, 3))
print(modulus(10, 3))
print(add(5, 'a'))
print(divide(5, 0))
```

## 2. uzdevums. Funkcija ar noklusējuma parametru

**Mērķis: apgūt funkciju ar noklusēto parametru izveidi.**

Izveido funkciju `greet`, kas pieņem vienu parametru — vārdu, ar noklusēto vērtību `draugs`, un atgriež ziņojumu **Sveiks, <vārds>!**.

*Papildus:* pievieno parametru `language` ar noklusējuma vērtību `lv` (latviešu). Atkarībā no valodas parametra, sveiciens tiktu izteikts attiecīgajā valodā (piemēram, "Sveiks" latviešu, "Hello" angļu, "Bonjour" franču utt.).

## 3. uzdevums. Lambda funkcijas izmantošana

**Mērķis: apgūt `lambda` funkcijas izmantošanu.**

Izveido lambda funkciju, kas aprēķina skaitļa kvadrātu. Pārbaudi to, izsaucot ar vairākiem skaitļiem.

*Papildus:*

1. Izveido lambda funkciju, kas aprēķina, vai skaitlis ir pāra vai nepāra, atgriežot attiecīgu tekstu.
2. Izveido sarakstu ar dažādām lambdas funkcijām, piemēram, kvadrāts, kubs, kvadrātsakne, un piemēro katru no saraksta funkcijām uz noteiktu skaitli.

`lambda` funkcijas izmantošanas paraugs:

```python
summa = lambda c: c+2
print(summa(4))
```

## 4. uzdevums. Rekursīva funkcija

**Mērķis: apgūt rekursīvu funkciju izveidi.**

Izveido funkciju `factorial`, kas aprēķina skaitļa faktoriālu, izmantojot rekursiju. Piemēram, `factorial(5)` atgriež 120.

*Papildus:* izveido rekursīvu funkciju `fibonacci(n)`, kas atgriež n-to Fibonaci skaitli.

## 5. uzdevums. Moduļa izveide un importēšana

**Mērķis: apgūt moduļu izveidi un importēšanu.**

Izveido *Python* moduli `math_operations.py`, kas satur matemātiskās darbības funkcijas (`add`, `subtract`, `multiply`, `divide`). Importē šo moduli citā *Python* failā un izmanto funkcijas.

*Papildus:*

1. Piešķir papildus funkcionalitāti – pievieno funkcijas, kas aprēķina logaritmus (`log(a, base)`), sinusu (`sin(angle)`), un kosinusu (`cos(angle)`). Lieto *Python* standarta bibliotēkas `math` funkcijas.
2. Izmanto `__all__`: ierobežo moduļa eksporta funkcijas, izmantojot `__all__` sarakstu, lai kontrolētu, kas tiek importēts, kad tiek izmantots `from math_operations import *`.

`main.py` datnes paraugs:

```python
import math_operations
print(math_operations.add(10, 5))
print(math_operations.subtract(10, 5))
print(math_operations.multiply(10, 5))
print(math_operations.divide(10, 5))
print(math_operations.log(10, 10))
print(math_operations.sin(90))
print(math_operations.cos(0))
```

## 6. uzdevums. Moduļu un paketes izveide

**Mērķis: apgūt moduļu un paketes izveidi.**

Izveido *Python* paketi `geometry`, kas satur divus moduļus — `circle.py` un `rectangle.py`. Moduļos izveido funkcijas, kas aprēķina apļa un taisnstūra laukumu un perimetru.

*Papildus:* izveido moduļus `triangle.py` un `square.py`, kas satur funkcijas trijstūra laukuma un perimetra, kā arī kvadrāta laukuma un perimetra aprēķināšanai.

## 7. uzdevums. Moduļu un standarta bibliotēku izmantošana

**Mērķis: apgūt moduļu un standarta bibliotēku izmantošanu.**

Izmanto standarta *Python* bibliotēku `random`, lai izveidotu funkciju `roll_dice`, kas simulē kauliņu ripināšanu un atgriež rezultātu (no 1 līdz 6). Izveido arī funkciju, kas veic vairākus kauliņu metienus un atgriež visus rezultātus.

*Papildus:* izmanto `time` bibliotēku, lai pievienotu aizkavēšanos starp metieniem un parādītu metiena rezultātu katru sekundi.

## Papildus uzdevumi

**Papildus uzdevumi prasmju nostiprināšanai.**
*Izpilde nav obligāta, bet ir vēlama!*

1. Izveidot funkciju `salidzinat(a, b)`, kura kā argumentu izmanto vārdus (*string* tipa mainīgos). Programma uz ekrāna izvada tekstu, pasakot, cik burtu ir katrā vārdā, un abu vārdu salīdzinājumu: kurš vārds ir garāks, kurš īsāks, varbūt vienādi gari?
2. Izveidot funkciju `mazakais(saraksts)`, kuru paredzēts lietot sarakstiem, kas satur skaitļus. Funkcija uz ekrāna izvada pašu sarakstu, tā mazāko elementu un elementa pozīciju sarakstā. Definēt arī īpašu atbildi gadījumam, ja funkcijai tiek padots tukšs saraksts (ar garumu 0 elementu). Neizmantot iebūvētās sarakstu funkcijas `saraksts.index()`, `min(saraksts)` u.c.
3. Izveidot funkciju, kura mēģina uzminēt slepenas laboratorijas piekļuves kodu (4 līdz 6 cipari), un tā meklē naturālus gadījuma skaitļus (izmantojot paketi `random`) tik ilgi, kamēr atrod tādu, kas vienāds ar norādīto kodu. Funkcija atgriež pilno gadījuma skaitli (kodu), kā arī skaitļa minēšanas reizi. Piezīme: 6 ciparu kodam tas var aizņemt vairākas sekundes aprēķinu laikā.
4. Daļu veidotājs. Izveidot funkciju, kurai ir 2 *veselu* skaitļu argumenti `a`, `b`. Funkcija uz ekrāna izvada skaitļu `a` un `b` dalījumu teksta formā. Funkcijai jāvar tikt galā arī ar jauktām daļām, jāspej noīsināt daļas. Piemēram, $a=20$, $b=8$ gadījumā uz ekrāna jāizvada **Dalījums ir: 2 un 1/2.**
5. Matricu reizināšana. Izveidot funkciju, kurai padot divas matricas un kura atgriež šo matricu reizinājumu. Matricas tiek padotas vektorizētā formā, piemēram, $2 \times 3$ matricu $\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$ padotu kā sarakstu sarakstu `[[1, 2, 3], [4, 5, 6]]`. Paredzēt funkcijas atbildi, ja matricu dimensijas ir pretrunā ar to reizināšanas likumiem. Neizmantot pakotni `numpy` funkcijas izveidei, bet to var importēt pārbaudei.
