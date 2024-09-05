import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()

from home.models import Produto

produto = Produto(nome='Mouse', preco=659.99)
produto.save()
print('Produto inserido com sucesso!')


