import tkinter as tk
from tkinter import messagebox
import requests
import webbrowser


# ======================================================
# FUNÇÃO: CONSULTAR CEP NA API VIACEP
# ======================================================
def consultar_cep(cep: str) -> dict:
    """
    Consulta um CEP na API ViaCEP.
    Aceita CEP com ou sem hífen.
    Retorna um dicionário com os dados do endereço.
    """

    # Remove hífen e espaços
    cep_limpo = cep.replace("-", "").strip()

    # Validação básica do CEP
    if len(cep_limpo) != 8 or not cep_limpo.isdigit():
        raise ValueError("CEP inválido. Use o formato 00000-000.")

    # URL da API
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    resposta = requests.get(url, timeout=5)

    if resposta.status_code != 200:
        raise ConnectionError("Erro ao acessar a API ViaCEP.")

    dados = resposta.json()

    if "erro" in dados:
        raise ValueError("CEP não encontrado.")

    return dados


# ======================================================
# AÇÃO DO BOTÃO "CONSULTAR"
# ======================================================
def acao_consultar():
    try:
        cep = entrada_cep.get()
        dados = consultar_cep(cep)

        # Atualiza os labels com os dados retornados
        lbl_logradouro_valor.config(text=dados.get("logradouro", "-"))
        lbl_bairro_valor.config(text=dados.get("bairro", "-"))
        lbl_cidade_valor.config(text=dados.get("localidade", "-"))
        lbl_estado_valor.config(text=dados.get("uf", "-"))

        # Monta endereço para o Google Maps
        endereco_maps = f"{dados.get('logradouro','')}, {dados.get('bairro','')}, {dados.get('localidade','')} - {dados.get('uf','')}"

        # Ativa o botão do Google Maps
        btn_maps.config(
            state=tk.NORMAL,
            command=lambda: abrir_google_maps(endereco_maps)
        )

    except ValueError as erro:
        messagebox.showerror("Erro", str(erro))
    except Exception:
        messagebox.showerror("Erro", "Falha na conexão com a API.")


# ======================================================
# ABRE O ENDEREÇO NO GOOGLE MAPS
# ======================================================
def abrir_google_maps(endereco: str):
    url = f"https://www.google.com/maps/search/?api=1&query={endereco}"
    webbrowser.open(url)


# ======================================================
# INTERFACE GRÁFICA (TKINTER)
# ======================================================
janela = tk.Tk()
janela.title("Consulta de CEP")
janela.geometry("700x400")
janela.resizable(False, False)
janela.configure(bg="#f2f2f2")

# ---------------- FRAME ESQUERDO ----------------
frame_esq = tk.Frame(janela, bg="#f2f2f2", padx=20, pady=20)
frame_esq.pack(side=tk.LEFT, fill=tk.Y)

tk.Label(
    frame_esq,
    text="CEP (com hífen)",
    font=("Arial", 11, "bold"),
    bg="#f2f2f2"
).pack(anchor="w")

entrada_cep = tk.Entry(frame_esq, width=20, font=("Arial", 11))
entrada_cep.pack(pady=5)

tk.Button(
    frame_esq,
    text="Consultar",
    width=15,
    command=acao_consultar
).pack(pady=10)

btn_maps = tk.Button(
    frame_esq,
    text="Abrir no Google Maps",
    width=20,
    state=tk.DISABLED
)
btn_maps.pack(pady=10)

# ---------------- FRAME DIREITO ----------------
frame_dir = tk.Frame(janela, bg="white", padx=20, pady=20)
frame_dir.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

def criar_label(texto, linha):
    tk.Label(
        frame_dir,
        text=texto,
        bg="white",
        font=("Arial", 10, "bold"),
        anchor="w"
    ).grid(row=linha, column=0, sticky="w", pady=5)

def criar_valor(linha):
    lbl = tk.Label(
        frame_dir,
        text="-",
        bg="white",
        font=("Arial", 10),
        anchor="w"
    )
    lbl.grid(row=linha, column=1, sticky="w", pady=5)
    return lbl

criar_label("Logradouro:", 0)
lbl_logradouro_valor = criar_valor(0)

criar_label("Bairro:", 1)
lbl_bairro_valor = criar_valor(1)

criar_label("Cidade:", 2)
lbl_cidade_valor = criar_valor(2)

criar_label("Estado:", 3)
lbl_estado_valor = criar_valor(3)

# Mantém a janela aberta
janela.mainloop()
