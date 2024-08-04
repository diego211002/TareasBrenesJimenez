def operation_selector(num1, num2, op):
    # Verificar que num1 y num2 sean números enteros
    if not isinstance(num1, int) or not isinstance(num2, int):
        return -50, None  # Código de error -50: num1 o num2 no son enteros
    if isinstance(num1, bool) or isinstance(num2, bool):
        return -50, None  # Código de error -50: num1 o num2 no son enteros
    # Verificar que op sea de tipo string
    if not isinstance(op, str):
        return -60, None  # Código de error -60: op no es de tipo string
    # Verificar que op sea una de las opciones permitidas
    if op not in ['+', '-', '*', '&']:
        return -70, None
    # Código de error -70: op no es una de las opciones válidas
    # Realizar la operación según el operador
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '&':
        result = num1 & num2
    return 0, result  # Código de éxito 0: operación realizada correctamente


def calculo_promedio(lista_valores):
    # Verificar que todos los elementos de la lista sean números (int o float) y no sean booleanos
    if not all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in lista_valores):
        return -80, None
    # Código de error -80: Al menos un elemento no es un número

    # Verificar que la lista no tenga más de 10 elementos
    if len(lista_valores) > 10:
        return -90, None
    # Código de error -90: La lista tiene más de 10 elementos

    # Calcular el promedio si todas las verificaciones son correctas
    promedio = sum(lista_valores) / len(lista_valores)

    return 0, promedio  # Código de éxito 0: operación realizada correctamente
