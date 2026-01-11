import tkinter as tk

def calcular_total():
    try:
        nome = entry_nome.get()
        preco = float(entry_preco.get())
        quantidade = int(entry_quantidade.get())

        total = preco * quantidade

        resultado.config(
            text=(
                f"Produto: {nome}\n"
                f"Preço unitário: R$ {preco:.2f}\n"
                f"Quantidade: {quantidade}\n"
                f"Preço total: R$ {total:.2f}"
            )
        )
    except ValueError:
        resultado.config(text="Preencha os campos corretamente")

# Janela
janela = tk.Tk()
janela.title("Calculadora de Preço Total")

# Nome do produto
tk.Label(janela, text="Nome do produto").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()
entry_nome.insert(0, "Cadeira Infantil")

# Preço unitário
tk.Label(janela, text="Preço unitário (R$)").pack()
entry_preco = tk.Entry(janela)
entry_preco.pack()
entry_preco.insert(0, "12.40")

# Quantidade
tk.Label(janela, text="Quantidade").pack()
entry_quantidade = tk.Entry(janela)
entry_quantidade.pack()
entry_quantidade.insert(0, "3")

# Botão
tk.Button(janela, text="Calcular Preço Total", command=calcular_total).pack(pady=10)
# Resultado
resultado = tk.Label(janela, text="", justify="left")
resultado.pack(pady=5)

# Mostrar janela
janela.mainloop()
