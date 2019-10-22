# load necessary modules ----
import pandas as pd
import numpy as np
import sys
from IPython.core import ultratb
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# ensure error messages are color coded using IPython color schema ----
sys.excepthook = ultratb.FormattedTB(mode="Verbose",
                                     color_scheme="Linux",
                                     call_pdb=False)

# load necessary data ----
fifa_df = pd.read_csv("write_data/all_players.csv")

# store relevant columns ----
relevant_columns = ['pace',
        'acceleration', 'sprint_speed', 'dribbling', 'agility', 'balance',
        'reactions', 'ball_control', 'composure', 'shooting', 'positioning',
        'finishing','shot_power', 'long_shots', 'volleys', 'penalties', 'passing',
        'vision', 'crossing', 'free_kick', 'short_pass', 'long_pass',
        'pass_curve', 'defending', 'interceptions', 'heading', 'marking', 
        'standing_tackle', 'sliding_tackle', 'physicality',
        'jumping', 'stamina', 'strength', 'aggression', 'diving', 'reflexes',
        'handling', 'speed', 'kicking', 'positoning']

field_all_columns = ['pace',
        'acceleration', 'sprint_speed', 'dribbling', 'agility', 'balance',
        'reactions', 'ball_control', 'composure', 'shooting', 'positioning',
        'finishing','shot_power', 'long_shots', 'volleys', 'penalties', 'passing',
        'vision', 'crossing', 'free_kick', 'short_pass', 'long_pass',
        'pass_curve', 'defending', 'interceptions', 'heading', 'marking', 
        'standing_tackle', 'sliding_tackle', 'physicality',
        'jumping', 'stamina', 'strength', 'aggression']

field_indi_columns = [
        'acceleration', 'sprint_speed', 'agility', 'balance',
        'reactions', 'ball_control', 'composure', 'positioning',
        'finishing','shot_power', 'long_shots', 'volleys', 'penalties',
        'vision', 'crossing', 'free_kick', 'short_pass', 'long_pass',
        'pass_curve', 'interceptions', 'heading', 'marking', 
        'standing_tackle', 'sliding_tackle',
        'jumping', 'stamina', 'strength', 'aggression']

agg_columns = ['pace', 'shooting', 'defending', 'passing', 'dribbling',
               'physicality']

gk_columns = ['diving', 'reflexes',
        'handling', 'speed', 'kicking', 'positoning']

# clean up data frame to only contain continuous variables ----
fifa_df.columns = [name.lower().replace(" ", "_")
                   for name in fifa_df.columns]

# split data into field players and goalkeepers

gk_df = fifa_df[fifa_df['position'] == 'GK']

field_df = fifa_df[fifa_df['position'] != 'GK']

# clean up data by dropping unnecessary columns ___
field_clean_df = field_df.drop(columns=['unnamed:_0', 'club',
                                     'league','nationality', 'position',
                                      'age','preferred_foot','attacking_workrate',
                                      'defensive_workrate',
                                      'skill_moves', 'weak_foot']
                                      ).set_index('player_name')


gk_clean_df = gk_df.drop(columns=['unnamed:_0', 'club',
                                     'league','nationality', 'position',
                                      'age','preferred_foot','attacking_workrate',
                                      'defensive_workrate',
                                      'skill_moves', 'weak_foot']
                                      ).set_index('player_name')


field_clean_df = (field_clean_df
           .filter(field_indi_columns)
           .dropna())

gk_clean_df = (gk_clean_df
           .filter(gk_columns)
           .dropna())



#fifa_clean_df.to_csv("write_data/clean_all_players.csv", index=True)

# scale it ----
#fifa_scaled_df = (StandardScaler()
                  #.fit(fifa_clean_df)
                  #transform(fifa_clean_df))




def pca_builder():
        """This function takes the cleaned dataframe, applies PCA to it,
        and returns a csv file for the PCA dataframe."""
        
        # instatiate PCA object ----
        pca = PCA(n_components=2, random_state=10)

        # fit fifa_df onto pca ----
        pca.fit(fifa_scaled_df)


        pc_df = pd.DataFrame({'pc1': np.matmul(fifa_scaled_df, pca.components_[0]),
                     'pc2': np.matmul(fifa_scaled_df, pca.components_[1])},
                     index=fifa_df.index)

        #pc_df.to_csv("write_data/pc_all_players.csv", index=True)
        return pc_df