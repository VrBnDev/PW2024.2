from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    return render(request, 'contato.html')


def desafio(request):
    contexto = {
        'lista' :[
        {'id': 1, 'nome': 'Perfil','descricao': 'Redicione o usuário para uma página com uma saudação e o nome dele.', 'imagem': "perfil.jpg", "input": "inline", 'url': "perfil"},
        {'id': 2, 'nome': 'Dias da Semana','descricao': 'Caro usuário você tem direito a uma mensagem semanal. Para escolher sua mensagem, escolha um número de 1 a 7.', 'imagem': "diassemanas.png", "input": "inline", 'url': "diasemana"},
        {'id': 3, 'nome': 'Produtos','descricao': 'Nesse case uma listagem de produtos foi cadastrado.', 'imagem': "produtos.jpg", "input": "none", 'url': "produto"},
    ]}

    return render(request, 'desafio.html', contexto)


def perfil(request, usuario):
    return render(request, 'perfil.html', {'usuario': usuario})


def diasemana(request, dia):
    semana = {'1': 'Domingo', '2': 'Segunda-feira', '3': 'Terça-feira', '4':'Quarta-feira', '5': 'Quinta-feira', '6': 'Sexta-feira', '7':'Sábado'}

    if dia not in semana:
        return render(request, 'diasemana.html', {'dia': 'inválido'})

    return render(request, 'diasemana.html', {'dia': semana[dia]})

def lista(request):
    contexto = {
        'lista': [
            {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00'},
            {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
            {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
        ]
    }

    return render(request, 'produto/lista.html', contexto)

def formularioproduto(request):
    return render(request, 'produto/formulario.html')