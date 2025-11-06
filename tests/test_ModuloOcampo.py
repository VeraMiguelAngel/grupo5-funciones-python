#tests/test_modulo.py
from funciones.moduloOcampo import modulo
def test_modulo():
 assert modulo(10, 3) == 1
 assert modulo(7, 0) is None
