from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    return render(request, 'contato.html')


def ajuda(request):
    return render(request, 'ajuda.html')


def perfil(request, usuario):
    return render(request, 'perfil.html', {'usuario': usuario})


def diasemana(request, dia):
    semana = {'1': 'Domingo', '2': 'Segunda-feira', '3': 'Terça-feira', '4':'Quarta-feira', '5': 'Quinta-feira', '6': 'Sexta-feira', '7':'Sábado'}

    if dia not in semana:
        return render(request, 'diasemana.html', {'dia': 'inválido'})

    return render(request, 'diasemana.html', {'dia': semana[dia]})
