# 12. nodarbība. Datu ievade un izvade

## 1. uzdevums. Failu izveide, datu apstrāde, filtrēšana un ziņojumu izveide

**Uzdevums**: izveidot _Python_ kodu, kas ģenerē nejaušus `.txt` failus ar skaitļiem, apstrādā šos failus, aprēķinot statistiskos datus (vidējo vērtību, standartnovirzi, minimālo un maksimālo vērtību) un atlasot vērtības noteiktā diapazonā, kā arī ģenerē kopsavilkuma ziņojumu.

Programmas soļi:

1. Failu ģenerēšana: Izveidot noteiktā direktorijā `.txt` failus ar nejaušiem skaitļiem, kas simulē reālu datu kopu.
2. Statistiskie aprēķini: Apstrādāt katru failu, aprēķinot tajā esošo skaitļu vidējo vērtību, standartnovirzi, minimālo un maksimālo vērtību.
3. Datu filtrēšana: Atlasīt tikai noteiktā diapazonā esošās vērtības un saglabāt tās vienā failā, norādot, no kura sākotnējā faila tās ir iegūtas.
4. Ziņojuma izveide: Saglabāt visu apkopoto informāciju (statistiku un filtrētos datus) kopsavilkuma failā.

## 2. uzdevums. Dažadu lampu spektru analīze

**Uzdevums**:

1. Ielasiet visus trīs dotos spektrus (tos iespējams lejupielādēt zem uzdevuma). Tie ir LED, kvēlspuldzes un dienasgaismas lampas spektri.
2. Normalizējiet katru spektru, izmantjot to maksimālās vērtības.
3. Attēlojiet spektrus kā melnas līnijas trīs apakšgrafikos ar vienu  $(x)$ asi, nodrošinot, ka starp apakšgrafikiem nav vertikālu atstarpju.
4. Intensitātes asij iestati diapazonu no 0 līdz 1.1 un viļņu garumu asij diapazonu no 480 nm līdz 710 nm.
5. Apzīmējiet kopīgo x asi $\lambda/\mathrm{nm}$.
6. Noņemiet datu punktus un apzīmējumus no visām vertikālajām asīm.
7. Pievienojiet anotācijas (nevis paskaidrojumus / _legends_) (a), (b) un (c) katra apakšgrafika augšējā labajā stūrī.
8. Izmainiet visu anotāciju, apzīmējumu u.tml. fontu uz _Times New Roman_ (vai jebkuru citu fontu), iestatot izmēru 9pt.
9. Eksportējiet grafiku kā `spektri.pdf`, iestatot tā platumu uz 16 pc un attēla attiecību (_aspect ratio_) 1. Nododiet saglabāto spektru atbilstošajā testa uzdevumā.
10. Pirmajā spektrā nosakiet izteiktākos pīķus. Izmantojiet funkciju `scipy.signal.find_peaks()` ar parametru `prominence=0.2`.
11. Visus atrastos pīķus apvelciet ar sarkaniem apļiem.

_Papildus uzdevums: Vai varat atpazīt kurš spektrs atbilst kurai lampai? Ierakstiet testa atbildes logā!_

Datnes: [1.spektrs](https://estudijas.lu.lv/draftfile.php/1176695/user/draft/812323098/spektrs1.asc) ; [2.spektrs](https://estudijas.lu.lv/draftfile.php/1176695/user/draft/812323098/spektrs2.asc) ; [3.spektrs](https://estudijas.lu.lv/draftfile.php/1176695/user/draft/812323098/spektrs3.asc) .

Koda fragments (drīkst neizmantot):

```python
import numpy as np
from matplotlib import pyplot as plt
for faila_nosaukums in ("spektrs1.asc", "spektrs2.asc", "spektrs3.asc"):
    spektrs = np.loadtxt(faila_nosaukums, delimiter='\t', skiprows=33)
    nm = spektrs[:, 0]
    intens = spektrs[:, 1]
    plt.plot(nm, intens, label=faila_nosaukums)
plt.legend()
plt.xlabel('λ (nm)')
plt.ylabel('I (s⁻¹)')
plt.show()
```

## 3. uzdevums. XANES datu vizualizācija

**Uzdevums**:

1. Datu nolasīšana un saglabāšana: no `CTS_Test.h5` faila (saite lejupielādei atrodas zem uzdevuma teksta) automātiski nolasīt norādītas rindas (`/entry8xxx`), izmantojot `h5py` bibliotēku.
2. Datu apstrāde:
    * atlasīt trīs mērījumu kanālus: `aem_27_ch01`, `aem_27_ch02`, un `pcap_energy_avg`;
    * aprēķināt datu attiecību starp kanālu `ch01` un `ch02`;
    * saglabāt rezultātus `*.csv` failā.

**NB!** Nepieciešams nodrošināt, ka, ja kādā ierakstā trūkst kāds kanāls, dati tiek izlaisti un apstrāde turpinās ar nākamo ierakstu.

1. Datu vizualizācija: ielasīt datus no iegūtā `*.csv` faila (piemēram, `CTS_TiO2-8815.csv`) un izveidot grafiku, izmantojot `matplotlib`bibliotēku:
    * izmantot `pcap_energy_avg` kā x-asi un `ch01 / ch02` kā y-asi;
    * grafikam piešķirt nosaukumu 'Ti L_{2,3}$ edge ($TiO_{2}$ SolGel)', x-asij 'Energy, eV' un y asij 'Normalized intensity, a.u.';
    * saglabāt grafiku kā `XANES.pdf` un nodod testa atbilstošajā uzdevumā.

Saite uz datiem: [testa datne](https://estudijas.lu.lv/draftfile.php/1176695/user/draft/355914573/CTS_Test.h5).
