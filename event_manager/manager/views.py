from django.shortcuts import render

testlist = ['Teste 1', 'Teste 2', 'Teste 3', 'Teste 4']

def index(request):
    return render(request, "manager/index.html")

def cadastro(request):
    return render(request, "manager/cadastro.html")

def cadastro_sala(request):
    return render(request, "manager/cadastro_sala.html")

def cadastro_cafe(request):
    return render(request, "manager/cadastro_cafe.html")

def consulta(request):
    return render(request, "manager/consulta.html", {
        "entries": testlist
    })