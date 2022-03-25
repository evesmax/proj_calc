def multiplicacion(a, b):
    """
    Función para multiplicar dos números
    Params:
      a: Primer número a multiplicar
      b: Segundo número a multiplicar
    Returns:
      El producto de a y b.
    >>>multiplicacion(5,"6/25")
      1.2
    """
    mult_a = get_fractions(a)
    mult_b = get_fractions(b)
    return mult_a * mult_b


def suma(a, b):
    """
    Calcula la suma entre dos números
    :param a: el valor del minuendo
    :param b: el valor del sustraendo
    :return: la suma entre el parámetro a y b.
    >>> suma(2,1)
    1
    >>> suma(1,2)
    -1
    """
    sumando_a = get_fractions(a)
    sumando_b = get_fractions(b)
    return sumando_a + sumando_b


def get_fractions(entrada):
    """ Recibe un numero elimina las fracciones y regresa el resultado"""
    numero = 0
    try:
        if isinstance(entrada, str):
            print(entrada)
            if "/" in entrada:
                arr = entrada.split("/")
                numerador = arr[0]
                denominador = arr[1]
                # print(arr)
                numero = float(numerador) / float(denominador)
                # print(arr, numero)
            else:
                numero = float(entrada)
                print(type(numero))

        if isinstance(entrada, int) or isinstance(entrada, float):
            numero = entrada
    except:
        print("Error de formato de numero")

    return numero
