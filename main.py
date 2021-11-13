from item import Item as It

print('Menu Almoxarifado:')
print('''
1 - Cadastrar novo item
2 - Pesquisar 
3 - Atualizar nome/categoria
4 - Remover do estoque
''')
op = int(input('Sua opção: '))

# Cadastrando novo produto
if op == 1:
    nome = str(input('Digite o nome: '))
    cod = int(input('Digite o codigo: '))
    categoria = str(input('Digite a categoria: '))
    item = It(nome, cod, categoria)
# Pesquisando produto
elif op == 2:
    cod = int(input('Digite o codigo: '))
    It.pesquisar(cod)
# Atualizando item
elif op == 3:
    cod = int(input('Digite o codigo do produto: '))
    nome = str(input('Digite o nome: '))
    categoria = str(input('Digite a categoria: '))
    It.atualizar(cod, nome, categoria)
#  Removendo item do estoque
elif op == 4:
    cod = int(input('Digite o codigo do produto: '))
    It.remover(cod)
