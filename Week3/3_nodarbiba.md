# 3. nodarbība. Programmas izpildes secības kontrole, atkļūdošana

## 1. uzdevums

### Mērķis: apgūt `if`, `else` un `elif` lietošanu

Uzrakstiet *Python* programmu, kas prasa lietotājam ievadīt temperatūru Celsija grādos un pēc tam aprēķina un parāda ekvivalento temperatūru:

- Fārenheitos: $F = C \times \frac{9}{5} + 32$
- Kelvinos: $K = C + 273,15$

Pēc temperatūras pārvērdošanas programmai:

1. Jāpārbauda, vai temperatūra nav zem absolūtās nulles (mazāka par -273,15°C). Ja tā ir mazāka, izdrukājiet brīdinājumu: **Temperatūra zem absolūtās nulles fiziski nav iespējama.**

2. Ja temperatūra ir derīga:

- Ja Fārenheitos temperatūra ir augstāka par 212 °F, izdrukājiet **Temperatūra ir virs ūdens viršanas temperatūras.**
- Ja Fārenheitos temperatūra ir zemāka par 32 °F, izdrukājiet **Temperatūra ir zem ūdens sasalšanas punkta.**
- Pretējā gadījumā izdrukājiet **Temperatūra ir starp ūdens sasalšanas un viršanas temperatūru.**

Pilnveidojiet programmu, pievienojot nosacījumu, kurā, ja lietotājs ievada temperatūru zem absolūtās nulles (mazāku par -273,15°C), programmai nekavējoties jāapstājas, izdrukājot ziņojumu: **Temperatūra zem absolūtās nulles nav iespējama.**

## 2. uzdevums

### Mērķis: apgūt `while` cikla izmantošanu

Uzrakstiet *Python* programmu, kas lūdz lietotājam uzminēt aptuveno gaismas ātrumu vakuumā (metros sekundē).

- Programmai jādarbojas līdz lietotājs to pareizi uzminēs (pareizā atbilde: 299 792 458 m/s).
- Ja ievadītais minējums ir pārāk liels, izdrukājiet **Pārāk liels skaitlis!**
- Ja ievadītais minējums ir pārāk zems, izdrukājiet **Pārāk mazs skaitlis!**
- Kad pareizā atbilde ir uzminēta, izdrukājiet **Pareizi! Gaismas ātrums ir 299 792 458 m/s.**

Neaizmirstiet izmantot `break`, lai apturētu (neizveidotos bezgalīgs cikls)!

## 3. uzdevums

### Mērķis: apgūt cikla `while` izmantošanu

Izveidojiet programmu, kas lūdz ievadīt paroli, lai piekļūtu fizikas laboratorijai.

- Parole ir "E=mc^2".
- Ja lietotājs ievada nepareizu paroli, izdrukājiet **Nepareiza parole, mēģiniet vēlreiz.**
- Kad ir ievadīta pareizā parole, izdrukājiet **Piekļuve piešķirta.**

Papildus uzdevums ar `break`:

- Ļaujiet lietotājam trīs reizes mēģināt ievadīt paroli. Pēc trim neveiksmīgiem mēģinājumiem izmantojiet `break`, lai beigtu ciklu, un izdrukājiet
**Pārāk daudz nepareizu mēģinājumu, piekļuve liegta.**

## 4. uzdevums

### Mērķis: apgūt, kā strādāt ar sarakstiem, izmantojot ciklu `for`

Uzrakstiet programmu, kurā ir dažādu vienādojumu saraksts, piemēram, `["F = ma", "E = mc^2", "V = IR", "P = IV", "K.E. = 1/2 mv^2"]`. Izmantojiet `for` ciklu, lai izdrukātu katru vienādojumu jaunā rindā.

Izmantojot `break`, apturiet atlikušo vienādojumu drukāšanu, tiklīdz ir atrasts "E = mc^2".

## 5. uzdevums

### Mērķis: apgūt, kā izmantot iegultos ciklus (*nested loops*)

Izmantojot iegulto ciklu, uzrakstiet programmu, kas no saraksta izveido diagonālo matricu un to izvada.

Piemēram, ievaddati: `[0, 1, 2, 3]` un izvada:

```bash
0 0 0 0
0 1 0 0
0 0 2 0
0 0 0 3
```

## 6. uzdevums

### Mērķis: apgūt loģisko funkciju `and`, `or`, `not` izmantošanu

Uzrakstiet programmu, kas iedala veselu skaitļu sarakstu dažādās grupās, pamatojoties uz nosacījumiem. Izmantojiet `and`, `or` un `not`, lai izveidotu loģiskās izteiksmes. Lai izlaistu vērtības, izmantojiet `continue`.

Ievaddati: veselu skaitļu (`int`) saraksts.

Katram skaitlim sarakstā:

- Ja skaitlis ir negatīvs un pāra, izlaidiet skaitli, izmantojot `continue`.
- Ja skaitlis ir pozitīvs un pāra, programmai jāizvada **Pozitīvs un pāra.**
- Ja skaitlis ir negatīvs un nepāra, programmai jāizvada **Negatīvs un nepāra.**
- Ja skaitlis ir pozitīvs un nepāra, programmai jāizvada **Pozitīvs un nepāra.**
- Ja skaitlis ir 0, programmai jāizvada **Nulle nav ne pozitīva, ne negatīva.**
- Ja skaitlis ir no 5 līdz 15 (ieskaitot), programmai jāizvada **Skaitlis ir diapazonā: no 5 līdz 15.**
- Ja skaitlis ir mazāks par -10 vai lielāks par 20, programmai jāizvada **Ārpus diapazona.**

## 7. uzdevums

### Mērķis: apgūt `match-case` izmantošanu

Uzrakstiet programmu, kas izmanto `match-case` struktūru, lai aprēķinātu dažādus fizikālos lielumus, pamatojoties uz lietotāja ievaddatiem. Lietotājam jāizvēlas, ko viņš vēlas aprēķināt un jāsniedz ievaddatus, pamatojoties uz kuriem programma izvada gala rezultātu. Piemēri aprēķiniem:

- Spēks (F = m * a, kur m ir masa un a ir paātrinājums)
- Gravitācijas spēks ($F = G \times m1 \times m2 / r^2$, kur G ir gravitācijas konstante, m1 un m2 ir masas, un r ir attālums starp tām)
- Kinētiskā enerģija ($KE = 0,5 \times m \times v^2$, kur m ir masa un v ir ātrums)
- Potenciālā enerģija ($PE = m \times g \times h$, kur m ir masa, g ir gravitācija un h ir augstums)

Programmai jāsniedz informācija lietotājam, ko iespējams aprēķināt, un tad jāpierasa nepieciešamās vērtības (masa, ātrums utt.), lai veiktu aprēķinu.

1. papildus uzdevums – programma lūdz ievadīt pareizu izvēli, ja lietotājs veicis nevalidu aprēķina izvēli, kā arī pēc veiksmīga aprēķina piedāvā atkārtoti aprēķināt citu lielumu līdz kamēr lietotājs aptur programmu.

2. papildus uzdevums – tiek veikta ievadāmo datu validācija, piemēram, masa nedrīkst būt negatīva.

## Papildus uzdevumi prasmju nostiprināšanai

*Izpilde nav obligāta, bet ir vēlama!*

1. **Redzamā spektra viļņu garums.**  
 Redzamā spektra viļņu garumi variē no 380 līdz 750 nm. Kaut arī spektrs tiek uzskatīts par nepārtrauktu, to pieņemts dalīt sešās krāsās (skat. tabulu). Lūdziet lietotājam ievadīt viļņa garumu. Programmai jāuzraksta, kurai krāsai atbilst ievadītais viļņa garums. Ja ievadītais garums ir ārpus redzamā spektra, programmai tas jāpaziņo.

 | Krāsa    | Viļņa garums (nm)       |
 | -------- | ----------------------- |
 | violets  | $\geq$ 380 un $\lt$ 450 |
 | zils     | $\geq$ 450 un $\lt$ 495 |
 | zaļš     | $\geq$ 495 un $\lt$ 570 |
 | dzeltens | $\geq$ 570 un $\lt$ 590 |
 | oranžs   | $\geq$ 590 un $\lt$ 620 |
 | sarkans  | $\geq$ 620 un $\lt$ 750 |

2. **Palindroms vai nē?**  
 Virkni sauc par palindromu, ja to var vienādi izlasīt no abām pusēm. Piemēram, “anna”, “civic”, “level”, “hannah”. Izveido programmu, kas lūdz lietotājam ievadīt vārdu un ar cikla palīdzību nosaka, vai vārds ir palindroms.

3. **FizzBuzz.** Izveidot programmu “FizzBuzz”, kas definētam skaitlim **N** izvada visus veselos skaitļus līdz **N**, aizstājot tos, kas dalās ar 3 bez atlikuma, ar “Fizz”, tos, kas dalās ar 5, ar “Buzz”, un tos, kas dalās ar 3 un 5, ar “FizzBuzz”.

4. **Reizināšanas tabula.**  
 Izveidot reizināšanas tabulu tā, lai programmas izvada pirmajā rindā būtu skaitļi no 1 līdz 10 sareizināti ar 1, otrajā – ar 2, … , desmitajā – ar 10. Padoms: *Python* komanda `print()` pēc noklusējuma pabeidz teksta izvadi ar pārcelšanu jaunā rindā, `print()` komandai izmantojiet parametru `end=' '`, kas to novērš.

5. **Maksimālā virknes vērtība.**  
 Šī uzdevuma mērķis ir noteikt maksimālo ieraksta vērtību nejaušu skaitļu rindā. Rindai jābūt aizpildītai ar skaitļiem no 1 līdz 100. Pie tam rinda nedrīkst saturēt dublikātus.  
 Padomājiet, kā jūs šo uzdevumu risinātu uz papīra? Lielākā daļa cilvēku salīdzinātu katru rindas locekli ar pārējiem, lai atrastu lielāko. Kā liekas, cik reizes var atjaunoties lielākā vērtība?  
 Uz visiem šiem jautājumiem var atbildēt ar varbūtību teorijas palīdzību.  
 Sākumā programmai jāizvēlas nejaušs skaitlis no 1 līdz 100. Uzreiz saglabājiet šo skaitli kā maksimālo vērtību. Pēc tam ģenerējiet vēl 99 nejaušu skaitļu tajā pašā diapazonā. Katru ģenerēto skaitli pārbaudiet, vai tas ir maksimālais, un, nepieciešamības gadījumā, pierakstiet jaunu maksimālā skaitļa vērtību. Izvadiet katru ģenerēto skaitli uz ekrāna, pievienojot paziņojumu par “līdera” izmaiņu, ja tas nepieciešams.  
 Pēc visu skaitļu izvades, nepieciešams uzrakstīt maksimālo vērtību, kā arī cik reizes tā tika nomainīta. Pārbaudiet programmu vairākas reizes, vai programma katru reizi sniedz vienādu rezultātu?

 Piemērs:

 ```bash
 30
 74 <== new max
 58
 17
 37
 13
 34
 46
 52
 80 <== new max
 37
 97 <== new max
 45
 55
 73
 …
 Maksimālā vērtība rindā: 100
 Maksimālās vērtības nomaiņas skaits: 5
 ```
