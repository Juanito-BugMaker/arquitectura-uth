from django.shortcuts import render
from .triangulo import TrianguloRectangulo

# Create your views here.

def calcular_triangulo(request):
    resultado = None
    error = None

    if request.method == "POST":
        try:
            base = float(request.POST.get("base"))
            altura = float(request.POST.get("altura"))

            triangulo = TrianguloRectangulo(base, altura)

            resultado = {
                "area": triangulo.calcular_area(),
                "hipotenusa": triangulo.calcular_hipotenusa(),
                "perimetro": triangulo.calcular_perimetro()
            }

        except ValueError as e:
            error = str(e)
        except Exception:
            error = "Ocurrió un error inesperado"

    return render(request, "triangulo.html", {
        "resultado": resultado,
        "error": error
    })

