import tkinter as tk

def somar(event=None):
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        resultado_var.set(f"Resultado: {n1 + n2}")
    except ValueError:
        resultado_var.set("Digite números válidos")

# Janela
janela = tk.Tk()
janela.title("Calculadora de Soma")
janela.geometry("250x180")

# Labels e entradas
tk.Label(janela, text="Número 1").pack(pady=5)
entrada1 = tk.Entry(janela)
entrada1.pack()
entrada1.focus()  # foco inicial

tk.Label(janela, text="Número 2").pack(pady=5)
entrada2 = tk.Entry(janela)
entrada2.pack()

# Botão
botao = tk.Button(janela, text="Somar", command=somar)
botao.pack(pady=10)

# Resultado
resultado_var = tk.StringVar(value="Resultado:")
resultado = tk.Label(janela, textvariable=resultado_var)
resultado.pack()

# Enter funciona em qualquer lugar da janela
janela.bind("<Return>", somar)

janela.mainloop()
