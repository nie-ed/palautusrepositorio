KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self.tarkistus(kapasiteetti, KAPASITEETTI, "Väärä kapasiteetti")
        self.kasvatuskoko = self.tarkistus(kasvatuskoko, OLETUSKASVATUS, "kapasiteetti2")

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def tarkistus(self, koko, oletusarvo, exeption):
        if koko is None:
            return oletusarvo
        elif not isinstance(koko, int) or koko < 0:
            raise Exception(exeption)
        else:
            return koko


    def kuuluu(self, n):
        if n in self.ljono:
            return True
        return False


    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True


        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm - len(self.ljono) == 0:
                lista_vanha = self.ljono.copy()
                self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(lista_vanha, self.ljono)

            return True

        return False

    def poista(self, n):
        if n in self.ljono:
            self.ljono.remove(n)
            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        uusi_lista = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(uusi_lista)):
            uusi_lista[i] = self.ljono[i]

        return uusi_lista
        
    def yhdiste(a, b):
        uusi_olio, a_lista, b_lista = alustus(a, b)
        kay_lista_lapi(uusi_olio.lisaa, a_lista)
        kay_lista_lapi(uusi_olio.lisaa, b_lista)

        return uusi_olio
        
    def leikkaus(a, b):
        uusi_olio, a_lista, b_lista = alustus(a, b)

        for i in range(0, len(a_lista)):
            for j in range(0, len(b_lista)):
                if a_lista[i] == b_lista[j]:
                    uusi_olio.lisaa(b_lista[j])

        return uusi_olio
        
    def erotus(a, b):
        uusi_olio, a_lista, b_lista = alustus(a, b)

        kay_lista_lapi(uusi_olio.lisaa, a_lista)
        kay_lista_lapi(uusi_olio.poista, b_lista)

        return uusi_olio

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:        
            listataan_str = str(self.ljono[0])
            for i in range(1, self.alkioiden_lkm):
                listataan_str += ", " + str(self.ljono[i])
            return "{" + listataan_str + "}"



def alustus(a, b):
    uusi_olio = IntJoukko()
    a_lista = a.to_int_list()
    b_lista = b.to_int_list()
    return uusi_olio, a_lista, b_lista


def kay_lista_lapi(uuden_olion_metodi, lista):
    for i in range (0, len(lista)):
        uuden_olion_metodi(lista[i])


