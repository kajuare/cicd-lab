# tests/test_app.py
from app.app import add, multiply 
 
def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(3, 4) == 12
