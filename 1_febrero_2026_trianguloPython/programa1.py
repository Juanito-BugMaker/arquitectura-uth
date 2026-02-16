from triangulo import TrianguloRectangulo

def main():
    try:
        altura = float(input("Ingrese el altura del triangulo :"))
        base = float(input("Ingrese la base del triangulo :"))

        triangulo = TrianguloRectangulo(base, altura)
        triangulo.resultados()

    except ValueError as e:
        print("Error de entrada: ",e)
    except Exception:
        print("Error ocurrio algo no esperado")

# Programa principal
if __name__ == "__main__":
    main()