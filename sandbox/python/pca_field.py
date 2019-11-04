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

field_all_columns = ['pace',
        'acceleration', 'sprint_speed', 'dribbling', 'agility', 'balance',
        'reactions', 'ball_control', 'composure', 'shooting', 'positioning',
        'finishing','shot_power', 'long_shots', 'volleys', 'penalties', 'passing',
        'vision', 'crossing', 'free_kick', 'short_pass', 'long_pass',
        'pass_curve', 'defending', 'interceptions', 'heading', 'marking', 
        'standing_tackle', 'sliding_tackle', 'physicality',
        'jumping', 'stamina', 'strength', 'aggression']

        fifa_df.columns = [name.lower().replace(" ", "_")
                   for name in fifa_df.columns]

field_df = fifa_df[fifa_df['position'] != 'GK']

field_clean_df = field_df.drop(columns=['unnamed:_0', 'club',
                                     'league','nationality', 'position',
                                      'age','preferred_foot',
                                      'attacking_workrate',
                                      'defensive_workrate',
                                      'skill_moves', 'weak_foot']
                                      ).set_index('player_name')

def field_df_att(columns):
    field_clean_df = (field_clean_df
           .filter(columns)
           .dropna())
    return field_clean_df

field_clean_arr = field_clean_df.to_numpy()

pca = PCA(n_components=3, random_state=10)

        # fit fifa_df onto pca ----
pca.fit(field_clean_arr)

field_pca_df = pd.DataFrame(
                    {'pc1': np.matmul(field_clean_arr, pca.components_[0]),
                    'pc2': np.matmul(field_clean_arr, pca.components_[1]),
                    'pc3': np.matmul(field_clean_arr, pca.components_[2])},
                    index=field_clean_df.index)

model_field = KMeans(n_clusters=5).fit(field_pca_df)

model_field.cluster_centers_

# Generate cluster index values for each row in df
cluster_assignments_field = model_field.predict(field_pca_df) 

field_df['classification'] = cluster_assignments_field

cluster1 = field_df[field_df['classification'] == 0]
cluster2 = field_df[field_df['classification'] == 1]
cluster3 = field_df[field_df['classification'] == 2]
cluster4 = field_df[field_df['classification'] == 3]
cluster5 = field_df[field_df['classification'] == 4]