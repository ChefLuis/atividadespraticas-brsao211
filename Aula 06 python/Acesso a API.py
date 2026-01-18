import tkinter as tk
from tkinter import messagebox
import requests


# ======================================================
# CAMADA DE SERVIÇO (API)
# ======================================================

def buscar_usuario():
    """
    Consome a API Random User e retorna nome, email e pais.
    Lanca RuntimeError em caso de falha.
    """

    url = "https://randomuser.me/api/"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()

        dados = resposta.json()
        usuario = dados["results"][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario["email"]
        pais = usuario["location"]["country"]

        return nome, email, pais

    except requests.exceptions.RequestException:
        raise RuntimeError("Falha na conexao com a API")

    except (KeyError, IndexError):
        raise RuntimeError("Dados retornados invalidos")


# ======================================================
# CAMADA DE CONTROLE (GUI)
# ======================================================

def acao_buscar():
    """
    Funcao acionada pelo botao.
    Atualiza a interface ou mostra erro.
    """

    try:
        nome, email, pais = buscar_usuario()

        lbl_nome_valor.config(text=nome)
        lbl_email_valor.config(text=email)
        lbl_pais_valor.config(text=pais)

    except RuntimeError as erro:
        messagebox.showerror(
            "Erro",
            str(erro)
        )


# ======================================================
# INTERFACE GRAFICA
# ======================================================

janela = tk.Tk()
janela.title("Usuário Aleatório - API")
janela.geometry("420x260")
janela.resizable(False, False)

tk.Label(
    janela,
    text="Usuário Fictício Aleatório",
    font=("Arial", 14, "bold")
).pack(pady=15)

# Nome
tk.Label(janela, text="Nome:").pack(anchor="w", padx=40)
lbl_nome_valor = tk.Label(janela, text="-")
lbl_nome_valor.pack(anchor="w", padx=40)

# Email
tk.Label(janela, text="E-mail:").pack(anchor="w", padx=40)
lbl_email_valor = tk.Label(janela, text="-")
lbl_email_valor.pack(anchor="w", padx=40)

# Pais
tk.Label(janela, text="País:").pack(anchor="w", padx=40)
lbl_pais_valor = tk.Label(janela, text="-")
lbl_pais_valor.pack(anchor="w", padx=40)

# Botao
tk.Button(
    janela,
    text="Buscar Usuário",
    command=acao_buscar,
    width=25
).pack(pady=20)

janela.mainloop()
