import operator
import math

operaciones = {

    '1': ('Sumar', operator.add),
    '2': ('Restar', operator.sub),
    '3': ('Dividir', operator.truediv),
    '4': ('Multiplicacion', operator.mul),
    '5': ('Potencias', operator.pow),
    '6': ('Raiz', math.sqrt),
    '7': ('Porcentaje', None)   
}


def mostrar_menu(operaciones):
    print("\n📌 Calculadora Interactiva")
    for key, (nombre, _) in operaciones.items():
        print(f"{key}, {nombre}")
    print("8. ❌ Salir")

    opcion = input("\nElige una opcion (1-8): ")
    return opcion


def obtener_numero(mensaje, permitir_negativos = True):
    while True:
        try:
            num = float(input(mensaje))
            if not permitir_negativos and num < 0:
                print("❌ No puedes ingresar numeros negativos")
                continue
            return num
        except ValueError:
             print("❌ Entrada inválida. Debes ingresar números.")


def calcular_raiz():
    num = obtener_numero("\nIngresar el numero para calcular la raiz: ", permitir_negativos = False)
    resultado = math.sqrt(num)
    mensaje = f"Raiz cuadrada de {num} = {resultado}"
    return resultado, mensaje

def calcular_porcentaje():
    base = obtener_numero("Ingrese un numero base: ")
    porcentaje = obtener_numero("Ingrese el pocentaje a calcular: ")
    resultado = (base * porcentaje) / 100
    mensaje = f"Porcentaje = {porcentaje}% de {base} = {resultado}"
    return resultado, mensaje

def calcular_basico(funcion, nombre):
    num1 = obtener_numero("Ingresa el primer numero: ")
    num2 = obtener_numero("Ingresa el segundo numero: ")

    if nombre == 'Dividir' and num2 == 0:
            print("❌ Error: No se puede dividir por cero")
            return None, None

    resultado = funcion(num1, num2)
    mensaje = f"{nombre} = {num1} y {num2} = {resultado}"
    return resultado, mensaje

def mostrar_historial(historial):
    print("\n📜 Historial de operaciones:")
    for h in historial:
        print(h)

def confirmar_salida():
    respuesta = input("¿Seguro que quieres salir? (s/n): ").strip().lower()
    return respuesta == "s"

def main():

    historial = []    
    while True:
        opcion = mostrar_menu(operaciones)

        if opcion == '8':
            if confirmar_salida():
                print("Hasta luego 👋🏽")
                break
            continue

        if opcion not in operaciones:
            print("❌ Opción inválida. Intenta de nuevo.")
            continue

        nombre, funcion = operaciones[opcion]

        if opcion == '6':
            resultado, mensaje = calcular_raiz()

        elif opcion == '7':
            resultado, mensaje = calcular_porcentaje()

        else:
            resultado, mensaje = calcular_basico(funcion, nombre)
            if resultado is None:
                continue
    
        print(f"\n✅ Resultado: {resultado}")
        historial.append(mensaje)
        mostrar_historial(historial)

if __name__ == "__main__":
    main()