# 6. nedēļas starprezultāts

> [!WARNING]
> Lai literatūras sarksts strādātu, ir jāpievieno `ref.bib` fails!

```latex
\documentclass{article}

\author{Antons Cvečkovskis}
\title{Viskozitātes noteikšana šķidrumos un gāzēs}

\usepackage{graphicx}
\usepackage{csquotes} % Lai nebūtu Package biblatex Warning: 'babel/polyglossia' detected but 'csquotes' missing. Loading 'csquotes' recommended.
\usepackage{biblatex}
\usepackage[latvian]{babel}

\addbibresource{ref.bib}

\begin{document}

\maketitle

\section{Ievads}

Šķidrumiem un gāzēm piemīt viskozitāte, kad šķidruma vai gāzes slāņi nav relatīvā miera stāvoklī viens pret otru. Slāņi iedarbojas viens uz otru. Starp slāņiem parādās miejiedarbības spēks -- berzes spēks. Šo berzi sauc par iekšējo berzi. Iekšējā berze (viskozitāte) šķidrumos un gāzēs pastāv tādēļ, ka notiek molekulu pāreja starp slāņiem, kas pārvietojas ar dažādiem ātrumiem. Molekulas, pārejot no ātrākiem slāņiem uz lēnākiem slāņiem, paātrina lēnākos slāņus un tie sāk pārvietoties ātrāk. Ja molekulas no lēnākiem slāņiem nonāk ātrākos slāņos, bremzē tos, skat. att.~....

Vielā parasti nav tādu norobežotu slāņu, kuros ir viens noteikts ātrums, bet ātrums slānī nepārtraukti mainās. Ātruma raksturošanai ievieš ātruma gradientu 

Ja attālums starp diviem slāņiem ir ... un otrā slāņa ātrums attiecībā pret pirmo slāni ir ..., tad, pieņemot, ka ātrums mainās lineāri atkarībā no attāluma, ātruma gradients ir 

Slāņu iekšējās berzes spēks ... ir atkarīgs no slāņu, starp kuriem pastāv berze, saskares virsmas laukuma ... un ātruma gradienta:

kur ... ir proporcionalitātes koeficients, ko sauc par iekšējās berzes jeb viskozitātes koeficientu. Sakarību ... sauc par Furjē formulu.

\section{Laminārā un turbulenta plūsma}

Pētot lamināru plūsmu caur kapilāru Hāgens 1839.g. \cite{Hagen1839} un Puazeils (Poiseuille) 1840.g. \cite{SuteraSkalak2003} eksperimentāli atklāja, ka laminārā šķidruma vai gāzes plūsmā laika vienībā caur kapilāra šķērsgriezuma laukumu izplūdušā šķidruma vai gāzes tilpumu ... nosaka sakarība:

kur ... ir kapilāra rādiuss, ... ir kapilāra garums, ... ir spiediena starpība starp kapilāra galiem, un ... ir viskozitātes koeficients: 


Lamināru šķidrumu vai gāzes plūsmu caurulēs raksturo Reinoldsa skaitlis:

kur ... -- šķidruma vai gāzes blīvums, ... -- caurules diametrs, ... -- šķidruma vai gāzes plūsmas ātrums, ... -- šķidruma vai gāzes viskozitātes koeficients.

Lai plūsma būtu lamināra, reinoldsa skaitlim jābūt mazākam par 2000 \cite{Rhodes2008}. Laika vienībā caur kapilāru izplūdušā šķidruma (gāzes) tilpums ... un kapilāra šķērsgriezuma laukums ... , no šīm abām izteiksmēm izsaka plūsmas ātrumu:


No izteiksmēm ... un ... iegūst:

\section{Stoksa likums}

Kustoties šķidrumā cietam ķermenim, tas viskozitātes dēļ aizrauj līdzi tam pieguļošos šķidruma slāņus, tāpēc šķidrums izrāda pretestību ķermeņa kustībai. Pretestības spēks ir atkarīgs no vides, ķermeņa kustības ātruma, tā izmēriem un formas. Mazu kustības ātrumu gadījumā pretestības spēks ir proporcionāls ķermeņa kustības ātrumam. Stokss konstatēja, ka sfēriskas formas ķermeņiem, kas kustas ar nelielu ātrumu, šķidruma pretestības spēks ... ir proporcionāls ķermeņa kustības ātrumam ... un lodes rādiusam ...:

kur ... -- viskozitātes koeficients.
Sakarību ... sauc par Stoksa likumu \cite{Stokes1851}. 

Uz lodi, kuras masa ... un rādiuss ..., kas krīt ar ātrumu ... šķidrumā, kura viskozitātes koeficients ir ..., darbojas 3 spēki (skat. ... att.). Šie spēki ar laiku līdzsvarojas.

Lodes smaguma spēks ir

kur ... -- lodes rādiuss, ... -- lodes masa, ... -- brīvās krišanas paātrinājums, ... -- lodes blīvums un ... -- šķidruma blīvums.

Ievietojot izteiksmē ... izteiksmes ... un ... , iegūst

no kurienes seko:

kur ... -- lodes diametrs un ... -- lodes veiktais ceļš laikā ... .

Izteiksme ... ir izmantojama tikai tad, ja vide, kurā kustās lode, ir neierobežota (bez sienām) un lode kustības laikā nedeformējas. Praksē šķidrums ir iepildīts cilindriskas formas traukā, kura diametrs ir ... . Lode krīt pa cilindra asi. Vienādojumu nepieciešams koriģēt:


\printbibliography

\end{document}

```
