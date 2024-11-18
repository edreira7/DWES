from operaciones import suma, resta, multiplicacion, division

def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, introduce un número válido.")

def obtener_operacion():
    while True:
        operacion = input("¿Qué operación deseas realizar? (suma, resta, multiplicacion, division): ").strip().lower()
        if operacion in ["suma", "resta", "multiplicacion", "division"]:
            return operacion
        else:
            print("Operación no válida. Inténtalo de nuevo.")

def main():
    while True:
        num1 = obtener_numero("Introduce el primer número: ")
        num2 = obtener_numero("Introduce el segundo número: ")
        operacion = obtener_operacion()
        
        if operacion == "suma":
            resultado = suma(num1, num2)
        elif operacion == "resta":
            resultado = resta(num1, num2)
        elif operacion == "multiplicacion":
            resultado = multiplicacion(num1, num2)
        elif operacion == "division":
            resultado = division(num1, num2)

        print(f"El resultado de la {operacion} es: {resultado}")
        
        continuar = input("¿Quieres hacer más operaciones? (s/n): ").strip().lower()
        if continuar != "s":
            print("¡Hasta luego!")
            break

if ( __name__ == "__main__" ):
    main()
