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

historial = []    
while True:

    print("\n📌 Calculadora Interactiva")
    for key, (nombre, _) in operaciones.items():
        print(f"{key}, {nombre}")
    print("8. ❌ Salir")

    opcion = input("\nElige una opcion (1-8): ")

    if opcion == '8':
        confirmar = input("¿Seguro quieres salir (s/n): ").strip().lower()
        if confirmar == 's':
            print("Hasta luego 👋🏽")
            break
        continue

    if opcion not in operaciones:
        print("❌ Opción inválida. Intenta de nuevo.")
        continue

    nombre, funcion = operaciones[opcion]

    if opcion == '6':
        num1 = obtener_numero("\nIngresar el numero para calcular la raiz: ", permitir_negativos = False)
        resultado = funcion(num1)

    elif opcion == '7':
        num1 = obtener_numero("\nIngresa numero base: ")
        num2 = obtener_numero("\nIngresa el porcentaje a calcular: ")
        resultado = (num1 * num2) / 100

    else:
        num1 = float(input("\nIngresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
        
        if opcion == '3' and num2 == 0:
            print("❌ Error: No se puede dividir por cero")
            continue

        resultado = funcion(num1, num2)
    
    historial.append(f"🔹 {nombre}: {num1} {' ' if opcion == '6' else num2} = {resultado}")
    
    print(f"\n✅ {nombre}: {resultado}")
    print("\n📜 Historial de operaciones:")
    for h in historial:
        print(h)
