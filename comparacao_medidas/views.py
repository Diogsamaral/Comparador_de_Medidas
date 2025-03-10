# views.py
import math
from django.shortcuts import render
from .forms import MedidasClienteForm, TabelaMedidasForm
from .models import TabelaMedidas

def calcular_diferencas(medidas_cliente, medidas_tabela):
    # Implemente a lógica de cálculo das diferenças aqui
    def distancia_euclidiana(medidas1, medidas2):
        return math.sqrt(sum((medidas1[dim] - medidas2[dim]) ** 2 for dim in medidas1))
    
    resultados_comparacao = {}
    
    for tamanho, medidas in TabelaMedidas.items():
        proximidade = distancia_euclidiana(medidas_cliente, medidas)
        diferenca_individual = {dim: medidas[dim] - medidas_cliente[dim] for dim in medidas}
        resultados_comparacao[tamanho] = {'proximidade': proximidade, 'diferenca_individual': diferenca_individual}


    # Suponha que você tenha um resultado de comparação em forma de dicionário chamado 'resultado'
    resultado = resultados_comparacao[tamanho]  # Substitua isso com o seu resultado real
    return resultado

def comparar_medidas(request):
    if request.method == 'POST':
        medidas_form = MedidasClienteForm(request.POST)
        tabela_form = TabelaMedidasForm(request.POST)
        if medidas_form.is_valid() and tabela_form.is_valid():
            medidas_cliente = medidas_form.save(commit=False)
            tabela_medidas_nome = tabela_form.cleaned_data['nome']
            tabela_medidas = TabelaMedidas.objects.get(nome=tabela_medidas_nome)
            
            resultado = calcular_diferencas(medidas_cliente, tabela_medidas)
            
            return render(request, 'resultado.html', {'resultado': resultado})
    else:
        medidas_form = MedidasClienteForm()
        tabela_form = TabelaMedidasForm()

    return render(request, 'comparar_medidas.html', {'medidas_form': medidas_form, 'tabela_form': tabela_form})
