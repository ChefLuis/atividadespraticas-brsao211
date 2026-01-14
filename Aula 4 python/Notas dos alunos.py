import tkinter as tk
from tkinter import messagebox

# ---------------- DADOS ----------------
alunos = {}

# ---------------- FUNÇÕES ----------------
def adicionar():
    nome = entry_nome.get().strip()

    try:
        nota = float(entry_nota.get())
        if nota < 0 or nota > 10:
            raise ValueError
    except:
        messagebox.showerror("Erro", "Nota inválida (0 a 10)")
        return

    if nome == "":
        messagebox.showerror("Erro", "Digite o nome do aluno")
        return

    if nome not in alunos:
        alunos[nome] = []

    if len(alunos[nome]) >= 4:
        messagebox.showerror("Erro", "Este aluno já possui 4 notas")
        return

    alunos[nome].append(nota)

    entry_nome.delete(0, tk.END)
    entry_nota.delete(0, tk.END)

    atualizar_lista()

def atualizar_lista():
    lista.delete(0, tk.END)

    for nome, notas in alunos.items():
        media = sum(notas) / len(notas)
        lista.insert(
            tk.END,
            f"{nome} | Notas: {notas} | Média: {media:.2f}"
        )

# ---------------- TELA DE CONSULTA ----------------
def abrir_consulta():
    janela_c = tk.Toplevel(janela)
    janela_c.title("Consulta de Aluno")
    janela_c.geometry("400x320")
    janela_c.resizable(False, False)

    tk.Label(janela_c, text="Nome do aluno:").pack(pady=5)
    entry_busca = tk.Entry(janela_c, width=30)
    entry_busca.pack()

    resultado = tk.Label(janela_c, text="", font=("Arial", 11), justify="left")
    resultado.pack(pady=10)

    def buscar():
        nome = entry_busca.get().strip()

        if nome not in alunos:
            resultado.config(text="Aluno não encontrado")
            return

        notas = alunos[nome]

        texto = "Notas:\n"
        for i, n in enumerate(notas, start=1):
            texto += f"Nota {i}: {n}\n"

        if len(notas) == 4:
            media = sum(notas) / 4
            texto += f"\nMédia final: {media:.2f}"
        else:
            texto += "\nAluno ainda não possui 4 notas"

        resultado.config(text=texto)

    tk.Button(janela_c, text="Buscar", command=buscar).pack(pady=5)

# ---------------- INTERFACE PRINCIPAL ----------------
janela = tk.Tk()
janela.title("Sistema de Notas")
janela.geometry("650x420")
janela.resizable(False, False)

frame_topo = tk.Frame(janela)
frame_topo.pack(pady=10)

tk.Label(frame_topo, text="Aluno:").grid(row=0, column=0, padx=5)
entry_nome = tk.Entry(frame_topo, width=25)
entry_nome.grid(row=0, column=1, padx=5)

tk.Label(frame_topo, text="Nota:").grid(row=0, column=2, padx=5)
entry_nota = tk.Entry(frame_topo, width=10)
entry_nota.grid(row=0, column=3, padx=5)

tk.Button(
    frame_topo,
    text="Adicionar",
    width=15,
    command=adicionar
).grid(row=1, column=1, columnspan=3, pady=8)

lista = tk.Listbox(janela, width=90, height=10)
lista.pack(padx=10, pady=10)

tk.Button(
    janela,
    text="Abrir Consulta",
    width=25,
    command=abrir_consulta
).pack(pady=5)

janela.mainloop()
