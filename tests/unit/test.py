import pytest
import src.calc as ca


def obtener_datos_suma():
 return [(1, 1, 2), ("1/4", 2, 2.25), (0.5, "1/4", 0.75)]


@pytest.mark.parametrize("numero1,numero2,resultado",obtener_datos_suma())
def test_suma(numero1, numero2, resultado):
  assert ca.suma(numero1,numero2) == resultado


def obtener_datos_multiplicacion():
  return [("1/2",2,1.0),(2,4,8),(-1,2,-2)]


@pytest.mark.parametrize("numero1,numero2,resultado", obtener_datos_multiplicacion())
def test_multiplicacion(numero1,numero2,resultado):
  assert ca.multiplicacion(numero1,numero2) == resultado


def obtener_datos_test_get_fractions():
  return [(10, 10), ("7/4", 1.75), (-1, -1)]


@pytest.mark.parametrize('num1, esperado', obtener_datos_test_get_fractions())
def test_get_fractions_parametrize(num1, esperado):
        assert ca.get_fractions(num1) == esperado
