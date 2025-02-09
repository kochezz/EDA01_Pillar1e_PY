import pandas as pd
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from feature_engineering import encode_labels


def test_encode_labels():
    df = pd.DataFrame({'species': ['setosa', 'versicolor', 'virginica']})
    df = encode_labels(df, 'species')
    assert df['species'].tolist() == [0, 1, 2]