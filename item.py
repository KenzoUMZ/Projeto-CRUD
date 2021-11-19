from database import Graph as Gp

db = Gp('bolt://localhost:7687', 'neo4j', '12345')


class Item:
    def __init__(self, nome, cod, categoria):
        self.nome = nome
        self.cod = cod
        self.categoria = categoria
        query = str(
            'CREATE(:Item' + '{nome:"' + f'{self.nome}",' + f'codigo:{self.cod},' +
            f'categoria:"{self.categoria}"' + '});')
        db.write(query)

    @staticmethod
    def pesquisar(cod='', nome='', categoria=''):

        if nome == '' and categoria == '':
            query = str('MATCH(i:Item{codigo:' + f'{cod}' + '})' +
                        'RETURN i.nome AS nome, i.categoria AS categoria;')
            result = db.execute_query(query)
            for record in result:
                return f'Item-> Nome: {record["nome"]}, Categoria: {record["categoria"]}'

        elif cod == '' and categoria == '':
            print('somente nome recebido')
            query = str('MATCH(i:Item{nome:' + f'"{nome}"' + '})' +
                        'RETURN i.nome AS nome, i.categoria AS categoria;')
            print(query)
            result = db.execute_query(query)
            for record in result:
                return f'Item-> Nome: {record["nome"]}, Categoria: {record["categoria"]}'

        elif cod == '' and nome == '':
            query = str('MATCH(i:Item{ categoria:' + f'{categoria}' + '})' +
                        'RETURN i.nome AS nome, i.categoria AS categoria;')
            result = db.execute_query(query)
            for record in result:
                return f'Item-> Nome: {record["nome"]}, Categoria: {record["categoria"]}'
        else:
            print('to aq')
            return 'Nenhum resultado encontrado'

    @staticmethod
    def atualizar(cod, nome, categoria):
        query = str('MATCH(i:Item{codigo:' + f'{cod}' + '})' +
                    'SET i.nome =' + f'"{nome}",' + 'i.categoria = ' + f'"{categoria}"')
        db.write(query)

    @staticmethod
    def remover(cod):
        query = 'MATCH(i:Item{codigo:' + f'{cod}' + '})' + ' DETACH DELETE i'
        db.write(query)

    @staticmethod
    def limpar_grafo():
        query = 'MATCH (n) DETACH DELETE n'
        db.execute_query(query)

    @staticmethod
    def inserir_platileira(prat, andar):
        pass
    # query = str('MATCH(i:Pratileira{nome:' + f'{prat}'}),(p:Plataforma{nome:'Xbox'})CREATE(j)-[:DISPONIVEL_PARA]->(p)')
