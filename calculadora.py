def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def multiplicar(a, b):
    return a * b

while True:

    print("\n📌 Calculadora Interactiva")
    print("1. Sumar ➕")
    print("2. Restar ➖")
    print("3. Dividir ➗")
    print("4. Multiplicacion ✖️")
    print("5. Salir ❌")

    option = input("Elige una opcion (1-5): ")

    if option == '5':
        print("¡Hasta luego! 👋")
        break

    if option not in ['1', '2', '3', '4']:
        print("❌ Opción inválida. Intenta de nuevo.")
        continue

    try:
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
    except ValueError:
        print("❌ Entrada inválida. Debes ingresar números.")
        continue

    if option == '1':
        print(f"✅ Resultado: {sumar(num1, num2)}")
    elif option == '2':
        print(f"✅ Resultado: {restar(num1, num2)}")
    elif option == '3':
        print(f"✅ Resultado: {dividir(num1, num2)}")
    elif option == '4':
        print(f"✅ Resultado: {multiplicar(num1, num2)}")