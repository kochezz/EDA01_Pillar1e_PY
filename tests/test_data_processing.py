import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from data_processing import load_data, save_data


def test_load_data():
    df = load_data('../data/raw/Iris.csv')
    assert isinstance(df, pd.DataFrame)

def test_save_data():
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    save_data(df, '../data/processed/test.csv')
    loaded_df = pd.read_csv('../data/processed/test.csv')
    assert loaded_df.equals(df)