# tests/test_app.py
from app.app import add

def test_add():
    assert add(2, 3) == 5
