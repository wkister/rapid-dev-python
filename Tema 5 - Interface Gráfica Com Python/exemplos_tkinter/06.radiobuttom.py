import tkinter as tk

janela = tk.Tk()
v = tk.IntVar()

tk.Label(
	janela,
	text="""Escolha uma linguagem de programação:""",
	justify=tk.LEFT,
	padx=20,
).pack()

tk.Radiobutton(janela, text="python", padx=25, variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(janela, text="C++", padx=25, variable=v, value=2).pack(anchor=tk.W)


def mostrar_selecao():
	"""Handler simples para mostrar a seleção atual da variável `v`."""
	selecionado = v.get()
	# Mapeia valores para nomes legíveis
	nomes = {1: "python", 2: "C++"}
	print("Selecionado:", nomes.get(selecionado, f"(nenhum: {selecionado})"))


tk.Button(janela, text="Mostrar seleção", command=mostrar_selecao).pack(pady=6)

janela.mainloop()