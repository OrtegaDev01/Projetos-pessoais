import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Minha Primeira Tela")  # Título da janela
janela.geometry("780x400")  # Define o tamanho da janela (largura x altura)

# Cria um rótulo (texto) dentro da janela
rotulo = tk.Label(janela, text="Bem-vindo à minha tela!", font=("Arial", 16))
rotulo.pack(pady=20)  # Adiciona o rótulo com um espaçamento vertical

# Cria um botão dentro da janela
botao = tk.Button(janela, text="Clique aqui", font=("Cascadia code", 12), command=lambda: print("Botão clicado!"))
botao.pack(pady=10)

# Executa a aplicação
janela.mainloop()