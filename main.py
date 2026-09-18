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
]

#==================================
# create new column describing if chosen team was home or away
#==================================

team_games["Home_Away"] = "Home"

print(team_games.head())



