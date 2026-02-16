from django.shortcuts import render
from .imc import IMC

# Create your views here.

def calcular_imc(request):
    resultado = None
    error = None

    if request.method == "POST":
        try:
            peso = float(request.POST.get("peso"))
            altura = float(request.POST.get("altura"))

            imc_obj = IMC(peso, altura)

            resultado = {
                "imc": round(imc_obj.calcular_imc(), 2),
                "categoria": imc_obj.categoria()
            }

        except ValueError as e:
            error = str(e)
        except Exception:
            error = "Ocurrió un error inesperado"

    return render(request, "imc.html", {
        "resultado": resultado,
        "error": error
    })
