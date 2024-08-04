def operation_selector(num1, num2, op):
    """
    Selecciona y realiza una operación matemática o bit a bit entre dos números

    Parámetros:
    num1 (int): El primer número entero.
    num2 (int): El segundo número entero.
    op (str): El operador define la operación a realizar.

    """
    # Verifica qué operación realizar basado en el operador seleccionado
    if op == '+':
        return num1 + num2  # Retorna la suma de los dos números
    elif op == '-':
        return num1 - num2  # Retorna resta del primer número menos el segundo
    elif op == '*':
        return num1 * num2  # Retorna el producto de los dos números
    elif op == '&':
        return num1 & num2  # Retorna la operación bit a bit AND de los números
    else:
        return "Operación no válida"  # Retorna un mensaje de error


# Solicita al usuario que introduzca el primer número entero
num1 = int(input("Introduce el primer número entero: "))

# Solicita al usuario que introduzca el segundo número entero
num2 = int(input("Introduce el segundo número entero: "))

# Solicita al usuario que introduzca el operador deseado
op = input("Introduce el operador (+, -, *, &): ")

# Realiza la operación seleccionada y almacena el resultado
resultado = operation_selector(num1, num2, op)

# Muestra el resultado de la operación al usuario
print(f"El resultado de {num1} {op} {num2} es: {resultado}")
