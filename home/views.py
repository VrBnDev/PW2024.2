from django.shortcuts import render,redirect
from .models import Produto
from home.forms import ProdutoForm

def home(request):
    return render(request, 'index.html')


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    return render(request, 'contato.html')


def desafio(request):
    contexto = {
        'lista' :[
        {'id': 1, 'nome': 'Perfil','descricao': 'URL: perfil/{nome usuario}', 'imagem': "perfil.jpg", "input": "inline", 'url': "desafio"},
        {'id': 2, 'nome': 'Dias da Semana','descricao': 'URL: diasemana/{dia da semana} ', 'imagem': "diassemanas.png", "input": "inline", 'url': "desafio"},
        {'id': 3, 'nome': 'Produtos','descricao': 'URL: lista ', 'imagem': "produtos.jpg", "input": "none", 'url': "lista"}
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
        'lista': Produto.objects.all()
    }

    return render(request, 'produto/lista.html', contexto)

def formularioproduto(request):
    if request.method == "POST":
        formulario = ProdutoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista') 

    else:
        formulario = ProdutoForm()

    return render(request, 'produto/formulario.html', {"form": formulario})


def editar_produto(request, id):
    produto = Produto.objects.get(pk=id)

    if request.method == "GET":
        form = ProdutoForm(instance=produto)
    else:
        form = ProdutoForm(request.POST,instance=produto)
        if form.is_valid:
            form.save()
            return redirect('lista')
        
    context = {
        'form': form
    }

    return render(request, 'produto/formulario.html', context)

def remover_produto(request, id):
    produto = Produto.objects.get(pk=id)

    if request.method == "POST":
        produto.delete()
        return redirect('lista')

    return render(request, 'produto/remover.html', {'produto': produto})

def base(request):
    return render(request, 'base.html')