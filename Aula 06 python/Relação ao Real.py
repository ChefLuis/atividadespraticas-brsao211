import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime

# ============================
# CONFIGURAÇÕES GERAIS
# ============================
API_BASE = "https://economia.awesomeapi.com.br/json/last"

MOEDAS_FIAT = {
    "Dólar (USD)": "USD",
    "Euro (EUR)": "EUR",
    "Libra (GBP)": "GBP",
    "Iene (JPY)": "JPY",
    "Peso Argentino (ARS)": "ARS",
    "Dólar Canadense (CAD)": "CAD",
    "Dólar Australiano (AUD)": "AUD"
}

CRIPTOS = {
    "Bitcoin (BTC)": "BTC",
    "Ethereum (ETH)": "ETH",
    "Litecoin (LTC)": "LTC",
    "Ripple (XRP)": "XRP"
}

# ============================
# FUNÇÃO DE CONSULTA
# ============================
def consultar_moeda(codigo):
    try:
        url = f"{API_BASE}/{codigo}-BRL"
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        chave = f"{codigo}BRL"
        info = dados[chave]

        resultado_valor.config(text=f"Valor Atual: R$ {info['bid']}")
        resultado_max.config(text=f"Máxima: R$ {info['high']}")
        resultado_min.config(text=f"Mínima: R$ {info['low']}")

        data = datetime.fromtimestamp(int(info['timestamp']))
        resultado_data.config(
            text=f"Atualizado em: {data.strftime('%d/%m/%Y %H:%M:%S')}"
        )

    except Exception:
        messagebox.showerror(
            "Erro",
            "Não foi possível obter os dados da moeda.\nVerifique sua conexão ou a moeda selecionada."
        )

# ============================
# CALLBACKS
# ============================
def consultar_fiat(event=None):
    nome = combo_fiat.get()
    if nome in MOEDAS_FIAT:
        consultar_moeda(MOEDAS_FIAT[nome])

def consultar_cripto(event=None):
    nome = combo_cripto.get()
    if nome in CRIPTOS:
        consultar_moeda(CRIPTOS[nome])

# ============================
# JANELA PRINCIPAL
# ============================
janela = tk.Tk()
janela.title("Consulta de Moedas - BRL")
janela.geometry("520x420")
janela.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

# ============================
# NOTEBOOK (ABAS)
# ============================
notebook = ttk.Notebook(janela)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# ============================
# ABA MOEDAS FIAT
# ============================
aba_fiat = ttk.Frame(notebook)
notebook.add(aba_fiat, text="Moedas Tradicionais")

ttk.Label(
    aba_fiat,
    text="Selecione a moeda:",
    font=("Segoe UI", 11)
).pack(pady=15)

combo_fiat = ttk.Combobox(
    aba_fiat,
    values=list(MOEDAS_FIAT.keys()),
    state="readonly",
    font=("Segoe UI", 11),
    width=30
)
combo_fiat.pack()
combo_fiat.bind("<Return>", consultar_fiat)

ttk.Button(
    aba_fiat,
    text="Consultar",
    command=consultar_fiat
).pack(pady=15)

# ============================
# ABA CRIPTOMOEDAS
# ============================
aba_cripto = ttk.Frame(notebook)
notebook.add(aba_cripto, text="Criptomoedas")

ttk.Label(
    aba_cripto,
    text="Selecione a criptomoeda:",
    font=("Segoe UI", 11)
).pack(pady=15)

combo_cripto = ttk.Combobox(
    aba_cripto,
    values=list(CRIPTOS.keys()),
    state="readonly",
    font=("Segoe UI", 11),
    width=30
)
combo_cripto.pack()
combo_cripto.bind("<Return>", consultar_cripto)

ttk.Button(
    aba_cripto,
    text="Consultar",
    command=consultar_cripto
).pack(pady=15)

# ============================
# RESULTADOS (COMUM)
# ============================
frame_resultado = ttk.LabelFrame(
    janela,
    text="Resultado",
    padding=15
)
frame_resultado.pack(fill="x", padx=15, pady=10)

resultado_valor = ttk.Label(frame_resultado, text="Valor Atual: -")
resultado_valor.pack(anchor="w")

resultado_max = ttk.Label(frame_resultado, text="Máxima: -")
resultado_max.pack(anchor="w")

resultado_min = ttk.Label(frame_resultado, text="Mínima: -")
resultado_min.pack(anchor="w")

resultado_data = ttk.Label(frame_resultado, text="Atualizado em: -")
resultado_data.pack(anchor="w")

# ============================
# LOOP
# ============================
janela.mainloop()

