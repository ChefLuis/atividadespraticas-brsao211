import tkinter as tk
from tkinter import messagebox


def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    return valor_conta * (porcentagem_gorjeta / 100)


def on_calcular():
    try:
        valor_conta = float(entry_valor.get())
        porcentagem = float(entry_porcentagem.get())

        if valor_conta < 0 or porcentagem < 0:
            raise ValueError

        gorjeta = calcular_gorjeta(valor_conta, porcentagem)
        resultado_var.set(f"Gorjeta: R$ {gorjeta:.2f}")

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Informe valores numéricos válidos e positivos."
        )


# Janela principal
janela = tk.Tk()
janela.title("Calculadora de Gorjeta")
janela.geometry("300x220")
janela.resizable(False, False)

# Variável para resultado
resultado_var = tk.StringVar()

# Layout
tk.Label(janela, text="Valor da conta (R$):").pack(pady=5)
entry_valor = tk.Entry(janela)
entry_valor.pack()

tk.Label(janela, text="Porcentagem da gorjeta (%):").pack(pady=5)
entry_porcentagem = tk.Entry(janela)
entry_porcentagem.pack()

tk.Button(
    janela,
    text="Calcular Gorjeta",
    command=on_calcular
).pack(pady=15)

tk.Label(
    janela,
    textvariable=resultado_var,
    font=("Arial", 12, "bold")
).pack()

# Loop principal
janela.mainloop()
