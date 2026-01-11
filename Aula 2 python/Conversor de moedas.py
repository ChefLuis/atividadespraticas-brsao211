import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/BRL"
taxas = {}

# Mapeamento código -> nome completo
NOMES_MOEDAS = {
    "USD": "Dólar Americano",
    "EUR": "Euro",
    "GBP": "Libra Esterlina",
    "JPY": "Iene Japonês",
    "ARS": "Peso Argentino",
    "CAD": "Dólar Canadense",
    "AUD": "Dólar Australiano",
    "CHF": "Franco Suíço",
    "CNY": "Yuan Chinês"
}

def carregar_moedas():
    global taxas
    try:
        resposta = requests.get(API_URL, timeout=5)
        dados = resposta.json()
        taxas = dados["rates"]

        menu["menu"].delete(0, "end")

        for codigo in sorted(taxas.keys()):
            nome = NOMES_MOEDAS.get(codigo, "Moeda Internacional")
            label = f"{codigo} - {nome}"

            menu["menu"].add_command(
                label=label,
                command=lambda c=codigo: moeda_var.set(c)
            )

        messagebox.showinfo("Sucesso", "Moedas carregadas com sucesso.")

    except:
        messagebox.showerror(
            "Erro",
            "Não foi possível carregar as taxas de câmbio."
        )

def converter():
    try:
        valor = float(entry_valor.get())
        codigo = moeda_var.get()

        if codigo == "":
            messagebox.showwarning("Aviso", "Selecione uma moeda.")
            return

        convertido = valor * taxas[codigo]
        nome = NOMES_MOEDAS.get(codigo, "Moeda Internacional")

        resultado.config(
            text=f"{valor:.2f} BRL = {convertido:.2f} {codigo}\n({nome})"
        )

    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido.")
    except KeyError:
        messagebox.showwarning("Aviso", "Carregue as moedas primeiro.")

# Janela
janela = tk.Tk()
janela.title("Conversor Universal de Moedas")
janela.geometry("420x350")

tk.Label(janela, text="Valor em Reais (BRL):").pack(pady=5)
entry_valor = tk.Entry(janela)
entry_valor.pack(pady=5)

tk.Button(janela, text="Carregar Moedas", command=carregar_moedas).pack(pady=5)

tk.Label(janela, text="Converter para:").pack(pady=5)

moeda_var = tk.StringVar()
menu = tk.OptionMenu(janela, moeda_var, "")
menu.pack(pady=5)

tk.Button(janela, text="Converter", command=converter).pack(pady=10)

resultado = tk.Label(janela, text="", font=("Arial", 12), justify="center")
resultado.pack(pady=10)

janela.mainloop()
