import pandas as pd
from sqlalchemy import create_engine


#create engine to read SQL database

engine = create_engine("postgresql:///soccer")


#create dataframe using all the player data from the FIFA 19 SQL database

df = pd.read_sql_query("SELECT * FROM fifa_19;", engine)


#save all player data as .csv file for exploration

df.to_csv("write_data/all_players.csv")  


#Save all players data frame as seperate, stand alone pandas data frame

pd.read_csv('../write_date/all_players.csv')