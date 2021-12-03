from database import Graph as Gp

db = Gp('bolt://localhost:7687', 'neo4j', '12345')


class Item:
    def __init__(self, nome, cod, categoria, especificacao, prat, andar):
        self.nome = nome
        self.cod = cod
        self.categoria = categoria
        self.especificacao = especificacao
        self.prat = prat
        self.andar = andar

        query1 = str(
            'CREATE(i:Item' + '{nome:"' + f'{self.nome}",' + f'código:{self.cod},' +
            f'categoria:"{self.categoria}",' + f'especificação:{self.especificacao}'
            + '}) RETURN i')
        db.execute_query(query1)

        query2 = str('CREATE(:Prateleira' + '{número:' + f'{self.prat},' + f'andar:{self.andar}'
                     + '});')
        db.execute_query(query2)

    def inserir_prat(self):

        query3 = str('MATCH(p:Prateleira{número:' + f'{self.prat}, ' + f'andar:{self.andar}' +
                     '}),(i:Item{nome:' + f'"{self.nome}",' + 'código:' + f'{self.cod},' +
                     'categoria:' + f'"{self.categoria}",' +
                     'especificação:' + f'{self.especificacao}' +
                     '})RETURN i, p')
        result = db.execute_query(query3)

        if len(result) != 0:
            print(len(result), 'sucesso')
            return 1
        else:
            print(len(result), 'fracasso')
            return 0

    @staticmethod
    def pesquisar(nome='', cod='', categoria='', espec='', prat='', andar=''):

        exp_comp = (nome != '' and cod != '' and categoria == 'Componente'
                    and espec != '' and prat != '' and andar != '')
        exp_fer = (nome != '' and cod != '' and categoria == 'Ferramenta'
                   and espec == '' and prat != '' and andar != '')
        # Pesquisa completa
        if exp_comp:
            query = str('MATCH(p:Prateleira{número:' + f'{prat}, ' +
                        f'andar:{andar}' +
                        '}),(i:Item{nome:' + f'"{nome}",' +
                        'código:' + f'{cod},' +
                        'categoria:' + f'"{categoria}",' +
                        'especificação:' + f'{espec}' +
                        '})RETURN i.nome AS nome,' +
                        ' i.especificação AS especificação,' +
                        'i.categoria AS categoria, ' +
                        'p.número AS número,'
                        'p.andar AS andar;')
            result = db.execute_query(query)
            print(query)
            for record in result:
                return str(f'Nome: {record["nome"]}, '
                           f'Especificação: {record["especificação"]}\n' +
                           f'Prateleira: {record["número"]}, ' +
                           f'Andar:{record["andar"]}')
            if len(result) == 0:
                return 'Nenhum resultado encontrado'
        if exp_fer:
            query = str('MATCH(p:Prateleira{número:' + f'{prat}, ' +
                        f'andar:{andar}' +
                        '}),(i:Item{nome:' + f'"{nome}",' +
                        'código:' + f'{cod},' +
                        'categoria:' + f'"{categoria}"' +
                        '})RETURN i.nome AS nome,' +
                        'p.número AS número,'
                        'p.andar AS andar;')
            result = db.execute_query(query)
            print(query)
            for record in result:
                return str(f'Nome: {record["nome"]},\n'
                           f'Prateleira: {record["número"]}, ' +
                           f'Andar:{record["andar"]}')
            if len(result) == 0:
                return 'Nenhum resultado encontrado'
        else:
            return 'Por favor preencha todos os campos!'

    # Recebe o código e atualiza o restante dos parametros mas mantem o lugar na prateleira
    @staticmethod
    def atualizar(cod='', nome='', categoria='', espec=''):

        query = str('MATCH(i:Item{código:' + f'{cod}' + '})' +
                    'SET i.nome =' + f'"{nome}",' +
                    'i.categoria = ' + f'"{categoria}", ' +
                    'i.especificação = ' + f'{espec}' +
                    'RETURN i.código as cod')
        result = db.write(query)
        if len(result) == 1:
            return 1
        else:
            return 0

    @staticmethod
    def remover(cod):
        query = 'MATCH(i:Item{código:' + f'{cod}' + '})' + ' DETACH DELETE i RETURN 1'
        result = db.write(query)

        if len(result) == 1:
            return 1
        else:
            return 0

    @staticmethod
    def limpar_grafo():
        query = 'MATCH (n) DETACH DELETE n'
        db.execute_query(query)
