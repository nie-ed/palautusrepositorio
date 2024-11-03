import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_konstruktori_hakee_tiedot(self):
        #luodaan funktion sisäinen pelaajat lista
        player_reader = PlayerReaderStub()
        players = player_reader.get_players()

        #verrataan jokaisen pelaajan tietoja StatisticsService pelaajan tietoihin
        for i in range(len(players)):
            self.assertEqual(players[i].name, self.stats._players[i].name)
            self.assertEqual(players[i].team, self.stats._players[i].team)
            self.assertEqual(players[i].goals, self.stats._players[i].goals)
            self.assertEqual(players[i].assists, self.stats._players[i].assists)


    def test_loytaa_pelaajan_listalta(self):
        #luodaan pelaaja joka tiedetään olevan myös listalla
        player = Player("Kurri",   "EDM", 37, 53)        
        name = "Kurri"
        #etsitään pelaajan nimellä lsitalta
        search_player = self.stats.search(name)
        #verrataan onko palautetun pelaajan tiedot samat kuin luodumme pelaajan tiedot
        self.assertEqual(player.name, search_player.name)
        self.assertEqual(player.team, search_player.team)
        self.assertEqual(player.goals, search_player.goals)
        self.assertEqual(player.assists, search_player.assists)

    def test_ei_loyda_pelaajaa_listalta(self):
        name = "Pekka"
        #etsitään pelaajaa joka ei ole listalle
        search_player = self.stats.search(name)
        #pelaajaa ei ole listalla, eli pitäisi palauttaa None
        self.assertEqual(search_player, None)

    def test_etsi_tietyn_tiimin_pelaajat(self):
        #tiimin EDM pelaajien nimet
        EDM_players = ["Semenko", "Kurri", "Gretzky"]
        #tiimin EDM pelaajien lista
        players_from_list = self.stats.team("EDM")
        #verrataan nimiä
        for i in range(3):
            self.assertEqual(EDM_players[i], players_from_list[i].name)

    def test_palauttaa_pelaajat_pisteiden_perusteella(self):
        PR = PlayerReaderStub() #luodaan PlayerReaderStub olio
        pelaajat = PR.get_players() #haetaan pelaajat
        #järjestetään pistejärjestykseen
        järjestetyt = sorted(pelaajat, reverse=True, key=lambda player: player.points)
        
        #rajataan, montako pelaajaa halutaan näyttää
        järjestetyt_listana= []
        for i in range(3):
            järjestetyt_listana.append(järjestetyt[i])
        
        #haetaan statistics_servicen kautta pelaajat pistejärjestyksessä
        haetut= self.stats.top(3, SortBy.POINTS)

        #verrataan
        for i in range(3):
            self.assertEqual(haetut[i].name, järjestetyt_listana[i].name)
            self.assertEqual(haetut[i].team, järjestetyt_listana[i].team)
            self.assertEqual(haetut[i].goals, järjestetyt_listana[i].goals)
            self.assertEqual(haetut[i].assists, järjestetyt_listana[i].assists)

    def test_palauttaa_pelaajat_assistien_perusteella(self):
        PR = PlayerReaderStub() #luodaan PlayerReaderStub olio
        pelaajat = PR.get_players() #haetaan pelaajat
        #järjestetään assists järjestykseen
        järjestetyt = sorted(pelaajat, reverse=True, key=lambda player: player.assists)
        
        #rajataan, montako pelaajaa halutaan näyttää
        järjestetyt_listana= []
        for i in range(3):
            järjestetyt_listana.append(järjestetyt[i])
        
        #haetaan statistics_servicen kautta pelaajat assists järjestyksessä
        haetut= self.stats.top(3, SortBy.ASSISTS)

        #verrataan
        for i in range(3):
            self.assertEqual(haetut[i].name, järjestetyt_listana[i].name)
            self.assertEqual(haetut[i].team, järjestetyt_listana[i].team)
            self.assertEqual(haetut[i].goals, järjestetyt_listana[i].goals)
            self.assertEqual(haetut[i].assists, järjestetyt_listana[i].assists)
   
    def test_palauttaa_pelaajat_goalsien_perusteella(self):
        PR = PlayerReaderStub() #luodaan PlayerReaderStub olio
        pelaajat = PR.get_players() #haetaan pelaajat
        #järjestetään goalsien järjestykseen
        järjestetyt = sorted(pelaajat, reverse=True, key=lambda player: player.goals)
        
        #rajataan, montako pelaajaa halutaan näyttää
        järjestetyt_listana= []
        for i in range(3):
            järjestetyt_listana.append(järjestetyt[i])
        
        #haetaan statistics_servicen kautta pelaajat goals järjestyksessä
        haetut= self.stats.top(3, SortBy.GOALS)

        #verrataan
        for i in range(3):
            self.assertEqual(haetut[i].name, järjestetyt_listana[i].name)
            self.assertEqual(haetut[i].team, järjestetyt_listana[i].team)
            self.assertEqual(haetut[i].goals, järjestetyt_listana[i].goals)
            self.assertEqual(haetut[i].assists, järjestetyt_listana[i].assists)

    def test_jos_ei_ole_sort_by_annettu_palautetaan_pisteiden_perusteella(self):
        PR = PlayerReaderStub() #luodaan PlayerReaderStub olio
        pelaajat = PR.get_players() #haetaan pelaajat
        #järjestetään pistejärjestykseen
        järjestetyt = sorted(pelaajat, reverse=True, key=lambda player: player.points)
        
        #rajataan, montako pelaajaa halutaan näyttää
        järjestetyt_listana= []
        for i in range(3):
            järjestetyt_listana.append(järjestetyt[i])
        
        #haetaan statistics_servicen kautta pelaajat pistejärjestyksessä
        haetut= self.stats.top(3)

        #verrataan
        for i in range(3):
            self.assertEqual(haetut[i].name, järjestetyt_listana[i].name)
            self.assertEqual(haetut[i].team, järjestetyt_listana[i].team)
            self.assertEqual(haetut[i].goals, järjestetyt_listana[i].goals)
            self.assertEqual(haetut[i].assists, järjestetyt_listana[i].assists)

            





