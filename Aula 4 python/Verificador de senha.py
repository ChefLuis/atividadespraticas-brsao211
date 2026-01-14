import tkinter as tk

def verificar_senha():
    senha = entry_senha.get()

    erros = []
    especiais = "!@#$%&*()-_=+[]{};:,.<>?/"

    if len(senha) < 8:
        erros.append("• Mínimo de 8 caracteres")

    if not any(c.isdigit() for c in senha):
        erros.append("• Pelo menos um número")

    if not any(c.isupper() for c in senha):
        erros.append("• Pelo menos uma letra maiúscula")

    if not any(c in especiais for c in senha):
        erros.append("• Pelo menos um caractere especial")

    if erros:
        label_resultado.config(
            text="Senha fraca:\n" + "\n".join(erros),
            fg="red"
        )
    else:
        label_resultado.config(
            text="Senha forte ✔",
            fg="green"
        )

# ---------- INTERFACE ----------
janela = tk.Tk()
janela.title("Verificador de Senha Forte")
janela.geometry("420x280")
janela.resizable(False, False)

label_titulo = tk.Label(janela, text="Digite a senha:", font=("Arial", 12))
label_titulo.pack(pady=10)

entry_senha = tk.Entry(janela, width=30, show="*", font=("Arial", 12))
entry_senha.pack()

botao_verificar = tk.Button(
    janela,
    text="Verificar Senha",
    width=20,
    command=verificar_senha
)
botao_verificar.pack(pady=15)

label_resultado = tk.Label(janela, text="", font=("Arial", 11), justify="left")
label_resultado.pack(pady=10)

janela.mainloop()
