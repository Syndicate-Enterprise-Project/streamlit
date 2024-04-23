import pandas as pd


def load_data_clean():
    return pd.read_csv('dataset-clean.csv')


def load_data_modelling():
    return pd.read_csv('dataset-modelling.csv')
