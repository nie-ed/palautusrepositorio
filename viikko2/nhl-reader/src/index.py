from player_reader import PlayerReader
from player_stats import PlayerStats
from rich import print
from rich.panel import Panel
from rich.table import Table

def main():
    print("[italic]NHL statistics by nationality\n[/italic]")
    print("Select season [bold magenta1][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/][/bold magenta1]:")
    season = input()
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)  
    
    while True:
        print("Select nationality\n [bold magenta1][AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR/][/bold magenta1]: ")
        nationality = input()
        players = stats.top_scorers_by_nationality(nationality)

        table =  Table(title=f"Top scorers of {nationality} season {season}")
        table.add_column("name", style="cyan", no_wrap=True)
        table.add_column("team", style="magenta")
        table.add_column("goals", style="green")
        table.add_column("assists", style="green")
        table.add_column("points", style="green")

        for player in players:
            points = player.goals + player.assists
            table.add_row(str(player.name), str(player.team), str(player.goals), str(player.assists), str(points))

        print(table)

if __name__ == "__main__":
    main()
