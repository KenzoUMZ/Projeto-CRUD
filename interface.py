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
        self.container1['padx'] = 120
        self.container1.configure(bg='#808080')
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2['padx'] = 33
        self.container2['pady'] = 5
        self.container2.configure(bg='#808080')
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3['padx'] = 33
        self.container3['pady'] = 5
        self.container3.configure(bg='#808080')
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4['padx'] = 35
        self.container4['pady'] = 5
        self.container4.configure(bg='#808080')
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5['padx'] = 35
        self.container5['pady'] = 5
        self.container5.configure(bg='#808080')
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6['padx'] = 35
        self.container6['pady'] = 5
        self.container6.configure(bg='#808080')
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7['padx'] = 35
        self.container7['pady'] = 5
        self.container7.configure(bg='#808080')
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8['padx'] = 58
        self.container8['pady'] = 5
        self.container8.configure(bg='#808080')
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9['padx'] = 65
        self.container9['pady'] = 5
        self.container9.configure(bg='#808080')
        self.container9.pack()

        # Container1

        # Titulo
        self.titulo = Label(self.container1, text='Menu Almoxarifado:')
        self.titulo['font'] = self.fonte_titulo
        self.titulo.configure(bg='#808080', fg='#FFFFFF')
        self.titulo.pack()

        # Container2
        # Label das categorias
        self.label_categoria = Label(self.container2,
                                     text='Categorias:',
                                     font=self.fonte_labels,
                                     width=10)
        self.label_categoria.configure(bg='#808080', fg='#FFFFFF')
        self.label_categoria.pack(side=LEFT)

        # Radio buttons das categorias
        self.combobox_categoria = ttk.Combobox(self.container2,
                                               width=28,
                                               values=['Selecione uma categoria',
                                                       'Componente', 'Ferramenta'],
                                               state='readonly',
                                               font=self.fonte_text_field)
        self.combobox_categoria.current(0)
        self.combobox_categoria.pack(side=LEFT)

        # Container3
        # Label do nome do item
        self.label_nome = Label(self.container3,
                                text='Item:', font=self.fonte_labels, width=10)
        self.label_nome.configure(bg='#808080', fg='#FFFFFF')

        self.label_nome.pack(side=LEFT)

        # ComboBox do nome do item

        self.componentes_ferramentas = ['Resistor', 'Potenciômetro',
                                        'Capacitor', 'Diodo', 'Led',
                                        'Bateria', 'Multímetro', 'Fita Isolante',
                                        'Tesoura', 'Jacarés', 'Gerador de Funções',
                                        'Osciloscópio']

        self.combobox_nome = ttk.Combobox(self.container3, width=28,
                                          values=self.componentes_ferramentas,
                                          state='readonly',
                                          font=self.fonte_text_field)
        self.combobox_nome.current(0)
        self.combobox_nome.pack(side=LEFT)

        # Container4
        # Label do codigo
        self.label_codigo = Label(self.container4,
                                  text='Código:',
                                  font=self.fonte_labels,
                                  width=10)
        self.label_codigo.configure(bg='#808080', fg='#FFFFFF')
        self.label_codigo.pack(side=LEFT)

        # Campo de texto do código
        self.text_field_codigo = Entry(self.container4)
        self.text_field_codigo['width'] = 30
        self.text_field_codigo['font'] = self.fonte_text_field
        self.text_field_codigo.pack(side=LEFT)

        # Container 5
        self.label_especificacao = Label(self.container5,
                                         text='Especificação:',
                                         font=self.fonte_labels,
                                         width=10)
        self.label_especificacao.configure(bg='#808080', fg='#FFFFFF')
        self.label_especificacao.pack(side=LEFT)

        # Campo de texto da especificação
        self.text_field_especificacao = Entry(self.container5)
        self.text_field_especificacao['width'] = 30
        self.text_field_especificacao['font'] = self.fonte_text_field
        self.text_field_especificacao.pack(side=LEFT)

        # Label da prateleira
        self.label_prateleira = Label(self.container6,
                                      text='Prateleira:',
                                      font=self.fonte_labels,
                                      width=10)
        self.label_prateleira.configure(bg='#808080', fg='#FFFFFF')
        self.label_prateleira.pack(side=LEFT)

        # Numero da prateleira
        self.text_field_prateleira = Entry(self.container6)
        self.text_field_prateleira['width'] = 30
        self.text_field_prateleira['font'] = self.fonte_labels
        self.text_field_prateleira.pack(side=LEFT)

        # Label do andar
        self.label_andar = Label(self.container7,
                                 text='Andar:',
                                 font=self.fonte_labels,
                                 width=10)
        self.label_andar.configure(bg='#808080', fg='#FFFFFF')
        self.label_andar.pack(side=LEFT)

        self.text_field_andar = Entry(self.container7)
        self.text_field_andar['width'] = 30
        self.text_field_andar['font'] = self.fonte_text_field
        self.text_field_andar.pack(side=LEFT)

        # Container7

        # Botao Inserir Item
        self.button_inserir = Button(self.container8, text='Devolver Item',
                                     font=self.fonte_labels, width=16)
        self.button_inserir['command'] = self.InserirItem
        self.button_inserir.pack(side=LEFT)

        # Botao Pesquisar
        self.button_pesquisar = Button(self.container8, text='Pesquisar',
                                       font=self.fonte_labels, width=16)
        self.button_pesquisar['command'] = self.PesquisarItem
        self.button_pesquisar.pack(side=LEFT)

        # Container8
        # Botao atualizar
        self.button_atualizar = Button(self.container9, text='Atualizar',
                                       font=self.fonte_labels, width=15)
        self.button_atualizar['command'] = self.AtualizarItem
        self.button_atualizar.pack(side=LEFT)

        # Botao retirar
        self.button_retirar = Button(self.container9, text='Retirar',
                                     font=self.fonte_labels, width=15)
        self.button_retirar['command'] = self.RetirarItem
        self.button_retirar.pack(side=LEFT)

    def InserirItem(self):
        nome = self.combobox_nome.get()
        codigo = self.text_field_codigo.get()
        categoria = self.combobox_categoria.get()
        especificacao = self.text_field_especificacao.get()
        prat = self.text_field_prateleira.get()
        andar = self.text_field_andar.get()

        it(nome, codigo, categoria, especificacao, prat, andar)

    # Read
    def PesquisarItem(self):
        nome = self.combobox_nome.get()
        categoria = self.combobox_categoria.get()
        codigo = self.text_field_codigo.get()
        espec = self.text_field_especificacao.get()
        prat = self.text_field_prateleira.get()
        andar = self.text_field_andar.get()
        result = it.pesquisar(nome, codigo, categoria, espec, prat, andar)
        tkinter.messagebox.showinfo(title='Sua Busca', message=result)

    # Update
    def AtualizarItem(self):
        nome = self.combobox_nome.get()
        categoria = self.combobox_categoria.get()
        codigo = self.text_field_codigo.get()
        espec = self.text_field_especificacao.get()
        output = it.atualizar(codigo, nome, categoria, espec)
        if output == 1:
            tkinter.messagebox.showinfo(title='Sua Busca',
                                        message=f'Item {codigo} atualizado!')
        else:
            tkinter.messagebox.showerror(title='Sua Busca',
                                         message='Não foi possível atualizar este item')

    # Delete
    def RetirarItem(self):
        codigo = self.text_field_codigo.get()
        output = it.remover(codigo)

        if output == 1:
            tkinter.messagebox.showinfo(title='Sua Busca',
                                        message=f'Item {codigo} retirado!')
        else:
            tkinter.messagebox.showerror(title='Sua Busca',
                                         message='Não foi possível retirar este item')

    # Era pra mudar a lista aqui
    def change_list_item(self):
        print('passou pelo metodo')
        print(self.combobox_categoria.get())


class LoginScreen:

    def __init__(self, master=None):
        # Labels das fontes
        self.fonte_titulo = ('Ubuntu', '13', 'bold')
        self.fonte_labels = ('Ubuntu', '10', 'bold')
        self.fonte_text_field = ('Calibri Light', '10')

        # Criando containers e labels

        # Container 1
        self.container1 = Frame(master)
        self.container1['pady'] = 10
        self.container1.pack()
        self.container1.configure(bg='#856ff8')

        # Titulo
        self.titulo = Label(self.container1, text='Bem Vindo!')
        self.titulo['font'] = self.fonte_titulo
        self.titulo.configure(bg='#856ff8', fg='#FFFFFF')
        self.titulo.pack()

        # Container 2
        self.container2 = Frame(master)
        self.container2['padx'] = 20
        self.container2['pady'] = 5
        self.container2.configure(bg='#856ff8')

        self.container2.pack()

        # Label da matricula do aluno
        self.label_matricula = Label(self.container2,
                                     text='Matrícula:',
                                     font=self.fonte_labels,
                                     width=10)
        self.label_matricula.configure(bg='#856ff8', fg='#FFFFFF')
        self.label_matricula.pack(side=LEFT)

        # Campo de texto da matricula
        self.text_field_matricula = Entry(self.container2)
        self.text_field_matricula['width'] = 20
        self.text_field_matricula['font'] = self.fonte_text_field
        self.text_field_matricula.pack(side=LEFT, padx=26)

        # Container 3
        self.container3 = Frame(master)
        self.container3['padx'] = 30
        self.container3['pady'] = 5
        self.container3.configure(bg='#856ff8')
        self.container3.pack()

        # Label do Curso

        self.titulo = Label(self.container3, text='Curso:')
        self.titulo['font'] = self.fonte_labels
        self.titulo.configure(bg='#856ff8', fg='#FFFFFF')
        self.titulo.pack(side=LEFT)

        # ComboBox dos cursos

        self.combobox_cursos = ttk.Combobox(self.container3, width=28,
                                            values=['Selecione seu curso',
                                                    'Engenharia Biomédica',
                                                    'Engenharia de Computação',
                                                    'Engenharia de Controle' +
                                                    ' e Automação',
                                                    'Engenharia Elétrica',
                                                    'Engenharia de Produção',
                                                    'Engenharia de Software',
                                                    'Engenharia de Telecomunicações'],
                                            state='readonly',
                                            font=self.fonte_text_field)
        self.combobox_cursos.current(0)
        self.combobox_cursos.pack(side=RIGHT)

        # Container 4
        self.container4 = Frame(master)
        self.container4['padx'] = 20
        self.container4['pady'] = 5
        self.container4.configure(bg='#856ff8')

        self.container4.pack()

        # Botao login
        self.button_login = Button(self.container4, text='Login',
                                   font=self.fonte_text_field, width=5,
                                   command=self.Login)
        self.button_login.pack(side=BOTTOM)

    @staticmethod
    def createNewWindow():
        Toplevel(CRUDScreen(tkinter.Tk()))

    def Login(self):
        auth = Usuario(self.text_field_matricula.get(),
                       self.combobox_cursos.get()).Autenticacao()

        if auth == 0:
            tkinter.messagebox.showwarning(title='Erro',
                                           message='Aluno não encontrado!' +
                                                   'Tente novamente.')
        else:
            tkinter.messagebox.showinfo(title='Inatel',
                                        message=f'Bem vindo(a) {auth}')
            self.createNewWindow()
