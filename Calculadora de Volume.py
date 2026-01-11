import tkinter as tk

def calcular(event=None):
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        n3 = float(entrada3.get())
        resultado.config(text=f"Resultado: {n1 * n2 * n3}")
    except ValueError:
        resultado.config(text="Digite números válidos")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora de Volume")
janela.geometry("250x200")

# Entradas
tk.Label(janela, text="Valor 1").pack()
entrada1 = tk.Entry(janela)
entrada1.pack()
entrada1.focus()

tk.Label(janela, text="Valor 2").pack()
entrada2 = tk.Entry(janela)
entrada2.pack()

tk.Label(janela, text="Valor 3").pack()
entrada3 = tk.Entry(janela)
entrada3.pack()

# Botão
tk.Button(janela, text="Calcular", command=calcular).pack(pady=10)

# Resultado
resultado = tk.Label(janela, text="Resultado:")
resultado.pack()

# Enter funciona
janela.bind("<Return>", calcular)

# ESSENCIAL
janela.mainloop()
