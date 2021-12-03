# Projeto-CRUD
Projeto de CRUD em Python utilizando Neo4J (Finalizado)

-Este projeto implementa uma interface gráfica utilizando a biblioteca Tkinter do Python para um software de controle de estoque para um almoxarifado.

1- A primeira tela faz o login do Aluno utilizando suas credenciais de número de matrícula e curso.

![Alt text](Screenshots/sc1.png?raw=true "Tela Login")
![Alt text](Screenshots/sc2.png?raw=true "Autenticação")

2-Feito o login na tela anterior, uma segunda tela abre mostrando os campos e botões para acesso às informações do almoxarifado.


![Alt text](Screenshots/sc3.png?raw=true "Tela Menu")

3 - O planjamento das funções básicas foram pensadas dentro de um flowchart

![Alt text](Screenshots/flowchart.png?raw=true "Flowchart")

4 - O principal problema a ser resolvido é uma janela indesejada em branco sendo aberta junto com o acionamento do botão de login, já que o mesmo faz com que 
a janela do menu seja aberta

# Observações:

Execução:
pip install neo4j
pip install names

Deve-se alterar as credenciais de conexão antes de realizar testes

1 - Executar main.py (há um script comentado aqui para caso queira um DB simulando diversos dados)

Problemas:
Erro de atributo do Tkinter para a segunda tela ainda permanece
