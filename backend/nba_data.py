
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
import pandas as pd

# Find Anthony Edwards
player = players.find_players_by_full_name("Anthony Edwards")[0]

print("Player:", player["full_name"])
print("NBA ID:", player["id"])

# Retrieve game logs from the 2025-26 season
games = playergamelog.PlayerGameLog(
    player_id=player["id"],
    season="2025-26",
    timeout=30
)

df = games.get_data_frames()[0]

# Display recent games
print("\nLast 5 Games:")
print(df[["GAME_DATE", "MATCHUP", "PTS", "REB", "AST"]].head())

# Calculate scoring average
print("\nAverage Points:", round(df["PTS"].mean(), 2))


from pathlib import Path

# Create a folder for exported datasets
data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

# Save Anthony Edwards' game history
output_file = data_folder / "anthony_edwards_2025_26.csv"
df.to_csv(output_file, index=False)

print(f"\nSaved NBA data to: {output_file}")
