import tkinter
from tkinter import *
from tkinter import ttk
from item import Item as it


class CRUDScreen(Frame):

    def __init__(self, master, **kwargs):
        ttk.Frame.__init__(self, master, **kwargs)
        # Labels das fontes
        super().__init__(master, **kwargs)
        self.fonte_titulo = ('Verdana', '8')
        self.fonte_labels = ('Calibri', '10', 'bold')
        self.fonte_text_field = ('Calibri Light', '10')

        # Criando containers e labels

        # Container 1
        self.container1 = Frame(master)
        self.container1['pady'] = 10
        self.container1.pack()

        # Titulo
        self.titulo = Label(self.container1, text='Menu Almoxarifado:')
        self.titulo['font'] = self.fonte_titulo
        self.titulo.pack()

        # Container 2
        self.container2 = Frame(master)
        self.container2['padx'] = 20
        self.container2['pady'] = 5
        self.container2.pack()

        # Label do nome do item
        self.label_nome = Label(self.container2,
                                text='Nome:', font=self.fonte_labels, width=10)
        self.label_nome.pack(side=LEFT)

        # Campo de texto do nome
        self.text_field_nome = Entry(self.container2)
        self.text_field_nome['width'] = 30
        self.text_field_nome['font'] = self.fonte_text_field
        self.text_field_nome.pack(side=LEFT)

        # Container 3
        self.container3 = Frame(master)
        self.container3['padx'] = 20
        self.container3['pady'] = 5
        self.container3.pack()

        # Label do codigo
        self.label_codigo = Label(self.container3,
                                  text='Código:', font=self.fonte_labels, width=10)
        self.label_codigo.pack(side=LEFT)

        # Campo de texto do nome
        self.text_field_codigo = Entry(self.container3)
        self.text_field_codigo['width'] = 30
        self.text_field_codigo['font'] = self.fonte_text_field
        self.text_field_codigo.pack(side=LEFT)

        # Container 4
        self.container4 = Frame(master)
        self.container4['padx'] = 20
        self.container4['pady'] = 5
        self.container4.pack()

        # Label do categoria
        self.label_categoria = Label(self.container4,
                                     text='Categoria:', font=self.fonte_labels, width=10)
        self.label_categoria.pack(side=LEFT)

        # ComboBox da categoria

        self.combobox_categoria = ttk.Combobox(self.container4, width=28,
                                               values=['Selecione uma categoria',
                                                       'Ferramenta',
                                                       'Dispositivo'],
                                               state='readonly', font=self.fonte_text_field)
        self.combobox_categoria.current(0)
        self.combobox_categoria.pack(side=LEFT)

        # Container 5
        self.container5 = Frame(master)
        self.container5['padx'] = 20
        self.container5['pady'] = 5
        self.container5.pack()

        # Botao Inserir Item
        self.button_inserir = Button(self.container5, text='Inserir no Estoque',
                                     font=self.fonte_labels, width=15)
        self.button_inserir['command'] = self.InserirItem
        self.button_inserir.pack(side=LEFT)

        # Botao Pesquisar
        self.button_pesquisar = Button(self.container5, text='Pesquisar',
                                       font=self.fonte_labels, width=15)
        self.button_pesquisar['command'] = self.PesquisarItem
        self.button_pesquisar.pack(side=LEFT)

        # Container 6
        self.container6 = Frame(master)
        self.container6['padx'] = 20
        self.container6['pady'] = 5
        self.container6.pack()

        # Botao atualizar
        self.button_atualizar = Button(self.container6, text='Atualizar',
                                       font=self.fonte_labels, width=15)
        self.button_atualizar['command'] = self.AtualizarItem
        self.button_atualizar.pack(side=LEFT)

        # Botao retirar
        self.button_retirar = Button(self.container6, text='Retirar',
                                     font=self.fonte_labels, width=15)
        self.button_retirar['command'] = self.RetirarItem
        self.button_retirar.pack(side=LEFT)

        # Container 7
        self.container7 = Frame(master)
        self.container7['padx'] = 20
        self.container7['pady'] = 5
        self.container7.pack()

        # Onde os resultados são mostrados
        self.label_result = Label(self.container7, text="")
        self.label_result["font"] = self.fonte_labels
        self.label_result.pack()

    # Create
    def InserirItem(self):
        nome = self.text_field_nome.get()
        codigo = self.text_field_codigo.get()
        categoria = self.combobox_categoria.get()

        it(nome, codigo, categoria)

    # Read
    def PesquisarItem(self):
        codigo = self.text_field_codigo.get()
        result = it.pesquisar(codigo)
        self.label_result['text'] = result

    # Update
    def AtualizarItem(self):
        codigo = self.text_field_codigo.get()
        nome = self.text_field_nome.get()
        categoria = self.combobox_categoria.get()
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
        self.label_nome = Label(self.container2,
                                text='Matrícula:', font=self.fonte_labels, width=10)
        self.label_nome.pack(side=LEFT)

        # Campo de texto do nome
        self.text_field_nome = Entry(self.container2)
        self.text_field_nome['width'] = 30
        self.text_field_nome['font'] = self.fonte_text_field
        self.text_field_nome.pack(side=LEFT)

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

        self.combobox_categoria = ttk.Combobox(self.container3, width=28,
                                               values=['Selecione seu curso',
                                                       'Engenharia Biomédica',
                                                       'Engenharia de Computação',
                                                       'Engenharia de Controle e Automação',
                                                       'Engenharia Elétrica'
                                                       'Engenharia de Produção',
                                                       'Engenharia de Software',
                                                       'Engenharia de Telecomunicações'],
                                               state='readonly', font=self.fonte_text_field)
        self.combobox_categoria.current(0)
        self.combobox_categoria.pack(side=RIGHT)

        # Container 4
        self.container4 = Frame(master)
        self.container4['padx'] = 20
        self.container4['pady'] = 5
        self.container4.pack()

        def createNewWindow():
            Toplevel(CRUDScreen(Tk()))

        # Botao login
        self.button_login = Button(self.container4, text='Login',
                                   font=self.fonte_labels, width=15,
                                   command=lambda: [createNewWindow()])

        self.button_login.pack(side=LEFT)
