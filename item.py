from database import Graph as Gp

db = Gp('bolt://3.93.238.219:7687', 'neo4j', 'patients-plug-blasts')


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
    def pesquisar(cod):
        query = str('MATCH(i:Item{codigo:' + f'{cod}' + '})' +
                    'RETURN i.nome AS nome, i.categoria AS categoria;')
        result = db.execute_query(query)
        for record in result:
            print(f'Item-> Nome: {record["nome"]}, Categoria: {record["categoria"]}')

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
