import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("titulo da tela")
root.geometry('600x400+200+200')
root.resizable(False,False)
#criando a label
label=ttk.Label(root, text'exemplo de texto')
label.pack()
#botão
exit_B=ttk.Button ( 
root,
text='fechar',
command=lambda:root.quit()
)
exit_B.pack(
  ipadx=5,
  ipady=5,
  expand=True
)
root.mainloop()