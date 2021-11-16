from database import Graph as Gp

db = Gp('bolt://localhost:7687', 'neo4j', '12345')


class Usuario:
    def __init__(self, matricula, curso):
        self.matricula = matricula
        self.curso = curso
        query = str(
            'MATCH(:Usuario' + '{matricula:"' + f'{self.matricula}",' + f'curso:{self.curso},' + '});')
        db.write(query)
