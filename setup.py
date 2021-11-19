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
    categorias = ('Ferramenta', 'Componente')
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
        rand_exp = randint(-6, 6)
        rand_cod = randint(1000, 1200)
        rand_cod2 = randint(1000, 1200)

        query_componente = str('CREATE(:Item{' +
                               f'código:{rand_cod},' +
                               f'categoria:"Componente",' +
                               f'nome:"{choice(componentes)}",' +
                               f'especificação:{rand_val * pow(10, rand_exp)}' +
                               '});')
        query_ferramenta = str('CREATE(:Item{' +
                               f'código:{rand_cod2},' +
                               f'categoria:"Ferramenta",' +
                               f'nome:"{choice(ferramentas)}"' + '});')

        db.execute_query(query_ferramenta)
        db.execute_query(query_componente)
