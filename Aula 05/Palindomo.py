import tkinter as tk
from tkinter import messagebox
import re


# ======================================================
# FUNÇÃO PRINCIPAL
# ======================================================

def verificar_palindromo(texto):
    """
    Verifica se uma palavra ou frase é um palíndromo.
    Ignora espaços, pontuação e diferenças entre maiúsculas e minúsculas.
    Retorna 'Sim' ou 'Não'.
    """

    texto = texto.lower()
    texto_limpo = re.sub(r'[^a-z0-9]', '', texto)

    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"


# ======================================================
# AÇÃO DO BOTÃO
# ======================================================

def verificar():
    """
    Função chamada ao clicar no botão.
    """

    texto_digitado = entrada_texto.get()

    if not texto_digitado.strip():
        messagebox.showerror(
            "Erro",
            "Digite uma palavra ou frase."
        )
        return

    resultado = verificar_palindromo(texto_digitado)
    resultado_texto.set(f"Palíndromo: {resultado}")


# ======================================================
# INTERFACE GRÁFICA
# ======================================================

janela = tk.Tk()
janela.title("Verificador de Palíndromo")
janela.geometry("400x260")
janela.resizable(False, False)


# -------------------------
# TÍTULO
# -------------------------

tk.Label(
    janela,
    text="Verificador de Palíndromo",
    font=("Arial", 14, "bold")
).pack(pady=15)


# -------------------------
# ENTRADA
# -------------------------

tk.Label(
    janela,
    text="Digite uma palavra ou frase:"
).pack()

entrada_texto = tk.Entry(janela, width=40)
entrada_texto.pack(pady=8)


# -------------------------
# BOTÃO
# -------------------------

tk.Button(
    janela,
    text="Verificar",
    command=verificar,
    width=25
).pack(pady=10)


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
