from database import Graph as Gp
from tkinter.messagebox import showinfo
import tkinter as tk

db = Gp('bolt://localhost:7687', 'neo4j', '12345')


class Usuario:
    def __init__(self, matricula, curso):
        self.matricula = matricula
        self.curso = curso

    def Autenticacao(self):
        values = ['Selecione seu curso',
                  'Engenharia Biomédica',
                  'Engenharia de Computação',
                  'Engenharia de Controle e Automação',
                  'Engenharia Elétrica',
                  'Engenharia de Produção',
                  'Engenharia de Software',
                  'Engenharia de Telecomunicações']
        cursos = ['', 'GEB', 'GEC', 'GEA', 'GEE', 'GEP', 'GES', 'GET']

        for i in range(len(values)):
            if values[i] == self.curso:
                self.curso = cursos[i]

        query = str(
            'MATCH(u:Usuario {matricula:' + f'{self.matricula}, ' +
            f'curso:"{self.curso}"' + '}) RETURN u.nome as nome')
        result = db.execute_query(query)

        print(result)

        if len(result) == 1:
            print('Aluno Autenticado')
            return 1
        elif len(result) == 0:
            print('Not Found')
            return 0
