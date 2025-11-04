"""Protótipo de Sistema de Pedidos para Lanchonete.

Este módulo implementa uma interface gráfica simples para um sistema de
pedidos de lanchonete chamado 'Sabor Rápido'. Permite aos usuários:
- Selecionar itens de um menu
- Adicionar itens ao pedido
- Visualizar pedidos atuais
- Finalizar pedidos com cálculo do total
- Gerenciar o menu (adicionar novos itens)

O sistema usa Tkinter para a interface gráfica e mantém os dados em memória.
"""

import tkinter as tk
from tkinter import messagebox


class SaborRapidoApp:
    """Interface gráfica principal do sistema Sabor Rápido.
    
    Esta classe gerencia a interface e a lógica do sistema de pedidos,
    incluindo o menu de itens, lista de pedidos e cálculo de valores.
    
    Attributes:
        root: Janela principal do Tkinter
        itens_menu (dict): Dicionário com itens e preços do menu
        pedido (list): Lista de itens no pedido atual
        listbox: Widget Tkinter para exibir o menu
        entry_item: Campo para nome do novo item
        entry_preco: Campo para preço do novo item
    """
    
    def __init__(self, root):
        """Inicializa a aplicação Sabor Rápido.
        
        Args:
            root: Instância de tk.Tk para a janela principal
        """
        self.root = root
        self.root.title("Sabor Rápido - Protótipo")
        self.root.geometry("400x500")

        self.itens_menu = {"Hambúrguer": 10.00, "Batata Frita": 5.00, "Refrigerante": 3.00}
        self.pedido = []

        tk.Label(root, text="Selecione os itens do pedido:", font=("Arial", 12)).pack(pady=10)
            
        self.listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, font=("Arial", 10))
        self.atualizar_lista_menu()
        self.listbox.pack()

    def atualizar_lista_menu(self):
        """Atualiza a exibição do menu na interface.
        
        Limpa e repopula a listbox com os itens atuais do menu.
        Também cria os botões de ação principais se ainda não existirem.
        """
        self.listbox.delete(0, tk.END)  # Limpa a lista atual
        for item in self.itens_menu.keys():
            self.listbox.insert(tk.END, item)

        # Cria os botões principais de interação
        tk.Button(root, text="Adicionar ao Pedido", command=self.adicionar_pedido).pack(pady=5)
        tk.Button(root, text="Visualizar Pedido", command=self.visualizar_pedido).pack(pady=5)

    def adicionar_pedido(self):
        """Adiciona os itens selecionados ao pedido atual.
        
        Pega todos os itens selecionados na listbox e os adiciona
        à lista de pedidos. Exibe uma mensagem de confirmação.
        """
        selecionados = self.listbox.curselection()
        for index in selecionados:
            item = self.listbox.get(index)
            self.pedido.append(item)
        messagebox.showinfo("Pedido", "Itens adicionados com sucesso!")

    def visualizar_pedido(self):
        """Exibe os itens do pedido atual.
        
        Mostra uma mensagem com todos os itens no pedido atual.
        Se não houver itens, exibe uma mensagem apropriada.
        Também adiciona um botão para finalizar o pedido.
        """
        if not self.pedido:
            messagebox.showinfo("Pedido", "Nenhum item no pedido.")
            return
        pedido_texto = "\n".join(self.pedido)
        messagebox.showinfo("Pedido Atual", f"Itens no pedido:\n{pedido_texto}")

        # Adiciona botão para finalização após visualizar
        tk.Button(root, text="Finalizar Pedido", command=self.finalizar_pedido).pack(pady=10)

    def finalizar_pedido(self):
        """Finaliza o pedido atual e calcula o total.
        
        Calcula o valor total do pedido baseado nos preços do menu,
        exibe o total, limpa o pedido atual e prepara a interface
        para adicionar novos itens ao menu.
        """
        if not self.pedido:
            messagebox.showinfo("Pedido", "Adicione itens antes de finalizar o pedido.")
            return
        
        # Calcula o total e exibe
        total = sum(self.itens_menu[item] for item in self.pedido)
        messagebox.showinfo("Total", f"Total do pedido: R$ {total:.2f}\nPedido finalizado!")
        self.pedido.clear()  # Limpa o pedido atual

        # Prepara interface para adicionar novos itens ao menu
        tk.Label(root, text="Adicionar Novo Item ao Menu:", font=("Arial", 12)).pack(pady=10)
        self.entry_item = tk.Entry(root, font=("Arial", 10))
        self.entry_item.pack()
        self.entry_preco = tk.Entry(root, font=("Arial", 10))
        self.entry_preco.pack()
        tk.Button(root, text="Adicionar Item", command=self.adicionar_item_menu).pack(pady=5)

    def adicionar_item_menu(self):
        """Adiciona um novo item ao menu.
        
        Obtém nome e preço dos campos de entrada, valida os dados
        e adiciona o novo item ao menu se os dados forem válidos.
        Limpa os campos após adicionar com sucesso.
        
        Raises:
            ValueError: Se o preço não puder ser convertido para float.
        """
        item = self.entry_item.get().strip()
        preco = self.entry_preco.get().strip()
        
        if item and preco:
            try:
                # Tenta converter o preço para float e adiciona ao menu
                self.itens_menu[item] = float(preco)
                self.atualizar_lista_menu()
                
                # Limpa os campos de entrada
                self.entry_item.delete(0, tk.END)
                self.entry_preco.delete(0, tk.END)
                
                messagebox.showinfo("Sucesso", "Item adicionado ao menu com sucesso!")
            except ValueError:
                messagebox.showerror("Erro", "Preço inválido. Digite um valor numérico.")
        else:
            messagebox.showerror("Erro", "Preencha ambos os campos corretamente.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SaborRapidoApp(root)
    root.mainloop()
