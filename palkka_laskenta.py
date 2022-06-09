
import math


def main():
    paivan_palkat = lue_tiedosto()
    selostus = "Syötä (1) jos haluat laskea ansaitun palkan määrän \nSyötä (2) jos haluat kirjata uuden palkan tiedostoon \nSyötä (3) jos haluat poistaa palkat tietyltä aikaväliltä\nSyötä (4) jos haluat nähdä luettelon palkoista\nSyötä (5) jos haluat lopettaa ohjelman suorittamisen\n"
    try:
        syoto = int(input(selostus))
    except ValueError:
        print("Virheellinen syöttö \n")
        main()

    if int(syoto) == 1:
        laske_palkka(paivan_palkat)
    elif int(syoto) == 2:
        kirjaa_uusi_palkka()
    elif int(syoto) == 4:
        pass
    else:
        print("Virheellinen syöttö \n")
        main()
    # Loppu




def kirjaa_uusi_palkka():
    syoto = "e"
    while syoto != "k":
        syoto = input("Kirjoita palkka ja päiväys\n")
        tiedosto =  open("palkka_lista.txt", "a")
        tiedosto.write(syoto)
        tiedosto.write("\n")
        tiedosto.close()
        syoto = input("Lopeta palkkojen syöttö syöttämällä 'k'\n")
    main()




def lue_tiedosto():
    paiva_palkat = {}
    tiedosto = open("palkka_lista.txt", "r")
    for rivi in tiedosto:
        try:
            tieto_rivi = rivi.rstrip()
            osat = tieto_rivi.split(",")
            try:
             paiva_palkat[osat[1]] = osat[0]
            except IndexError:
                pass
        except OSError:
            pass
    return paiva_palkat


def laske_palkka(palkat):
    summa = 0
    palkka_lista = palkat.values()
    for i in palkka_lista:
        summa += float(i)
    print("Yhteenlaskettu palkkasi on",summa,"€\nKirjoita 'k' jos haluat  ansaitun palkan vaikutukset sijoituksillesi")
    syoto = input()
    if syoto == "k":
        palkka_sijoitus(summa)
    else:
        main()

def muokkaa_lukua(luku):
    luku = str(int(luku))
    if len(luku) > 3:
        loppu = luku[len(luku)-3:len(luku)]
        alku = luku[:len(luku)-3]
    elif len(luku) > 6:
        loppu = luku[len(luku)-6:len(luku)]
        alku = luku[:len(luku)-6]
    elif len(luku) > 9:
        loppu = luku[len(luku)-9:len(luku)]
        alku = luku[:len(luku)-9]
    else:
        return luku
    return alku + " " + loppu


def palkka_sijoitus(palkka_summa):
    syoto = input("Syötä sijoitustilin rahamäärä (€) sekä odotettu vuotuinen kasvu (%) pilkulla erotettuna\nesim. '18000,10'\n")
    lista = syoto.split(",")
    tili_maara = float(lista[0])
    sijoitus_ilman_palkkaa = tili_maara
    palkallinen_sijoitus = tili_maara + palkka_summa
    kasvu = float(lista[1]) / 100 + 1
    print('-' * 40)
    vali = " "*9
    for i in range(20):
        palkaton_tuotto = sijoitus_ilman_palkkaa * kasvu**i
        palkallinen_tuotto = palkallinen_sijoitus * kasvu**i
        erotus = palkallinen_tuotto - palkaton_tuotto

# Seuraavaksi muokataan tulostettavia lukuja nätimmiksi
        palkaton_tuotto_tulostus =muokkaa_lukua(palkaton_tuotto)
        palkallinen_tuotto_tulostus = muokkaa_lukua(palkallinen_tuotto)
        erotus_tulostus = muokkaa_lukua(erotus)

        print (f"| {palkaton_tuotto_tulostus:<10}| {palkallinen_tuotto_tulostus:<10}|{erotus_tulostus:<10}|")
        print('-'*40)

    syoto = input("Syötä 'k' jos kiinnostaa nähdä rahan vuotuisen kasvun muutoksen\n")
    if syoto != 'k':
        main()
    else:
        print('-' * 40)
    for i in range(20):
        palkaton_tuotto = sijoitus_ilman_palkkaa * math.e**(math.log(kasvu)*i)*math.log(kasvu)
        palkallinen_tuotto = palkallinen_sijoitus * math.e**(math.log(kasvu)*i)*math.log(kasvu)
        erotus = palkallinen_tuotto - palkaton_tuotto

        #Muutu nätimmäksi!
        palkaton_tuotto_tulostus =muokkaa_lukua(palkaton_tuotto)
        palkallinen_tuotto_tulostus = muokkaa_lukua(palkallinen_tuotto)
        erotus_tulostus = muokkaa_lukua(erotus)
        print (f"| {palkaton_tuotto:>10} | {palkallinen_tuotto:>10} | {erotus:>10}")
        print('-'*40)
    main()


main()