import tkinter as tk
from tkinter import messagebox


# ======================================================
# FUNÇÕES DE CÁLCULO
# ======================================================

def converter_para_float(texto):
    """
    Converte texto em float aceitando vírgula ou ponto.
    """
    texto = texto.replace(",", ".")
    return float(texto)


def calcular_preco_final(preco, desconto_percentual):
    """
    Calcula o preço final após aplicar desconto.
    Retorna valor arredondado para 2 casas decimais.
    """
    desconto = preco * (desconto_percentual / 100)
    return round(preco - desconto, 2)


def simbolo_moeda(moeda):
    """
    Retorna o símbolo da moeda selecionada.
    """
    if moeda == "Real":
        return "R$"
    if moeda == "Dólar":
        return "$"
    if moeda == "Euro":
        return "€"
    return ""


# ======================================================
# AÇÃO DO BOTÃO
# ======================================================

def calcular():
    try:
        preco = converter_para_float(entrada_preco.get())
        desconto = converter_para_float(entrada_desconto.get())

        if preco <= 0 or desconto < 0 or desconto > 100:
            raise ValueError

        resultado_final = calcular_preco_final(preco, desconto)
        moeda = moeda_selecionada.get()
        simbolo = simbolo_moeda(moeda)

        resultado_texto.set(f"Preço final: {simbolo} {resultado_final:.2f}")

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite valores válidos.\n"
            "Exemplo: 125,25 ou 125.25\n"
            "Desconto entre 0 e 100."
        )


# ======================================================
# INTERFACE GRÁFICA
# ======================================================

janela = tk.Tk()
janela.title("Calculadora de Preço Final")
janela.geometry("400x360")
janela.resizable(False, False)


# -------------------------
# TÍTULO
# -------------------------

tk.Label(
    janela,
    text="Calculadora de Desconto",
    font=("Arial", 14, "bold")
).pack(pady=15)


# -------------------------
# PREÇO
# -------------------------

tk.Label(janela, text="Preço do produto:").pack()
entrada_preco = tk.Entry(janela, width=30)
entrada_preco.pack(pady=5)


# -------------------------
# DESCONTO
# -------------------------

tk.Label(janela, text="Desconto (%):").pack()
entrada_desconto = tk.Entry(janela, width=30)
entrada_desconto.pack(pady=5)


# -------------------------
# MOEDA
# -------------------------

tk.Label(janela, text="Moeda:").pack(pady=10)

moeda_selecionada = tk.StringVar(value="Real")

tk.Radiobutton(janela, text="Real (R$)", variable=moeda_selecionada, value="Real").pack()
tk.Radiobutton(janela, text="Dólar ($)", variable=moeda_selecionada, value="Dólar").pack()
tk.Radiobutton(janela, text="Euro (€)", variable=moeda_selecionada, value="Euro").pack()


# -------------------------
# BOTÃO
# -------------------------

tk.Button(
    janela,
    text="Calcular",
    command=calcular,
    width=25
).pack(pady=15)


# -------------------------
# RESULTADO
# -------------------------

resultado_texto = tk.StringVar()

tk.Label(
    janela,
    textvariable=resultado_texto,
    font=("Arial", 12, "bold")
).pack(pady=10)


# -------------------------
# LOOP PRINCIPAL
# -------------------------

janela.mainloop()
