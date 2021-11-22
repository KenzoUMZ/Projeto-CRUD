from database import Graph as Gp
from names import get_full_name as gfn
from random import randint, choice
from item import Item as it

db = Gp('bolt://localhost:7687', 'neo4j', '12345')


# Esse arquivo serve exclusivamente pra inserir dados hipotéticos no DB
def insert_all():
    # Deletando DB
    it.limpar_grafo()

    cursos = ('GEB', 'GEC', 'GEA', 'GEP', 'GES', 'GET', 'GEE')
    componentes = ('Resistor', 'Potenciômetro', 'Capacitor', 'Diodo', 'Led', 'Bateria')
    ferramentas = ('Multímetro', 'Fita Isolante', 'Tesoura', 'Jacarés', 'Gerador de Funções', 'Osciloscópio')

    for i in range(100):
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
        rand_andar = randint(1, 200)
        rand_comp = choice(componentes)
        rand_fer = choice(ferramentas)
        query_componente = str('CREATE(:Item{' +
                               f'código:{rand_cod},' +
                               f'categoria:"Componente",' +
                               f'nome:"{rand_comp}",' +
                               f'especificação:{rand_val * pow(10, rand_exp)}' +
                               '});')

        query_ferramenta = str('CREATE(:Item{' +
                               f'código:{rand_cod2},' +
                               f'categoria:"Ferramenta",' +
                               f'nome:"{rand_fer}"' + '});')

        query_prateleira = str('CREATE(:Prateleira{' +
                               f'número:{i},' +
                               f'andar:{rand_andar}' + '});')

        query_inserir_prateleira = str('MATCH(p:Prateleira{número:' + f'{i},'
                                       + f'andar:{rand_andar}' +
                                       '}),(i:Item{nome:' + f'"{rand_comp}",'
                                       + 'código:' + f'{rand_cod},'
                                       + 'categoria:' + '"Componente",' +
                                       'especificação:' + f'{rand_val * pow(10, rand_exp)}' +
                                       '}),' + '(j:Item{nome:' + f'"{rand_fer}",'
                                       + 'código:' + f'{rand_cod2},' +
                                       'categoria:' + '"Ferramenta"' +
                                       '})' + 'CREATE(i) - [: LOCALIZADO_EM]->(p)' +
                                       'CREATE(j) - [: LOCALIZADO_EM]->(p)')

        print(query_inserir_prateleira)
        db.execute_query(query_ferramenta)
        db.execute_query(query_componente)
        db.execute_query(query_prateleira)
        db.execute_query(query_inserir_prateleira)
