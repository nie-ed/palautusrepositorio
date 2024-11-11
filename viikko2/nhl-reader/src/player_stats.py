class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nat):
        players = self.reader.get_players()
        players.sort(key=lambda x: x.goals+x.assists, reverse=True)
        nat_players = filter(lambda a: (a.nat ==nat), players)
        return nat_players

