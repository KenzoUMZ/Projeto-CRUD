import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from item import Item as it
from usuario import Usuario


class CRUDScreen:

    def __init__(self, master=None):
        # Labels das fontes
        self.fonte_titulo = ('Verdana', '8')
        self.fonte_labels = ('Calibri', '10', 'bold')
        self.fonte_text_field = ('Calibri Light', '10')

        # Criando containers e labels

        self.container1 = Frame(master)
        self.container1['pady'] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2['padx'] = 20
        self.container2['pady'] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3['padx'] = 20
        self.container3['pady'] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4['padx'] = 20
        self.container4['pady'] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5['padx'] = 20
        self.container5['pady'] = 30
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6['padx'] = 20
        self.container6['pady'] = 6
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7['padx'] = 20
        self.container7['pady'] = 5
        self.container7.pack()

        # Container1

        # Titulo
        self.titulo = Label(self.container1, text='Menu Almoxarifado:')
        self.titulo['font'] = self.fonte_titulo
        self.titulo.pack()

        # Container2
        # Label das categorias
        self.label_categoria = Label(self.container2,
                                     text='Categorias:', font=self.fonte_labels, width=10)
        self.label_categoria.pack(side=LEFT)

        # Radio buttons das categorias
        self.selected_categoria = StringVar()
        self.radiobutton_categoria_comp = ttk.Radiobutton(self.container2,
                                                          width=14,
                                                          text='Componente',
                                                          variable=self.selected_categoria,
                                                          value='C',
                                                          state=NORMAL)
        self.radiobutton_categoria_comp.pack(side=RIGHT, padx=2)
        self.radiobutton_categoria_fer = ttk.Radiobutton(self.container2, width=14,
                                                         text='Ferramenta',
                                                         variable=self.selected_categoria,
                                                         value='F',
                                                         state=NORMAL)
        self.radiobutton_categoria_fer.pack(side=RIGHT, padx=2)

        # Container3
        # Label do nome do item
        self.label_nome = Label(self.container3,
                                text='Item:', font=self.fonte_labels, width=10)
        self.label_nome.pack(side=LEFT)

        # ComboBox do nome do item

        self.componentes_ferramentas = ['Resistor', 'Potenciômetro', 'Capacitor',
                                        'Diodo', 'Led', 'Bateria',
                                        'Multímetro', 'Fita Isolante',
                                        'Tesoura', 'Jacarés', 'Gerador de Funções',
                                        'Osciloscópio']
        self.combobox_nome = ttk.Combobox(self.container3, width=28,
                                          values=self.componentes_ferramentas,
                                          state='readonly', font=self.fonte_text_field)
        self.combobox_nome.current(0)
        self.combobox_nome.pack(side=LEFT)

        # Container4
        # Label do codigo
        self.label_codigo = Label(self.container4,
                                  text='Código:', font=self.fonte_labels, width=10)
        self.label_codigo.pack(side=LEFT)

        # Campo de texto do nome
        self.text_field_codigo = Entry(self.container4)
        self.text_field_codigo['width'] = 30
        self.text_field_codigo['font'] = self.fonte_text_field
        self.text_field_codigo.pack(side=LEFT)

        # Container5
        # Onde os resultados são mostrados
        self.label_result = Label(self.container5, text="")
        self.label_result["font"] = self.fonte_labels
        self.label_result.pack()
        #

        # Container6
        # Botao Inserir Item
        self.button_inserir = Button(self.container6, text='Devolver Item',
                                     font=self.fonte_labels, width=16)
        self.button_inserir['command'] = self.InserirItem
        self.button_inserir.pack(side=LEFT)

        # Botao Pesquisar
        self.button_pesquisar = Button(self.container6, text='Pesquisar',
                                       font=self.fonte_labels, width=16)
        self.button_pesquisar['command'] = self.PesquisarItem
        self.button_pesquisar.pack(side=LEFT)

        # Container7
        # Botao atualizar
        self.button_atualizar = Button(self.container7, text='Atualizar',
                                       font=self.fonte_labels, width=15)
        self.button_atualizar['command'] = self.AtualizarItem
        self.button_atualizar.pack(side=LEFT)

        # Botao retirar
        self.button_retirar = Button(self.container7, text='Retirar',
                                     font=self.fonte_labels, width=15)
        self.button_retirar['command'] = self.RetirarItem
        self.button_retirar.pack(side=LEFT)

        # Create

    def InserirItem(self):
        nome = self.combobox_nome.get()
        codigo = self.text_field_codigo.get()
        categoria = self.selected_categoria.get()

        it(nome, codigo, categoria)

    # Read
    def PesquisarItem(self):
        codigo = self.text_field_codigo.get()
        result = it.pesquisar(codigo)
        self.label_result['text'] = result

    # Update
    def AtualizarItem(self):
        codigo = self.text_field_codigo.get()
        nome = self.combobox_nome.get()
        categoria = self.selected_categoria.get()
        it.atualizar(codigo, nome, categoria)

    # Delete
    def RetirarItem(self):
        codigo = self.text_field_codigo.get()
        it.remover(codigo)


class LoginScreen:

    def __init__(self, master=None):
        # Labels das fontes
        self.fonte_titulo = ('Verdana', '8')
        self.fonte_labels = ('Calibri', '10', 'bold')
        self.fonte_text_field = ('Calibri Light', '10')

        # Criando containers e labels

        # Container 1
        self.container1 = Frame(master)
        self.container1['pady'] = 10
        self.container1.pack()

        # Titulo
        self.titulo = Label(self.container1, text='Bem Vindo:')
        self.titulo['font'] = self.fonte_titulo
        self.titulo.pack()

        # Container 2
        self.container2 = Frame(master)
        self.container2['padx'] = 20
        self.container2['pady'] = 5
        self.container2.pack()

        # Label da matricula do aluno
        self.label_matricula = Label(self.container2,
                                     text='Matrícula:', font=self.fonte_labels, width=10)
        self.label_matricula.pack(side=LEFT)

        # Campo de texto da matricula
        self.text_field_matricula = Entry(self.container2)
        self.text_field_matricula['width'] = 15
        self.text_field_matricula['font'] = self.fonte_text_field
        self.text_field_matricula.pack(side=RIGHT)

        # Container 3
        self.container3 = Frame(master)
        self.container3['padx'] = 30
        self.container3['pady'] = 5
        self.container3.pack()

        # Label do Curso

        self.titulo = Label(self.container3, text='Curso:')
        self.titulo['font'] = self.fonte_labels
        self.titulo.pack(side=LEFT)

        # ComboBox dos cursos

        self.combobox_cursos = ttk.Combobox(self.container3, width=28,
                                            values=['Selecione seu curso',
                                                    'Engenharia Biomédica',
                                                    'Engenharia de Computação',
                                                    'Engenharia de Controle e Automação',
                                                    'Engenharia Elétrica',
                                                    'Engenharia de Produção',
                                                    'Engenharia de Software',
                                                    'Engenharia de Telecomunicações'],
                                            state='readonly', font=self.fonte_text_field)
        self.combobox_cursos.current(0)
        self.combobox_cursos.pack(side=RIGHT)

        # Container 4
        self.container4 = Frame(master)
        self.container4['padx'] = 20
        self.container4['pady'] = 5
        self.container4.pack()

        # Botao login

        self.button_login = Button(self.container4, text='Login',
                                   font=self.fonte_labels, width=15,
                                   command=self.Login)
        self.button_login.pack(side=BOTTOM)

    @staticmethod
    def createNewWindow():
        Toplevel(CRUDScreen(tkinter.Tk()))

    def Login(self):
        auth = Usuario(self.text_field_matricula.get(),
                       self.combobox_cursos.get()).Autenticacao()

        if auth == 0:
            tkinter.messagebox.showwarning(title='Erro', message='Aluno não encontrado! Tente novamente.')
        elif auth == 1:
            self.createNewWindow()
