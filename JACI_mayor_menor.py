def main():
    print("MAYOR y MENOR")
    numero = int(input("¿Cuántos valores va a introducir? "))

    if numero <= 0:
        print("No se puede comparar amigo")
    else:
        valor = float(input("Escriba el número 1: "))
        minimo = maximo = suma = valor
        for i in range(2, numero + 1):
            valor = float(input(f"Escriba el número {i}: "))
            suma = suma + valor
            if valor < minimo:
                minimo = valor
            if valor > maximo:
                maximo = valor
        print(f"El número menor es: {minimo}")
        print(f"El número mayor es: {maximo}")
      

if __name__ == "__main__":
    main()
