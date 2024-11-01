import unittest
from statistics_service import StatisticsService
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


