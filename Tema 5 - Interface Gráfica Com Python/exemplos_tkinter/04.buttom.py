import tkinter as tk
contador = 0
def contador_label(lblRotulo):
    def funcao_contar():
        global contador
        contador += 1
        lblRotulo.config(text=str(contador))
        lblRotulo.after(1000, funcao_contar)

    funcao_contar()

janela = tk.Tk()
janela.title("Contagem dos Segundos")
lblRotulo = tk.Label(janela, fg="green")
lblRotulo.pack()
contador_label(lblRotulo)
btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem', width=50, command=janela.destroy)
btnAcao.pack()
janela.mainloop()