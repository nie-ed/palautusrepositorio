from kauppa import Kauppa
from kirjanpito import kirjanpito
from varasto import varasto
from pankki import pankki
from viitegeneraattori import viitegeneraattori

# 1 täg muutos
# 2 täg muutos
# 3 täg muutos

def main():
    # käytetään valmiiksi luotuja "oletusarvoisia" varasto-, pankki- ja viitegeneraattoriolioita
    kauppa = Kauppa(varasto, pankki, viitegeneraattori)

    # kauppa hoitaa yhden asiakkaan kerrallaan seuraavaan tapaan:
    kauppa.aloita_asiointi()
    kauppa.lisaa_koriin(1)
    kauppa.lisaa_koriin(3)
    kauppa.lisaa_koriin(3)
    kauppa.poista_korista(1)
    kauppa.tilimaksu("Pekka Mikkola", "1234-12345")

    # seuraava asiakas
    kauppa.aloita_asiointi()

    for _ in range(0, 24):
        kauppa.lisaa_koriin(5)

    kauppa.tilimaksu("Arto Vihavainen", "3425-1652")

    # kirjanpito
    for tapahtuma in kirjanpito.tapahtumat:
        print(tapahtuma)


if __name__ == "__main__":
    main()
