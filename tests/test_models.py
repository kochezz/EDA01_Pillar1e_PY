import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from models import train_model

def test_train_model():
    X, y = load_iris(return_X_y=True)
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)
    assert model is not None