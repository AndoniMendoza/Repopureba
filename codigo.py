# Función para realizar una suma
def suma(a, b):
    return a + b

# Función para realizar una resta
def resta(a, b):
    return a - b

# Función para realizar una multiplicación
def multiplicacion(a, b):
    return a * b

# Función para realizar una división
def division(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    else:
        return a / b

# Función principal de la calculadora
def calculadora():
    print("Selecciona una operación:")
    #print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Esta es una línea de prueba para la opción salir")
    print("6. Otra prueba")

    # Solicitar al usuario que seleccione una operación
    opcion = input("Ingresa el número de la operación que deseas realizar: ")

    # Solicitar al usuario que ingrese dos números
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == '1':
        resultado = suma(num1, num2)
    elif opcion == '2':
        resultado = resta(num1, num2)
    elif opcion == '3':
        resultado = multiplicacion(num1, num2)
    elif opcion == '4':
        resultado = division(num1, num2)
    else:
        resultado = "Opción no válida"

    print("El resultado es:", resultado)

# Llamar a la función principal de la calculadora
calculadora()
