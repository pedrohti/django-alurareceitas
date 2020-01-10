from django.shortcuts import render

receitas = {
    1: 'Lasanha',
    2: 'Sopa de Legumes',
    3: 'Sorvete',
    4: 'Caneloni',
}

dados = {
    'nome_das_receitas' : receitas
}

def index(request):
    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')