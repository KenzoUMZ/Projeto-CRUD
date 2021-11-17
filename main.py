import tkinter
from interface import LoginScreen
from setup import insert_all  # Esse arquivo serve exclusivamente pra inserir dados hipotéticos no DB

# insert_all()
root = tkinter.Tk()
LoginScreen(root)
root.title('Almoxarifado Inatel')
root.mainloop()
