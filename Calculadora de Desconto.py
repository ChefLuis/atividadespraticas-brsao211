import tkinter as tk
from tkinter import messagebox

def calcular_desconto():
    try:
        produto = entry_produto.get()
        preco = float(entry_preco.get())
        desconto = float(entry_desconto.get())

        if produto == "":
            messagebox.showwarning("Aviso", "Informe o nome do produto.")
            return

        valor_desconto = preco * (desconto / 100)
        preco_final = preco - valor_desconto

        resultado.config(
            text=(
                f"Produto: {produto}\n"
                f"Preço Original: R$ {preco:.2f}\n"
                f"Desconto: {desconto:.1f}%\n\n"
                f"Valor do Desconto: R$ {valor_desconto:.2f}\n"
                f"Preço Final: R$ {preco_final:.2f}"
            )
        )

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Preço e desconto devem ser valores numéricos."
        )

# Janela
janela = tk.Tk()
janela.title("Calculadora de Desconto")
janela.geometry("420x360")

# Campos
tk.Label(janela, text="Nome do Produto:").pack(pady=4)
entry_produto = tk.Entry(janela, width=30)
entry_produto.pack(pady=4)

tk.Label(janela, text="Preço Original (R$):").pack(pady=4)
entry_preco = tk.Entry(janela)
entry_preco.pack(pady=4)

tk.Label(janela, text="Desconto (%):").pack(pady=4)
entry_desconto = tk.Entry(janela)
entry_desconto.pack(pady=4)

# Botão
tk.Button(janela, text="Calcular Desconto", command=calcular_desconto).pack(pady=10)

# Resultado
resultado = tk.Label(janela, text="", font=("Arial", 11), justify="left")
resultado.pack(pady=10)

janela.mainloop()
