from formation_indus_ds_avancee.feature_engineering import prepare_features
from formation_indus_ds_avancee.train_and_predict import train_model

DATA_PATH = 'data/la-haute-borne-data-2017-2020.csv'
FEATURES_PATH = 'prepared_features'

prepare_features(DATA_PATH, FEATURES_PATH)
train_model(FEATURES_PATH)
