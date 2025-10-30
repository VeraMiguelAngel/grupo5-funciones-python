from funciones.potencialegal import potencialegal


def test_potencialegal():
    assert potencialegal(2, 3) == 8
    assert potencialegal(5, 0) == 1
