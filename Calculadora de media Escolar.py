import tkinter as tk
from tkinter import messagebox

def calcular_media():
    try:
        materia = entry_materia.get()

        notas = [
            float(entry_nota1.get()),
            float(entry_nota2.get()),
            float(entry_nota3.get()),
            float(entry_nota4.get())
        ]

        if materia == "":
            messagebox.showwarning("Aviso", "Informe o nome da materia.")
            return

        for nota in notas:
            if nota < 0 or nota > 10:
                messagebox.showwarning(
                    "Aviso",
                    "As notas devem estar entre 0 e 10."
                )
                return

        media = sum(notas) / 4

        if media >= 7:
            situacao = "Aprovado"
        elif media >= 5:
            situacao = "Recuperacao"
        else:
            situacao = "Reprovado"

        resultado.config(
            text=(
                f"Materia: {materia}\n\n"
                f"Semestre 1: {notas[0]:.2f}\n"
                f"Semestre 2: {notas[1]:.2f}\n"
                f"Semestre 3: {notas[2]:.2f}\n"
                f"Semestre 4: {notas[3]:.2f}\n\n"
                f"Media Final: {media:.2f}\n"
                f"Resultado Final: {situacao}"
            )
        )

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite apenas valores numericos nas notas."
        )

# Janela
janela = tk.Tk()
janela.title("Media Escolar por Materia")
janela.geometry("520x580")
janela.resizable(True, True)

# Materia
tk.Label(janela, text="Nome da materia:").pack(pady=4)
entry_materia = tk.Entry(janela, width=35)
entry_materia.pack(pady=4)

# Notas
tk.Label(janela, text="Nota semestre 1:").pack(pady=3)
entry_nota1 = tk.Entry(janela)
entry_nota1.pack(pady=3)

tk.Label(janela, text="Nota semestre 2:").pack(pady=3)
entry_nota2 = tk.Entry(janela)
entry_nota2.pack(pady=3)

tk.Label(janela, text="Nota semestre 3:").pack(pady=3)
entry_nota3 = tk.Entry(janela)
entry_nota3.pack(pady=3)

tk.Label(janela, text="Nota semestre 4:").pack(pady=3)
entry_nota4 = tk.Entry(janela)
entry_nota4.pack(pady=3)

# Botao
tk.Button(
    janela,
    text="Calcular resultado final",
    command=calcular_media
).pack(pady=10)

# Resultado
resultado = tk.Label(
    janela,
    text="",
    font=("Arial", 11),
    justify="left",
    wraplength=480
)
resultado.pack(pady=15)

janela.mainloop()
