from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import pandas as pd
from joblib import dump
from joblib import load

model_field_df = pd.read_csv('write_data/model_field_players.csv')\
                            .set_index('player_name')

X = model_field_df.drop(['classification'], axis=1)
y = model_field_df['classification']
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                   random_state=1)

rf = RandomForestClassifier(n_estimators=300,
                            max_features='sqrt',
                            random_state=10)
rf.fit(X_train, y_train)

pipe = Pipeline(steps=[("football_model", rf)])

pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)

dump(pipe, 'football_model.joblib')

loaded = load('football_model.joblib')