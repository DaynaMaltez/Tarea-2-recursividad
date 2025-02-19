def convertir_binario(n):
  if n == 0:
    return "0"
  elif n == 1:
    return "1"
  else: 
    return convertir_binario(n // 2) + str(n % 2)
  
def contar_digitos (n):
  if abs(n) < 10:
    return 1
  return 1 + contar_digitos(n // 10)
    
    
def calcular_raiz(n, i=1):
    if i * i > n:
        return i - 1
    return calcular_raiz(n, i + 1)

def raiz_cuadrada_entera(n):
    return calcular_raiz(n)

romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def convertir_decimal(romano, index=0):
    if index == len(romano) - 1:
        return romanos[romano[index]]
    actual = romanos[romano[index]]
    siguiente = romanos[romano[index + 1]]
    if actual < siguiente:
        return -actual + convertir_decimal(romano, index + 1)
    else:
        return actual + convertir_decimal(romano, index + 1)

def suma(n):
    if n == 0:
        return 0
    return n + suma(n - 1)

def menu():
    while True:
        print("\nMenú:")
        print("1. Convertir a Binario")
        print("2. Contar Dígitos")
        print("3. Raíz Cuadrada Entera")
        print("4. Convertir a Decimal desde Romano")
        print("5. Suma de Números Enteros")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            num = int(input("Ingrese un número: "))
            print("Binario:", convertir_binario(num))
        elif opcion == '2':
            num = int(input("Ingrese un número: "))
            print("Cantidad de dígitos:", contar_digitos(num))
        elif opcion == '3':
            num = int(input("Ingrese un número: "))
            print("La raíz cuadrada es:", raiz_cuadrada_entera(num))
        elif opcion == '4':
            romano = input("Ingrese un número romano: ").upper()
            print("El decimal es:", convertir_decimal(romano))
        elif opcion == '5':
            num = int(input("Ingrese un número: "))
            print("La suma es:", suma(num))
        elif opcion == '6':
            print("Ha salido")
            break
        else:
            print("Opción invalida. Intente de nuevo.")

if __name__ == "__main__":
    menu()