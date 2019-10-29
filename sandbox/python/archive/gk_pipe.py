from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import sys
from IPython.core import ultratb
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

fifa_df = pd.read_csv("write_data/all_players.csv")
gk_columns = ['diving', 'reflexes',
        'handling', 'speed', 'kicking', 'positoning']

# clean up data frame to only contain continuous variables ----
fifa_df.columns = [name.lower().replace(" ", "_")
                   for name in fifa_df.columns]

# split data into field players and goalkeepers

gk_df = fifa_df[fifa_df['position'] == 'GK']

gk_clean_df = gk_df.drop(columns=['unnamed:_0', 'club',
                                     'league','nationality', 'position',
                                      'age','preferred_foot','attacking_workrate',
                                      'defensive_workrate',
                                      'skill_moves', 'weak_foot']
                                      ).set_index('player_name')

gk_clean_df = (gk_clean_df
           .filter(gk_columns)
           .dropna())

gk_clean_arr = gk_clean_df.to_numpy()

pca = PCA(n_components=3, random_state=10)

        # fit fifa_df onto pca ----
pca.fit(gk_clean_arr)

gk_pca_df_3clust = pd.DataFrame({
                'pc1': np.matmul(gk_clean_arr,
                pca.components_[0]),
                'pc2': np.matmul(gk_clean_arr, pca.components_[1]), 
                'pc3': np.matmul(gk_clean_arr, pca.components_[2])},
                index=gk_clean_df.index)


model_gk = KMeans(n_clusters=4).fit(gk_pca_df)
model_gk.cluster_centers_

# Generate cluster index values for each row in df
cluster_assignments_gk = model_field.predict(gk_pca_df) 

gk_df['classification'] = cluster_assignments_gk

cluster1 = field_df[field_df['classification'] == 0]
cluster2 = field_df[field_df['classification'] == 1]
cluster3 = field_df[field_df['classification'] == 2]
cluster4 = field_df[field_df['classification'] == 3]

