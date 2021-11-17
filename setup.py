from database import Graph as Gp
from names import get_full_name as gfn
from random import randint, choice

db = Gp('bolt://localhost:7687', 'neo4j', '12345')


# Esse arquivo serve exclusivamente pra inserir dados hipotéticos no DB
def insert_all():
    # Deletando DB
    query = 'MATCH(n) DETACH DELETE n'
    db.execute_query(query)

    cursos = ('GEB', 'GEC', 'GEA', 'GEP', 'GES', 'GET', 'GEE')
    componentes = ('Resistor', 'Potenciômetro', 'Capacitor', 'Diodo', 'Led', 'Bateria')
    ferramentas = ('Multímetro', 'Fita Isolante', 'Tesoura', 'Jacarés', 'Gerador de Funções', 'Osciloscópio')
    for i in range(200):
        rand_name = gfn()
        rand_age = randint(17, 27)
        rand_mat = randint(1, 3000)
        query = str('CREATE(:Usuario{nome:' + f'"{rand_name}",' +
                    f'idade:{rand_age},' +
                    f'matricula:{rand_mat},' +
                    f'curso:"{choice(cursos)}"' +
                    '});')
        db.execute_query(query)

        rand_val = randint(10, 500)
        query_componente = str('CREATE(:Componente{nome:' + f'"{choice(componentes)}",' +
                               f'Especificações:{rand_val}' +
                               '});')
        query_ferramenta = str('CREATE(:Ferramenta{nome:' + f'"{choice(ferramentas)}"' + '});')

        db.execute_query(query_ferramenta)
        db.execute_query(query_componente)
