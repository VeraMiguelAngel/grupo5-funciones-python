#tests/test_dividir.py 
from funciones.divisionGomez import dividir 
def test_dividir(): 
    assert dividir(10, 2) == 5 
    assert dividir(5, 0) is None