import tkinter as tk
from tkinter import messagebox as mb

def resposta():
   mb.showerror("Resposta", "Desculpe, nenhuma resposta disponível!")

def verificacao():
   if mb.askyesno('Verificar', 'Realmente quer sair?'):
      mb.showwarning('Yes', 'Ainda não foi implementado')
   else:
      mb.showinfo('No', 'A opção de Sair foi cancelada')

tk.Button(text='Sair', command=verificacao).pack(fill=tk.X)
tk.Button(text='Resposta', command=resposta).pack(fill=tk.X)

tk.mainloop()