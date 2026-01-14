import tkinter as tk

pares = 0
impares = 0

def analisar():
    global pares, impares

    valor = entrada.get()

    try:
        numero = int(valor)
    except ValueError:
        resultado["text"] = "Digite um número inteiro válido"
        resultado["fg"] = "red"
        return

    if numero % 2 == 0:
        pares += 1
        resultado["text"] = f"{numero} é PAR"
        resultado["fg"] = "green"
    else:
        impares += 1
        resultado["text"] = f"{numero} é ÍMPAR"
        resultado["fg"] = "blue"

    label_pares["text"] = f"Pares: {pares}"
    label_impares["text"] = f"Ímpares: {impares}"

    entrada.delete(0, tk.END)

# -------- INTERFACE --------
janela = tk.Tk()
janela.title("Identificação de Par e Ímpar")
janela.geometry("360x300")
janela.resizable(False, False)

tk.Label(janela, text="Digite um número:", font=("Arial", 12)).pack(pady=10)

entrada = tk.Entry(janela, font=("Arial", 12), width=20)
entrada.pack()
entrada.bind("<Return>", lambda e: analisar())

tk.Button(janela, text="Adicionar", command=analisar).pack(pady=15)

resultado = tk.Label(janela, text="", font=("Arial", 11))
resultado.pack(pady=5)

label_pares = tk.Label(janela, text="Pares: 0", font=("Arial", 11))
label_pares.pack(pady=5)

label_impares = tk.Label(janela, text="Ímpares: 0", font=("Arial", 11))
label_impares.pack(pady=5)

janela.mainloop()
