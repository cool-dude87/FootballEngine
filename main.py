import pandas as pd

#==================================
# DATA ONE SEASON
#==================================

data = pd.read_csv("E0_223.csv")

#==================================
# DINSPECT THE DATA ESPECIALLY COLUMNS 
#==================================

# print(data.head())
# print(data.shape)
# print(data.columns.tolist())

#==================================
# include only the useful columns we need
#==================================

football_data = data[
    [
        "Date",
        "HomeTeam",
        "AwayTeam",
        "FTHG",     # full-time home goals    
        "FTAG",     # full-time away goals
        "FTR",      # full-time result
        "HS",       # Home shots
        "AS",       # Away shots
        "HST",      # on target
        "AST",
        "HC",       # Home Corners
        "AC"        # Away corners
    ]
].copy()

# print(football_data.head())
# print(football_data.dtypes)

#==================================
# idate is a str atm we need to change this to pandas  date time
#==================================

football_data["Date"] = pd.to_datetime(
    football_data["Date"],
    format="%d/%m/%Y"
)

football_data = football_data.sort_values("Date")

# How many of each column is NA? --> this case none...
# print(football_data.isna().sum())

"""
Now for team level data, such as choosing a team and being able to extract 
each match containing that team
"""

team = "Arsenal"

#==================================
# data frame containing only columns of teams with that team
#==================================

team_games = football_data[
    (football_data["HomeTeam"] == team) | 
    (football_data["AwayTeam"] == team)
].copy()

#==================================
# create new column describing if chosen team was home or away
#==================================

team_games["Home_Away"] = "Home"

team_games.loc[
    team_games["AwayTeam"] == team,
    "Home_Away"
] = "Away"

#==================================
# Create opponent column 
#==================================

team_games["Opponent"] = team_games["AwayTeam"]

team_games.loc[
    team_games["Home_Away"] == "Away",
    "Opponent"
] = team_games["HomeTeam"]

#==================================
# Creating goals for and goals against columns 
#==================================

team_games["scored"] = team_games["FTHG"]

team_games.loc[
    team_games["Home_Away"] == "Away",
    "scored"    
] = team_games["FTAG"]

team_games["conceded"] = team_games["FTAG"]

team_games.loc[
    team_games["Home_Away"] == "Away",
    "conceded"    
] = team_games["FTHG"]

#==================================
# Shots for and shots against columns  
#==================================

team_games["shots_for"] = team_games["HS"]

team_games.loc[
    team_games["Home_Away"] == "Away",
    "shots_for"
] = team_games["AS"]

team_games["shots_against"] = team_games["AS"]

team_games.loc[
    team_games["Home_Away"] == "Away",
    "shots_against"
] = team_games["HS"]

#==================================
# shots on target and corners 
#==================================

team_games["sot_for"] = team_games["HST"]

team_games.loc[
    team_games["Home_Away"] == "Away",
    "sot_for"
] = team_games["AST"]

team_games["sot_against"] = team_games["AST"]

team_games.loc[
    team_games["Home_Away"] == "Away",
    "sot_against"
] = team_games["HST"]

team_games["corners_for"] = team_games["HC"]

team_games.loc[
    team_games["Home_Away"] == "Away",
    "corners_for"
] = team_games["AC"]

team_games["corners_against"] = team_games["AC"]

team_games.loc[
    team_games["Home_Away"] == "Away",
    "corners_against"
] = team_games["HC"]

#==================================
# Cleaner view of the table 
#==================================

team_view = team_games[
    [
     "Date",
     "Opponent",
     "Home_Away",
     "scored",
     "conceded",
     "shots_for",
     "shots_against",
     "sot_for",
     "sot_against",
     "corners_for",
     "corners_against"
    ]
].copy()

"""
ADDED FIRST FUNCTION USING THIS TO FUNCTIONS.PY
"""
#==================================
# Getting to the point where we can access the last n matches wth given date
#==================================

# it was easier to construct using a function so below is the function created FIRSTLY in functions.py

# def previous(n, data, team_name, date=None):
#     if date is None:
#         date = data["Date"].max() + pd.Timedelta(days=1)

#     team_stats = team_view(data, team_name)
#     team_stats = team_stats.reset_index(drop=True)

#     previous_games = team_stats[
#         team_stats["Date"] < date
#     ]

#     previous_games = previous_games.sort_values("Date", ascending=False)

#     previous_games = previous_games.iloc[0:n].copy()

#     return previous_games

