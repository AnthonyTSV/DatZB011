# 4. nodarbība. Datu struktūras

## Uzdevumi par sarakstiem

### Mērķis: apgūt sarakstu izmantošanu

1. Uzrakstiet programmu, kas pieprasa lietotājam ievadīt veselus skaitļus un saglabā tos saraksta veidā. Ievades beigu indikators ir **0**. Kad ievade pabeigta, programmai jāizvada uz ekrāna skaitļus augošā secībā (izņemot 0). Datu kārtošanai izmantojiet metodi `sort` vai funkciju `sorted`.
*Papildus nosacījums – kods nedrīkst būt garāks par 10 rindām.*

1. Izveidojiet programmu, kas lūdz lietotājam ievadīt vārdus un saglabā tos saraksta veidā. Pēc tam uz ekrāna jāattēlo lietotāja ievadītos vārdus bez atkārtojumiem, piemēram, ja lietotājs ievadījis: `first, second, first, third, second`, programmai jāizvada: `first, second, third`.
*Papildus nosacījums – kods nedrīkst būt garāks par 10 rindām.*

1. Nejauši loterijas numuri. Galvenās balvas iegūšanai nepieciešams, lai seši skaitļi uz loterijas biļetes sakristu ar sešiem nejaušiem skaitļiem diapazonā no 1 līdz 49, kas izkrīt izlozes laikā. Uzrakstiet programmu, kas atlasa sešus nejaušus skaitļus biļetei. Pārliecinieties, ka šo skaitļu starpā nav dublikātu. Izvadiet skaitļus augošā secībā uz ekrāna.
*Papildus nosacījums – kods nedrīkst būt garāks par 5 rindām.*

## Uzdevumi par vārdnīcām

### Mērķis: apgūt vārdnīcu izmantošanu

1. Uzrakstiet programmu, kas nosaka un izvada, cik unikālu simbolu satur ievadītā virkne. Piemēram, virknei `Hello World!` ir 9 unikāli simboli, bet virknei `zzz` – viens. Izmantojiet vārdnīcu, lai atrisinātu šo uzdevumu.  
*Papildus nosacījums – kods nedrīkst būt garāks par 10 rindām.*

2. **Anagrammas**. Par anagrammām sauc tādus vārdus, kuri veidojas, pārvietojot burtus. Piemēram, vārdi `live` un `evil` ir anagramma. Uzrakstiet programmu, kas pieprasa lietotājam ievadīt vārdus un noteiks, vai tie ir anagrammas vai nav, uz ekrāna izvadot paziņojumu.  
*Papildus nosacījums – kods nedrīkst būt garāks par 10 rindām.*

3. **Scrabble.** Šajā spēlē katram burtam atbilst noteikts punktu skaits. Kopējais spēlētāja punktu skaits ir visu vārda burtu punktu kopsummā. Jo biežāk burts sastopams valodā, jo mazāks punktu skaits tiek piešķirts tam. Tabulā ir parādīts, cik punktu tiek piešķirts par burtiem angļu spēles versijā. Izveidojiet programmu, kas saskaita un atspoguļo iegūto punktu skaitu par vārdu. Izveidojiet vārdnīcu, kas glabā punktu un burtu vērtības. Izmantojiet to savos aprēķinos.  
*Papildus nosacījums – kods nedrīkst būt garāks par 18 rindām.*

| Points | Letters                      |
| ------ | ---------------------------- |
| 1      | A, E, I, L, N, O, R, S, T, U |
| 2      | D, G                         |
| 3      | B, C, M, P                   |
| 4      | F, H, V, W, Y                |
| 5      | K                            |
| 8      | J, X                         |
| 10     | Q, Z                         |

4. Izveidojiet programmu, kas pārvērš un izvada lietotāja ievadīto frāzi Morzes kodā. Koda uzglabāšanai nepieciešams izmantot vārdnīcu. Morzes kodu var atrast internetā.

## Papildus uzdevumi prasmju nostiprināšanai

*Izpilde nav obligāta, bet ir vēlama!*

1. Izveidot programmu, kas apvieno sarakstu ar teksta tipa elementiem (vārdiem) par vienu garu teksta mainīgo (teikumu). Piemēram, saraksts `["Mani", "sauc", "Aleksandrs"]` tiktu saglabāts programmas atmiņā kā mainīgais ar saturu `Mani sauc Aleksandrs`.

2. Programmā definēt sarakstu, kas satur gan skaitliska tipa elementus, gan teksta tipa elementus. Izveidot programmu, kas mēģina katru saraksta elementu izvadīt uz ekrāna, attēlotu ar lielajiem burtiem (`teksta_mainigais.upper()`). Ja tas neizdodas, uz ekrāna izvadīt tekstu `Neizdevās attēlot ar lielajiem burtiem`.

3. Izveidot vārdnīcas tipa datu struktūru `galvaspilsetas`, kurā definētas piecas valstis un tām atbilstošās galvaspilsētas. Pārbaudīt funkcionalitāti, veidojot datu šķēlumu, izmantojot valsts nosaukumu. Piemēram, ja pieprasa `galvaspilsetas['Lietuva']` tiek atgriezts `'Viļņa'`.

4. Izveidot programmu, kurā ir definēti trīs saraksti, kas satur teksta tipa mainīgos: Divi saraksti ar īpašības vārdiem (`["Milzīgs", "Neliels", ...]`, `["Zaļš", "Zils", ...]`), viens ar lietvārdiem (`["Zilonis", ...]`). Programma sastāda savā atmiņā sarakstu, kas satur visus iespējamos teikumus, kas var tikt kombinēti no šiem vārdiem (`["Milzīgs zaļš zilonis", "Neliels zaļš zilonis", ...]`).

5. Izveidot programmu, kura sarakstam ar astronautu vārdiem un amatiem veic apkopojumu par konkrēta amata darītāju skaitu un saglabā to atmiņā kā vārdnīcu. Piemēram, sarakstam `[{'vārds':'Jānis', 'amats':'tehniķis'}, {'vārds':'Elza', 'amats':'kapteinis'}, {'vārds':'Alise', 'amats':'tehniķis'}]` tiktu izveidota vārdnīca `{'tehniķis':2, 'kapteinis':1}`. Programmai pašai jāmāk uzskaitīt visus amatus un saskaitīt darbiniekus tajos.
