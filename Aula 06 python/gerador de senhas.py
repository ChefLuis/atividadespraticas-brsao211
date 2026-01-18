import tkinter as tk
import re


# ==============================
# FUNCAO DE VALIDACAO
# ==============================

def validar_senha(event=None):
    senha = entrada_senha.get()

    # Regras de validacao
    tem_tamanho = len(senha) >= 8
    tem_letra = bool(re.search(r"[A-Za-z]", senha))
    tem_numero = bool(re.search(r"[0-9]", senha))
    tem_especial = bool(re.search(r"[^A-Za-z0-9]", senha))

    # Atualiza cores conforme validacao
    atualizar_label(lbl_tamanho, tem_tamanho)
    atualizar_label(lbl_letra, tem_letra)
    atualizar_label(lbl_numero, tem_numero)
    atualizar_label(lbl_especial, tem_especial)

    # Valida senha completa
    if tem_tamanho and tem_letra and tem_numero and tem_especial:
        resultado.set("Senha forte")
        lbl_resultado.config(fg="green")
    else:
        resultado.set("Senha fraca")
        lbl_resultado.config(fg="red")


def atualizar_label(label, valido):
    if valido:
        label.config(fg="green")
    else:
        label.config(fg="red")


# ==============================
# INTERFACE
# ==============================

janela = tk.Tk()
janela.title("Validador de Senha")
janela.geometry("420x350")
janela.resizable(False, False)

tk.Label(
    janela,
    text="Validação de Senha",
    font=("Arial", 14, "bold")
).pack(pady=15)

tk.Label(
    janela,
    text="Digite sua senha:"
).pack()

entrada_senha = tk.Entry(janela, width=35, show="*")
entrada_senha.pack(pady=8)

# Valida a cada tecla digitada
entrada_senha.bind("<KeyRelease>", validar_senha)

# Regras visuais
lbl_tamanho = tk.Label(janela, text="• Mínimo 8 caracteres", fg="red")
lbl_tamanho.pack(anchor="w", padx=40)

lbl_letra = tk.Label(janela, text="• Contém letras", fg="red")
lbl_letra.pack(anchor="w", padx=40)

lbl_numero = tk.Label(janela, text="• Contém números", fg="red")
lbl_numero.pack(anchor="w", padx=40)

lbl_especial = tk.Label(janela, text="• Contém caracteres especiais", fg="red")
lbl_especial.pack(anchor="w", padx=40)

resultado = tk.StringVar()

lbl_resultado = tk.Label(
    janela,
    textvariable=resultado,
    font=("Arial", 12, "bold")
)
lbl_resultado.pack(pady=20)

janela.mainloop()
