import pandas as pd
import functions as fnc

# load up my data
data = pd.read_csv("E0_223.csv")

#clean said data
football_data = fnc.data_setup(data)

# generate key stats
arsenal_stats = fnc.team_view(football_data,"Arsenal")

print(arsenal_stats.head())

# grabbing first 5 games before date for chelsea 

chelsea_games = fnc.previous(5, football_data, "Chelsea", "12/03/2023")

print(chelsea_games.head())

# couple more testers

test1 = fnc.previous(5, football_data, "Arsenal")

test2 = fnc.previous(
    5,
    football_data,
    "Chelsea",
    "01/01/2023"
)

test3 = fnc.previous(
    10,
    football_data,
    "Liverpool",
    "01/10/2022"
)

test4 = fnc.previous(
    10,
    football_data,
    "Arsenal",
    "15/08/2022"
)

print(test1)
print(test2)
print(test3)
print(test4)

