from django.shortcuts import render


def index(request):
    return render(request, "manager/index.html")

def cadastro(request):
    return render(request, "manager/cadastro.html")

def consulta(request):
    return render(request, "manager/consulta.html")